# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

# class ViewsTestCase(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

#     def test_home_view_requires_login(self):
#         response = self.client.get(reverse('home'))
#         self.assertRedirects(response, '/accounts/login/?next=/home/')

#     def test_login_view_get(self):
#         response = self.client.get(reverse('loginDelivery'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'loginDelivery.html')

#     def test_login_view_post(self):
#         response = self.client.post(reverse('loginDelivery'), {'email': 'testuser', 'password': 'testpassword'})
#         self.assertRedirects(response, reverse('home'))

#     def test_login_view_invalid_credentials(self):
#         response = self.client.post(reverse('loginDelivery'), {'email': 'wronguser', 'password': 'wrongpassword'})
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('loginDelivery'))
#         self.assertContains(response, 'Invalid Username or Password', status_code=200)

#     def test_register_view_get(self):
#         response = self.client.get(reverse('registerDelivery'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registerDelivery.html')

#     def test_register_view_post(self):
#         response = self.client.post(reverse('registerDelivery'), {'email': 'newuser@example.com', 'password': 'newpassword'})
#         self.assertRedirects(response, reverse('loginDelivery'))
#         self.assertTrue(get_user_model().objects.filter(username='newuser@example.com').exists())

#     def test_register_view_existing_user(self):
#         response = self.client.post(reverse('registerDelivery'), {'email': 'testuser', 'password': 'testpassword'})
#         self.assertRedirects(response, reverse('registerDelivery'))
#         self.assertContains(response, 'User already exists with this email address.', status_code=200)