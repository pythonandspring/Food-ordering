import unittest
from django.test import TestCase
from django.core.exceptions import ValidationError
from customer.models import Customer, Feedback, Contact

class CustomerRegressionTest(TestCase):

    # Regression tests for the Customer model

    def setUp(self):
        """Set up test data"""
        self.valid_customer = Customer.objects.create(
            name="John Doe",
            address="123 Main St",
            phone_number="9822751921",
            email="john@example.com",
            password="securepassword123"
        )
        # Call full_clean to ensure the object is valid
        self.valid_customer.full_clean()
    
    def test_regression_customer_update_without_changes(self):
        # """Test that saving a customer without changes doesn't affect the data"""
        original_data = {
            'name': self.valid_customer.name,
            'address': self.valid_customer.address,
            'phone_number': self.valid_customer.phone_number,
            'email': self.valid_customer.email
        }
        
        self.valid_customer.save()
        self.valid_customer.refresh_from_db()
        
        for field, value in original_data.items():
            self.assertEqual(getattr(self.valid_customer, field), value)

    def test_regression_partial_update(self):
        # """Test updating only some fields doesn't affect others"""
        original_phone = self.valid_customer.phone_number
        original_email = self.valid_customer.email
        
        self.valid_customer.name = "Jane Doe"
        self.valid_customer.address = "456 New St"
        self.valid_customer.full_clean()
        self.valid_customer.save()
        
        self.valid_customer.refresh_from_db()
        
        self.assertEqual(self.valid_customer.name, "Jane Doe")
        self.assertEqual(self.valid_customer.address, "456 New St")
        self.assertEqual(self.valid_customer.phone_number, original_phone)
        self.assertEqual(self.valid_customer.email, original_email)

    def test_regression_model_integrity(self):
        # """Test model data integrity under various conditions"""
        # Test repeated saves
        original_name = self.valid_customer.name
        for _ in range(5):
            self.valid_customer.save()
            self.valid_customer.refresh_from_db()
            self.assertEqual(self.valid_customer.name, original_name)

    def test_regression_phone_validation(self):
        # Test phone number validation
        valid_numbers = [
            "1234567890",      # 10 digits
            "12345678901",     # 11 digits
            "123456789012345"  # 15 digits
        ]
        
        invalid_numbers = [
            "123456789",       # 9 digits (too short)
            "1234567890123456",# 16 digits (too long)
            "abcd1234567",     # contains letters
            "123-456-7890",    # contains hyphens
            "+1234567890"      # contains plus sign
        ]
        
        # Test valid numbers
        for number in valid_numbers:
            self.valid_customer.phone_number = number
            try:
                self.valid_customer.full_clean()
            except ValidationError:
                self.fail(f"Valid phone number {number} raised ValidationError")
        
        # Test invalid numbers
        for number in invalid_numbers:
            self.valid_customer.phone_number = number
            with self.assertRaises(ValidationError):
                self.valid_customer.full_clean()

    def test_regression_model_relationships(self):
        # Test relationships between Customer and other models
        # Create feedbacks
        feedbacks = []
        for i in range(1, 6):
            feedback = Feedback.objects.create(
                stars=i,
                comments=f"Feedback {i}"
            )
            feedbacks.append(feedback)
        
        # Create contacts
        contact1 = Contact.objects.create(
            name=self.valid_customer.name,
            email=self.valid_customer.email,
            subject="Test Subject 1"
        )
        
        contact2 = Contact.objects.create(
            name="Different Name",
            email=self.valid_customer.email,
            subject="Test Subject 2"
        )
        
        # Verify data integrity
        self.assertEqual(Feedback.objects.count(), len(feedbacks))
        self.assertEqual(
            Contact.objects.filter(email=self.valid_customer.email).count(), 
            2
        )

    def test_regression_field_limits(self):
        # Test field length limits
        # Test name field (max_length=100)
        self.valid_customer.name = "A" * 100
        self.valid_customer.full_clean()  # Should not raise error
        
        with self.assertRaises(ValidationError):
            self.valid_customer.name = "A" * 101
            self.valid_customer.full_clean()
        
        # Test address field (max_length=255)
        self.valid_customer.name = "John Doe"  # Reset name
        self.valid_customer.address = "A" * 255
        self.valid_customer.full_clean()  # Should not raise error
        
        with self.assertRaises(ValidationError):
            self.valid_customer.address = "A" * 256
            self.valid_customer.full_clean()

class RegressionTestSuite(unittest.TestCase):
    # Main regression test suite that runs all regression tests
    
    def test_run_all_regression_tests(self):
        # Run all regression tests and ensure they pass
        suite = unittest.TestLoader().loadTestsFromTestCase(CustomerRegressionTest)
        runner = unittest.TextTestRunner(verbosity=2)  # Increased verbosity
        result = runner.run(suite)
        
        # Print more detailed error information
        if not result.wasSuccessful():
            print("\nFailed Tests:")
            for failure in result.failures:
                print(f"\nTest: {failure[0]}")
                print(f"Error: {failure[1]}")
            for error in result.errors:
                print(f"\nTest: {error[0]}")
                print(f"Error: {error[1]}")
                
        self.assertEqual(result.wasSuccessful(), True)
