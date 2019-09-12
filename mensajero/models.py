from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.
class Mensaje(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha_creacion']

class HiloManager(models.Manager):
    def hallar(self, user1 , user2):
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            return queryset[0]
        return None

    def hallar_or_create(self, user1, user2):
        hilo = self.hallar(user1, user2)
        if hilo is None:
            hilo = Hilo.objects.create()
            hilo.users.add(user1, user2)
        return hilo

class Hilo(models.Model):
    users = models.ManyToManyField(User, related_name='hilos')
    mensajes = models.ManyToManyField(Mensaje)
    fecha_actualizar = models.DateTimeField(auto_now=True)

    objects = HiloManager()

    class Meta:
        ordering = ['-fecha_actualizar']


def mensajes_changed(sender, **kwargs):
    instance = kwargs.pop("instance", None)
    action = kwargs.pop("action", None)
    pk_set = kwargs.pop("pk_set", None)
    print(instance, action, pk_set)

    false_pk_set = set()
    if action is "pre_add":
        for msg_pk in pk_set:
            msg = Mensaje.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print("Ups, ({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk)
    
    #Buscar los mensajes de false_pk_set que si están en pk_set y borrarlos de pk_set
    pk_set.difference_update(false_pk_set)

    instance.save()

m2m_changed.connect(mensajes_changed, sender=Hilo.mensajes.through)