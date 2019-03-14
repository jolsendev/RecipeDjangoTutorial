from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create(
            email='admin@fake.com',
            password='test123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@fake.com',
            password = 'test1234',
            name ='Test user full name'
        )

    # https://docs.djangoproject.com/en/2.1/ref/contrib/admin/
    def test_for_users_listed(self):
        print(reverse('admin:core_user_changelist'))
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        print(res)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
