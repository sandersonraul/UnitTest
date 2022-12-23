from core.tests import test_base
from django.urls import reverse
from expenses.models import Category
import datetime

class TestExpensesViews(test_base.TestBase):

    def test_list_expenses(self):
        self.create_user()
        self.login()
        response_200 = self.client.get('/expenses/', follow=True)
        self.assertEqual(response_200.status_code, 200)
        self.assertTemplateUsed(response_200, "index.html")

    def test_create(self):
        self.create_user()
        self.login()
        category = Category.objects.create(name="rent")
        category.save()
        response_200 = self.client.post(reverse('add-expenses'), {
            "amount": 1.500,
            "description": "asdasda",
            "category": category,
            "date": datetime.date(2012, 12, 20),
            "expense_date": datetime.date(2012, 12, 20)
        }, follow=True)
        self.assertEqual(response_200.status_code, 200)
    
    def test_create_get(self):
        self.create_user()
        self.login()
        response_200 = self.client.get(reverse('add-expenses'), follow=True)
        self.assertEqual(response_200.status_code, 200)
    
    def test_create_without_description(self):
        self.create_user()
        self.login()
        category = Category.objects.create(name="rent")
        category.save()
        response_200 = self.client.post(reverse('add-expenses'), data={
            "amount": 1.500,
            "description": "",
            "category": category,
            "date": datetime.date(2012, 12, 20),
            "expense_date": datetime.date(2012, 12, 20)
        }, follow=True)
        self.assertEqual(response_200.status_code, 200)

    def test_create_without_amount(self):
        self.create_user()
        self.login()
        category = Category.objects.create(name="rent")
        category.save()
        response_200 = self.client.post(reverse('add-expenses'), data={
            "amount":"",
            "description": "",
            "category": category,
            "date": datetime.date(2012, 12, 20),
            "expense_date": datetime.date(2012, 12, 20)
        }, follow=True)
        self.assertEqual(response_200.status_code, 200)

    
