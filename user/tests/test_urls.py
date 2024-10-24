from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user.views import index, register, logout, login, user_profile


class TestUrl(SimpleTestCase):

    def test_index_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_register_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_login_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_logout_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout)

    def test_profile_resolved(self):
        url = reverse('/u/12')
        self.assertEquals(resolve(url).func, user_profile)

