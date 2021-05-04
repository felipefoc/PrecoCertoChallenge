from django.test import RequestFactory, TestCase, Client
from django.urls.base import reverse
from accounts.models import CustomUser
from companies.models import Company
from products.models import Products


# Create your tests here.
class CompanyTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()     
        self.company = Company.objects.create(
            name='TEST COMPANY LTDA',
            cnpj='19.210.614/0001-26',
        )
        self.user = CustomUser.objects.create_user(
            username='TestUser',
            password='User@123',
            company=self.company
        )
        self.data = {'username': 'TestUser',
                    'password': 'User@123'}

        self.admin = CustomUser.objects.create_user(
            username='AdminUser',
            password='User@123',
            is_superuser=True,
            is_staff=True
        )
        self.admin_data = {
            'username': 'AdminUser',
            'password': 'User@123'
        }
        self.product = Products.objects.create(
            name='Test Product',
            price=845.99,
            cost=50.00,
            company=Company.objects.get(id=1)
        )
        self.product_data = {
            'name': 'New Product',
            'price': 849.99,
            'cost': 147.99,
            'company': 'TEST COMPANY LTDA',
        }

        self.login = reverse('login')
        self.logout = reverse('logout')
        self.company_list = reverse('company-list')
        self.signup = reverse('signup')
        self.create_product = reverse('product-create')
        self.delete_company = reverse('company-delete', args={
            '1': self.company.id
        })
        self.update_company = reverse('company-update', kwargs={
            'pk': 1
        })

    def test_create_product_as_superuser(self):
        self.client.post(self.login, self.admin_data)
        res = self.client.post(self.create_product, self.product_data)
        self.assertEqual(res.status_code, 200)