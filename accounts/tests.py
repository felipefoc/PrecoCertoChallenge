from django.test import RequestFactory, TestCase, Client
from django.urls.base import reverse_lazy
from accounts.models import CustomUser

class AccountTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='TestUser',
            password='User@123'
        )
        self.data = {'username': 'TestUser',
                    'password': 'User@123'}
        self.login = reverse_lazy('login')
        self.restrict_page = reverse_lazy('company-create')

    def test_if_user_can_login(self):
        res = self.client.post(self.login, self.data)
        self.assertEqual(res.status_code, 302)
    
    def test_if_user_can_access_homepage_after_login(self):
        self.client.post(self.login, self.data)
        res = self.client.get('')
        self.assertEqual(res.status_code, 200)

    def test_if_normal_user_dont_have_permission_to_acess_page(self):
        self.client.post(self.login, self.data)
        res = self.client.get(self.restrict_page)
        self.assertEqual(res.status_code, 403)




    