from core.tests import test_base
from django.urls import reverse

class TestAuthViews(test_base.TestBase):
    def test_register_page(self):
        response_200 = self.client.get(reverse('register'))
        self.assertEqual(response_200.status_code, 200)
        # self.assertTemplateUsed(response_200, "register.html")
    
    def test_register(self):
        response_200 = self.client.post(reverse('register'), {
            "username": "teste2",
            "email": "teste@gmail.com",
            "password": "teste123"
        }, follow=True)
        self.assertEqual(response_200.status_code, 200)
        self.assertTemplateUsed(response_200, "login.html")

    def test_login(self):
        self.create_user()
        response_200 = self.client.post(reverse('login'), {
            "username": "teste1",
            "password": "123456"
        }, follow=True)
        self.assertEqual(response_200.status_code, 200)
    
    def test_login_user_doenst_exist(self):
        response_200 = self.client.post(reverse('login'), {
            "username": "teste2",
            "password": "teste123"
        }, follow=True)
        self.assertEqual(response_200.status_code, 200)
    
    def test_login_without_username(self):
        response_200 = self.client.post(reverse('login'), {
            "username": "",
            "password": ""
        }, follow=True)
        self.assertEqual(response_200.status_code, 200)

    def test_logout(self):
        self.create_user()
        self.client.login()
        response_200 = self.client.post(reverse('logout'), follow=True)
        self.assertEqual(response_200.status_code, 200)