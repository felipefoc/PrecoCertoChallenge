from django.test import RequestFactory, TestCase, Client
from django.urls.base import reverse_lazy
from accounts.models import CustomUser
from companies.models import Company

class AccountTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='TestUser',
            password='User@123'
        )
        self.data = {'username': 'TestUser',
                    'password': 'User@123'}

        self.admin = CustomUser.objects.create_user(
            username='AdminUser',
            password='User@123',
            is_superuser=True,
            is_staff=True
        )
        self.admin_data = {'username': 'AdminUser',
                           'password': 'User@123'}
        self.company = Company.objects.create(
            name='TEST COMPANY LTDA',
            cnpj='19.210.614/0001-26',
        )
        self.login = reverse_lazy('login')
        self.logout = reverse_lazy('logout')
        self.home = reverse_lazy('home')
        self.signup = reverse_lazy('signup')
        self.create_comapany = reverse_lazy('company-create')

    def test_if_user_can_login(self):
        res = self.client.post(self.login, self.data)
        self.assertEqual(res.status_code, 302)
    
    def test_if_user_can_access_homepage_after_login(self):
        self.client.post(self.login, self.data)
        res = self.client.get('')
        self.assertEqual(res.status_code, 200)

    def test_if_normal_user_dont_have_permission_to_acess_page(self):
        self.client.post(self.login, self.data)
        res = self.client.get(self.create_comapany)
        self.assertEqual(res.status_code, 403)

    def test_logout(self):
        res = self.client.get(self.logout)
        self.assertEqual(res.status_code, 302)
    
    def test_creating_new_user(self):
        self.client.post(self.login, self.admin_data)
        data = {
            'username': 'na',
        }
        res = self.client.post(self.signup, data)
        self.assertEqual(res.status_code, 202)

    