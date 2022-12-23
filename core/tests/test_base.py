from django.test import TestCase
from django.contrib.auth.models import User

class TestBase(TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def create_user(self):
        user = User.objects.create_user(username='teste1', password='123456')
        user.save()
        return user

    def login(self):
        user_logged = self.client.login(username='teste1', password='123456')
        return user_logged