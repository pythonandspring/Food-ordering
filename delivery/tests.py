from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from datetime import date
from customer.models import State, City, Place, CustomUser
from .models import deliveryUser, Feedback, Contact, DeliveryPerson, DeliveryPersonLocation

class DeliveryUserModelTest(TestCase):
    def setUp(self):
        self.state = State.objects.create(name="Test State")
        self.city = City.objects.create(name="Test City", state=self.state)
        self.delivery_user = deliveryUser.objects.create(
            username="deliveryuser",
            name="John Doe",
            address="123 Test Street",
            state=self.state,
            city=self.city,
            place="Test Place",
            latitude=12.345678,
            longitude=98.765432
        )

    def test_delivery_user_creation(self):
        self.assertEqual(str(self.delivery_user), "John Doe")

class FeedbackModelTest(TestCase):
    def setUp(self):
        self.feedback = Feedback.objects.create(
            stars=5,
            comments="Great service!"
        )

    def test_feedback_creation(self):
        self.assertEqual(self.feedback.stars, 5)
        self.assertEqual(self.feedback.comments, "Great service!")

class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name="Jane Doe",
            email="jane.doe@example.com",
            subject="Test Subject"
        )

    def test_contact_creation(self):
        self.assertEqual(str(self.contact), "Jane Doe")

class DeliveryPersonModelTest(TestCase):
    def setUp(self):
        self.delivery_person = DeliveryPerson.objects.create(
            first_name="John",
            last_name="Smith",
            email="john.smith@example.com",
            phone_number="1234567890",
            vehicle_type="Bike",
            license_number="1234-5678",
            status="active",
            rating=4.5,
            address="123 Delivery Lane",
            emergency_contact_name="Jane Doe",
            emergency_contact_phone="0987654321",
            vehicle_registration_date=date.today()
        )

    def test_delivery_person_creation(self):
        self.assertEqual(str(self.delivery_person), "John Smith")
        self.assertEqual(self.delivery_person.status, "active")

    def test_default_values(self):
        self.assertTrue(self.delivery_person.available_for_delivery)

class DeliveryPersonLocationModelTest(TestCase):
    def setUp(self):
        self.delivery_person = DeliveryPerson.objects.create(
            first_name="John",
            last_name="Smith",
            email="john.smith@example.com",
            phone_number="1234567890"
        )
        self.location = DeliveryPersonLocation.objects.create(
            delivery_person=self.delivery_person,
            latitude=12.345678,
            longitude=98.765432
        )

    def test_delivery_person_location_creation(self):
        self.assertEqual(
            str(self.location),
            "Location for John Smith"
        )
        self.assertEqual(self.location.latitude, 12.345678)
        self.assertEqual(self.location.longitude, 98.765432)