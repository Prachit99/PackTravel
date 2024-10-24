from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user.views import index, register, logout, login, user_profile, my_rides


class TestUrl(SimpleTestCase):

    def test_search_resolved(self):
        url = reverse("search")
        self.assertEquals(resolve(url).func, my_rides)

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
        url = reverse('user_profile', args=["123"])
        self.assertEquals(resolve(url).func, user_profile)

