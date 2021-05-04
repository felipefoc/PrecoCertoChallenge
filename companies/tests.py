from django.test import RequestFactory, TestCase, Client
from django.urls.base import reverse
from accounts.models import CustomUser
from companies.models import Company


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
        self.admin_data = {'username': 'AdminUser',
                           'password': 'User@123'}

        self.login = reverse('login')
        self.logout = reverse('logout')
        self.company_list = reverse('company-list')
        self.signup = reverse('signup')
        self.create_company = reverse('company-create')
        self.delete_company = reverse('company-delete', args={
            '1': self.company.id
        })
        self.update_company = reverse('company-update', kwargs={
            'pk': 1
        })

    def test_if_no_allowed_user_can_access_restrict_company_list_page(self):
        self.client.post(self.login, self.data)
        res = self.client.get(self.company_list)
        self.assertEqual(res.status_code, 403)

    def test_if_not_logged_user_can_access_restrict_company_list_page(self):
        res = self.client.get(self.company_list)
        self.assertEqual(res.status_code, 302)
    
    def test_if_allowed_user_can_access_restrict_company_list_page(self):
        self.client.post(self.login, self.admin_data)
        res = self.client.get(self.company_list)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(str(self.admin.username), str(res.context['user']))

    def test_create_company_as_admin_with_valid_cnpj(self):
        self.client.post(self.login, self.admin_data)
        res = self.client.post(self.create_company, {
            'name': 'Test Company',
            'cnpj': '47.715.155/0001-78'
        })
        self.assertEqual(res.status_code, 302)

    def test_create_company_as_admin_with_invalid_cnpj(self):
        self.client.post(self.login, self.admin_data)
        res = self.client.post(self.create_company, {
            'name': 'Test Company',
            'cnpj': 'invalidcnpj'
        })
        self.assertEqual(res.status_code, 200)
    
    def test_create_company_as_user(self):
        self.client.post(self.login, self.data)
        res = self.client.post(self.create_company, {
            'name': 'Test Company',
            'cnpj': '47.715.155/0001-78'
        })
        self.assertEqual(res.status_code, 403)

    def test_delete_company_as_user(self):
        self.client.post(self.login, self.data)
        res = self.client.get(self.delete_company)
        self.assertEqual(res.status_code, 403)
    
    def test_delete_company_as_superuser(self):
        self.client.post(self.login, self.admin_data)
        res = self.client.get(self.delete_company)
        self.assertEqual(res.status_code, 302)

    def test_update_company_as_superuser(self):
        self.client.post(self.login, self.admin_data)
        res = self.client.post(self.update_company, {
            'name': 'UPDATE COMPANY LTDA',
            'cnpj': '13.161.431/0001-81'
        })
        self.company.refresh_from_db()
        self.assertEqual(res.status_code, 302)
        self.assertTrue(Company.objects.get(pk=1).name == 'UPDATE COMPANY LTDA')

    def test_update_company_as_user(self):
        self.client.post(self.login, self.data)
        res = self.client.post(self.update_company, {
            'name': 'UPDATE COMPANY LTDA',
            'cnpj': '13.161.431/0001-81'
        })
        self.company.refresh_from_db()
        self.assertEqual(res.status_code, 403)
        self.assertFalse(Company.objects.get(pk=1).name == 'UPDATE COMPANY LTDA')

    


        
