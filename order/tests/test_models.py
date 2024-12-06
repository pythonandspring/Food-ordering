from django.test import TestCase
from menu.models import Menu
from delivery.models import deliveryUser
from order.models import Order
from restaurant.models import Restaurant  # Import the Restaurant model

class OrderModelTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(name="Test Restaurant")  # Create a Restaurant instance
        self.menu_item = Menu.objects.create(name="Pizza", cost=10.00, restaurant=self.restaurant)  # Adjust fields as per Menu model
        self.delivery_user = deliveryUser.objects.create(name="John Doe")  # Adjust fields as per deliveryUser model
    def test_create_order(self):
        order = Order.objects.create(
            item=self.menu_item,
            quantity=2,
            sum_of_price=20.00,
            order_no="12345",
            status="PENDING",
            delivery_person=self.delivery_user,
            restaurant_name="Pizza Place",
            comments="Extra cheese"
        )
        self.assertEqual(order.item, self.menu_item)
        self.assertEqual(order.quantity, 2)
        self.assertEqual(order.sum_of_price, 20.00)
        self.assertEqual(order.order_no, "12345")
        self.assertEqual(order.status, "PENDING")
        self.assertEqual(order.delivery_person, self.delivery_user)
        self.assertEqual(order.restaurant_name, "Pizza Place")
        self.assertEqual(order.comments, "Extra cheese")

    def test_default_status(self):
        order = Order.objects.create(
            item=self.menu_item,
            quantity=1,
            sum_of_price=10.00,
            order_no="12346",
            restaurant_name="Pizza Place"
        )
        self.assertEqual(order.status, "PENDING")

    def test_on_delete_item(self):
        order = Order.objects.create(
            item=self.menu_item,
            quantity=1,
            sum_of_price=10.00,
            order_no="12347",
            delivery_person=self.delivery_user,
            restaurant_name="Pizza Place"
        )
        self.menu_item.delete()
        with self.assertRaises(Order.DoesNotExist):
            order.refresh_from_db()

    def test_on_delete_delivery_person(self):
        order = Order.objects.create(
            item=self.menu_item,
            quantity=1,
            sum_of_price=10.00,
            order_no="12348",
            delivery_person=self.delivery_user,
            restaurant_name="Pizza Place"
        )
        self.delivery_user.delete()
        order.refresh_from_db()
        self.assertIsNone(order.delivery_person)

    def test_comments_blank_null(self):
        order = Order.objects.create(
            item=self.menu_item,
            quantity=1,
            sum_of_price=10.00,
            order_no="12349",
            restaurant_name="Pizza Place"
        )
        self.assertIn(order.comments, ["", None])  # Adjust the assertion to handle None values