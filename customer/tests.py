from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import State, City, Place, CustomUser, customerUser, Contact, Customer, Order

class ModelsTestCase(TestCase):

    def setUp(self):
        # Set up initial data for tests
        self.state = State.objects.create(name="Test State")
        self.city = City.objects.create(name="Test City", state=self.state)
        self.place = Place.objects.create(name="Test Place", city=self.city)

        self.customer_user = CustomUser.objects.create_user(
            username="testuser",
            password="password123",
            is_user=True
        )

        self.customer = Customer.objects.create(
            name="Test Customer",
            address="123 Test Address",
            phone_number="1234567890",
            email="testcustomer@example.com",
            password="securepassword"
        )

        self.customer_user_profile = customerUser.objects.create(
            name="Test Customer",
            state=self.state,
            city=self.city,
            place="Test Place",
            address="123 Test Address",
            customer=self.customer
        )

        self.order = Order.objects.create(
            customer=self.customer_user_profile,
            item="Test Item",
            quantity=1,
            category="Test Category",
            sum_of_price=9.99,
            order_no="ORD123",
            restaurant_name="Test Restaurant",
        )

    def test_state_creation(self):
        self.assertEqual(self.state.name, "Test State")

    def test_city_creation(self):
        self.assertEqual(self.city.name, "Test City")
        self.assertEqual(self.city.state, self.state)

    def test_place_creation(self):
        self.assertEqual(self.place.name, "Test Place")
        self.assertEqual(self.place.city, self.city)

    def test_customer_user_creation(self):
        self.assertTrue(self.customer_user.is_user)
        self.assertFalse(self.customer_user.is_restaurant)
        self.assertFalse(self.customer_user.is_delivery)

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "Test Customer")
        self.assertEqual(self.customer.phone_number, "1234567890")
        self.assertEqual(self.customer.email, "testcustomer@example.com")

    def test_customer_phone_number_validation(self):
        self.customer.phone_number = "invalidphone"
        with self.assertRaises(ValidationError):
            self.customer.clean()

    def test_order_creation(self):
        self.assertEqual(self.order.item, "Test Item")
        self.assertEqual(self.order.quantity, 1)
        self.assertEqual(self.order.category, "Test Category")
        self.assertEqual(self.order.sum_of_price, 9.99)
        self.assertEqual(self.order.order_no, "ORD123")
        self.assertEqual(self.order.restaurant_name, "Test Restaurant")

    def test_order_status_choices(self):
        choices = dict(self.order.get_status_choices)
        self.assertIn("PENDING", choices)
        self.assertIn("DELIVERED", choices)

    def test_get_orders_for_restaurant(self):
        orders = Order.get_orders_for_restaurant("Test Restaurant")
        self.assertIn(self.order, orders)

    def test_get_orders_for_delivery_person(self):
        self.order.delivery_person = "Test Delivery Person"
        self.order.save()
        orders = Order.get_orders_for_delivery_person("Test Delivery Person")
        self.assertIn(self.order, orders)

    def test_contact_creation(self):
        contact = Contact.objects.create(
            name="Test Contact",
            email="contact@example.com",
            subject="Test Subject"
        )
        self.assertEqual(contact.name, "Test Contact")
        self.assertEqual(contact.email, "contact@example.com")
        self.assertEqual(contact.subject, "Test Subject")

    def test_order_status_update(self):
        self.order.status = "DELIVERED"
        self.order.save()
        self.assertEqual(self.order.status, "DELIVERED")

    def test_order_comments(self):
        self.order.comments = "Test comment"
        self.order.save()
        self.assertEqual(self.order.comments, "Test comment")

    def test_customer_user_str(self):
        self.assertEqual(str(self.customer_user_profile), "Test Customer - Test Place, Test City, Test State")

    def test_order_str(self):
        self.assertEqual(str(self.order), "Order ORD123 - Test Customer")
        
  