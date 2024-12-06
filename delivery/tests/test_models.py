# from decimal import Decimal
# from django.test import TestCase
# from delivery.models import DeliveryPerson

# class DeliveryPersonModelTest(TestCase):

#     def setUp(self):
#         self.delivery_person = DeliveryPerson.objects.create(
#             first_name="John",
#             last_name="Doe",
#             email="john.doe@example.com",
#             phone_number="1234567890",
#             vehicle_type="Bike",
#             license_number="ABC123456",
#             status="active",
#             current_location="123 Main St",
#             rating=Decimal('4.50'),
#             available_for_delivery=True,
#             bank_account_details="123456789",
#             address="123 Main St",
#             profile_picture_url="http://example.com/profile.jpg",
#             emergency_contact_name="Jane Doe",
#             emergency_contact_phone="0987654321",
#             vehicle_registration_date="2023-01-01",
#             last_login="2023-01-01T12:00:00Z",
#             note="No notes"
#         )

#     def test_delivery_person_creation(self):
#         self.assertIsInstance(self.delivery_person, DeliveryPerson)
#         self.assertEqual(self.delivery_person.first_name, "John")
#         self.assertEqual(self.delivery_person.last_name, "Doe")
#         self.assertEqual(self.delivery_person.email, "john.doe@example.com")
#         self.assertEqual(self.delivery_person.phone_number, "1234567890")
#         self.assertEqual(self.delivery_person.vehicle_type, "Bike")
#         self.assertEqual(self.delivery_person.license_number, "ABC123456")
#         self.assertEqual(self.delivery_person.status, "active")
#         self.assertEqual(self.delivery_person.current_location, "123 Main St")
#         self.assertEqual(self.delivery_person.rating, Decimal('4.50'))
#         self.assertTrue(self.delivery_person.available_for_delivery)
#         self.assertEqual(self.delivery_person.bank_account_details, "123456789")
#         self.assertEqual(self.delivery_person.address, "123 Main St")
#         self.assertEqual(self.delivery_person.profile_picture_url, "http://example.com/profile.jpg")
#         self.assertEqual(self.delivery_person.emergency_contact_name, "Jane Doe")
#         self.assertEqual(self.delivery_person.emergency_contact_phone, "0987654321")
#         self.assertEqual(str(self.delivery_person.vehicle_registration_date), "2023-01-01")
#         self.assertEqual(str(self.delivery_person.last_login), "2023-01-01 12:00:00+00:00")
#         self.assertEqual(self.delivery_person.note, "No notes")

#     def test_str_method(self):
#         self.assertEqual(str(self.delivery_person), "John Doe")  # Ensure it matches the string representation of the name

#     def test_edit_delivery_person(self):
#         self.delivery_person.first_name = "Jane"
#         self.delivery_person.last_name = "Smith"
#         self.delivery_person.email = "jane.smith@example.com"
#         self.delivery_person.phone_number = "0987654321"
#         self.delivery_person.vehicle_type = "Car"
#         self.delivery_person.license_number = "XYZ987654"
#         self.delivery_person.status = "inactive"
#         self.delivery_person.current_location = "456 Elm St"
#         self.delivery_person.rating = Decimal('4.80')
#         self.delivery_person.available_for_delivery = False
#         self.delivery_person.bank_account_details = "987654321"
#         self.delivery_person.address = "456 Elm St"
#         self.delivery_person.profile_picture_url = "http://example.com/profile2.jpg"
#         self.delivery_person.emergency_contact_name = "John Smith"
#         self.delivery_person.emergency_contact_phone = "1234567890"
#         self.delivery_person.vehicle_registration_date = "2023-02-01"
#         self.delivery_person.last_login = "2023-02-01T12:00:00Z"
#         self.delivery_person.note = "Updated notes"
#         self.delivery_person.save()

#         updated_delivery_person = DeliveryPerson.objects.get(id=self.delivery_person.id)
#         self.assertEqual(updated_delivery_person.first_name, "Jane")
#         self.assertEqual(updated_delivery_person.last_name, "Smith")
#         self.assertEqual(updated_delivery_person.email, "jane.smith@example.com")
#         self.assertEqual(updated_delivery_person.phone_number, "0987654321")
#         self.assertEqual(updated_delivery_person.vehicle_type, "Car")
#         self.assertEqual(updated_delivery_person.license_number, "XYZ987654")
#         self.assertEqual(updated_delivery_person.status, "inactive")
#         self.assertEqual(updated_delivery_person.current_location, "456 Elm St")
#         self.assertEqual(updated_delivery_person.rating, Decimal('4.80'))
#         self.assertFalse(updated_delivery_person.available_for_delivery)
#         self.assertEqual(updated_delivery_person.bank_account_details, "987654321")
#         self.assertEqual(updated_delivery_person.address, "456 Elm St")
#         self.assertEqual(updated_delivery_person.profile_picture_url, "http://example.com/profile2.jpg")
#         self.assertEqual(updated_delivery_person.emergency_contact_name, "John Smith")
#         self.assertEqual(updated_delivery_person.emergency_contact_phone, "1234567890")
#         self.assertEqual(str(updated_delivery_person.vehicle_registration_date), "2023-02-01")
#         self.assertEqual(str(updated_delivery_person.last_login), "2023-02-01 12:00:00+00:00")
#         self.assertEqual(updated_delivery_person.note, "Updated notes")

#     def test_delete_delivery_person(self):
#         delivery_person_id = self.delivery_person.id
#         self.delivery_person.delete()
#         with self.assertRaises(DeliveryPerson.DoesNotExist):
#             DeliveryPerson.objects.get(id=delivery_person_id)