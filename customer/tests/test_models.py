from django.test import TestCase
from django.core.exceptions import ValidationError
from customer.models import Customer

class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name="John Doe",
            address="123 Main St",
            phone_number="9822751921",
            email="john@example.com",
            password="securepassword123"
        )

    def test_customer_creation(self):
        self.assertIsInstance(self.customer, Customer)
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.address, "123 Main St")
        self.assertEqual(self.customer.phone_number, "9822751921")
        self.assertEqual(self.customer.email, "john@example.com")

    def test_str_method(self):
        self.assertEqual(str(self.customer), "John Doe")  # Ensure it matches the string representation of the name

    def test_invalid_phone_number(self):
        with self.assertRaises(ValidationError):
            customer = Customer(
                name="Jane Doe",
                address="456 Elm St",
                phone_number="invalidphone",
                email="jane@example.com",
                password="securepassword123"
            )
            customer.full_clean()  # This will trigger the validation

    def test_invalid_email(self):
        with self.assertRaises(ValidationError):
            customer = Customer(
                name="Jane Doe",
                address="456 Elm St",
                phone_number="9822751921",
                email="invalidemail",
                password="securepassword123"
            )
            customer.full_clean()  # This will trigger the validation

    def test_blank_name(self):
        with self.assertRaises(ValidationError):
            customer = Customer(
                name="",
                address="456 Elm St",
                phone_number="9822751921",
                email="jane@example.com",
                password="securepassword123"
            )
            customer.full_clean()  # This will trigger the validation

    def test_blank_address(self):
        with self.assertRaises(ValidationError):
            customer = Customer(
                name="Jane Doe",
                address="",
                phone_number="9822751921",
                email="jane@example.com",
                password="securepassword123"
            )
            customer.full_clean()  # This will trigger the validation

    def test_edit_customer(self):
        # Update the customer instance
        self.customer.name = "John Smith"
        self.customer.address = "456 Elm St"
        self.customer.phone_number = "9876543210"
        self.customer.email = "johnsmith@example.com"
        self.customer.save()

        # Retrieve the updated customer instance
        updated_customer = Customer.objects.get(id=self.customer.id)
        self.assertEqual(updated_customer.name, "John Smith")
        self.assertEqual(updated_customer.address, "456 Elm St")
        self.assertEqual(updated_customer.phone_number, "9876543210")
        self.assertEqual(updated_customer.email, "johnsmith@example.com")

    def test_delete_customer(self):
        customer_id = self.customer.id
        self.customer.delete()
        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(id=customer_id)
            