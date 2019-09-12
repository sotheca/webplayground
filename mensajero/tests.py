from django.test import TestCase
from django.contrib.auth.models import User
from .models import Hilo, Mensaje

# Create your tests here.
class HiloTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.user2 = User.objects.create_user('user2', None, 'test1234')
        self.user3 = User.objects.create_user('user3', None, 'test1234')

        self.hilo = Hilo.objects.create()

    def test_add_users_to_hilo(self):
        self.hilo.users.add(self.user1, self.user2)
        self.assertEqual(len(self.hilo.users.all()), 2)

    def test_filter_hilo_by_users(self):
        self.hilo.users.add(self.user1, self.user2)
        hilos = Hilo.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.hilo, hilos[0])

    def test_filter_non_existent_hilo(self):
        hilos = Hilo.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(len(hilos), 0)

    def test_add_mensajes_to_hilo(self):
        self.hilo.users.add(self.user1, self.user2)
        mensaje1 = Mensaje.objects.create(user=self.user1, contenido="Hola que tal")
        mensaje2 = Mensaje.objects.create(user=self.user2, contenido="Todo bien y tú?")
        self.hilo.mensajes.add(mensaje1, mensaje2)
        self.assertEqual(len(self.hilo.mensajes.all()), 2)

        for mensaje in self.hilo.mensajes.all():
            print("({}): {}".format(mensaje.user, mensaje.contenido))

    def test_add_mensaje_from_user_not_in_hilo(self):
        self.hilo.users.add(self.user1, self.user2)
        mensaje1 = Mensaje.objects.create(user=self.user1, contenido="Hola que tal")
        mensaje2 = Mensaje.objects.create(user=self.user2, contenido="Todo bien y tú?")
        mensaje3 = Mensaje.objects.create(user=self.user3, contenido="Soy un espía")
        self.hilo.mensajes.add(mensaje1, mensaje2, mensaje3)
        self.assertEqual(len(self.hilo.mensajes.all()), 2)

    def test_hallar_hilo_with_custom_manager(self):
        self.hilo.users.add(self.user1, self.user2)
        hilo = Hilo.objects.hallar(self.user1, self.user2)
        self.assertEqual(self.hilo, hilo)

    def test_hallar_or_create_hilo_with_custom_manager(self):
        self.hilo.users.add(self.user1, self.user2)
        hilo = Hilo.objects.hallar_or_create(self.user1, self.user2)
        self.assertEqual(self.hilo, hilo)
        hilo = Hilo.objects.hallar_or_create(self.user1, self.user3)
        self.assertIsNotNone(hilo)