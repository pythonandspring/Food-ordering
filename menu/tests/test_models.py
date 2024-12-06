from django.test import TestCase
from restaurant.models import Restaurant
from menu.models import Menu

class MenuModelTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(name="Test Restaurant")

    def test_create_menu(self):
        menu = Menu.objects.create(
            name="Pizza",
            image="images/pizza.jpg",
            restaurant=self.restaurant,
            availability=True,
            cost=10.00
        )
        self.assertEqual(menu.name, "Pizza")
        self.assertEqual(menu.image, "images/pizza.jpg")
        self.assertEqual(menu.restaurant, self.restaurant)
        self.assertTrue(menu.availability)
        self.assertEqual(menu.cost, 10.00)

    def test_default_availability(self):
        menu = Menu.objects.create(
            name="Burger",
            image="images/burger.jpg",
            restaurant=self.restaurant,
            cost=5.00
        )
        self.assertTrue(menu.availability)

    def test_on_delete_restaurant(self):
        menu = Menu.objects.create(
            name="Pasta",
            image="images/pasta.jpg",
            restaurant=self.restaurant,
            availability=True,
            cost=8.00
        )
        self.restaurant.delete()
        with self.assertRaises(Menu.DoesNotExist):
            menu.refresh_from_db()