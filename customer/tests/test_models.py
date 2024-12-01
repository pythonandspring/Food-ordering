# from django.test import TestCase
# from customer.models import Customer
# from django.core.exceptions import ValidationError

# class CustomerModelTest(TestCase):

#     def setUp(self):
#         self.customer = Customer.objects.create(
#             name="John Doe",
#             address="123 Main St",
#             phone_number=1234567890,
#             email="john.doe@example.com"
#         )

#     def test_customer_creation(self):
#         self.assertIsInstance(self.customer, Customer)
#         self.assertEqual(self.customer.name, "John Doe")
#         self.assertEqual(self.customer.address, "123 Main St")
#         self.assertEqual(self.customer.phone_number, 1234567890)
#         self.assertEqual(self.customer.email, "john.doe@example.com")

#     def test_customer_str(self):
#         self.assertEqual(str(self.customer), "John Doe")

#     def test_required_fields(self):
#         with self.assertRaises(ValidationError):
#             Customer.objects.create(
#                 name="",
#                 address="",
#                 phone_number=None,
#                 email=""
#             ).full_clean()

#     def test_field_lengths(self):
#         customer = Customer.objects.create(
#             name="A" * 100,
#             address="B" * 255,
#             phone_number=1234567890,
#             email="email@example.com"
#         )
#         customer.full_clean()  # Should not raise any exceptions

#     def test_invalid_phone_number(self):
#         with self.assertRaises(ValidationError):
#             customer = Customer(
#                 name="Invalid Phone Number",
#                 address="123 Test St",
#                 phone_number="invalid_phone_number",
#                 email="test@example.com"
#             )
#             customer.full_clean()