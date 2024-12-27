from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.core.exceptions import ValidationError
from restaurant.models import Restaurant, Cart, Product, Payment
from django.test import TestCase
from restaurant.models import State, City, Place, CustomUser
from customer.models import  customerUser, Contact, Customer, Order
from restaurant.models import restaurantUser, foodItems, Cart, Product, Payment

class RestaurantModelTest(TestCase):

    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            address="123 Test St",
            phone_number="1234567890",
            email="test@example.com"
        )

    def test_restaurant_creation(self):
        self.assertIsInstance(self.restaurant, Restaurant)
        self.assertEqual(self.restaurant.name, "Test Restaurant")
        self.assertEqual(self.restaurant.address, "123 Test St")
        self.assertEqual(self.restaurant.phone_number, "1234567890")
        self.assertEqual(self.restaurant.email, "test@example.com")

    def test_edit_restaurant(self):
        self.restaurant.name = "Updated Restaurant"
        self.restaurant.address = "456 Updated St"
        self.restaurant.phone_number = "0987654321"
        self.restaurant.email = "updated@example.com"
        self.restaurant.save()

        updated_restaurant = Restaurant.objects.get(id=self.restaurant.id)
        self.assertEqual(updated_restaurant.name, "Updated Restaurant")
        self.assertEqual(updated_restaurant.address, "456 Updated St")
        self.assertEqual(updated_restaurant.phone_number, "0987654321")
        self.assertEqual(updated_restaurant.email, "updated@example.com")

    def test_delete_restaurant(self):
        restaurant_id = self.restaurant.id
        self.restaurant.delete()
        with self.assertRaises(Restaurant.DoesNotExist):
            Restaurant.objects.get(id=restaurant_id)

    
            

class CartModelTest(TestCase):

    def setUp(self):
        self.cart = Cart.objects.create(
            number_of_products=3,
            product1="Burger",
            product2="Fries",
            product3="Soda",
            price=15.99,
            total=20.99
        )

    def test_edit_cart(self):
        self.cart.number_of_products = 5
        self.cart.product1 = "Pizza"
        self.cart.product2 = "Salad"
        self.cart.product3 = "Juice"
        self.cart.price = 25.99
        self.cart.total = 30.99
        self.cart.save()

        updated_cart = Cart.objects.get(id=self.cart.id)
        self.assertEqual(updated_cart.number_of_products, 5)
        self.assertEqual(updated_cart.product1, "Pizza")
        self.assertEqual(updated_cart.product2, "Salad")
        self.assertEqual(updated_cart.product3, "Juice")
        self.assertEqual(updated_cart.price, 25.99)
        self.assertEqual(updated_cart.total, 30.99)

    def test_delete_cart(self):
        cart_id = self.cart.id
        self.cart.delete()
        with self.assertRaises(Cart.DoesNotExist):
            Cart.objects.get(id=cart_id)

    def test_str_method(self):
        cart = Cart.objects.create(
            number_of_products=3,
            product1="Burger",
            product2="Fries",
            product3="Soda",
            price=15.99,
            total=20.99
        )
        self.assertEqual(str(cart), str(cart.id))  # Ensure it matches the string representation of the id
        
        

class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            category="Test Category",
            subcategory="Test Subcategory"
        )

    def test_edit_product(self):
        self.product.name = "Updated Product"
        self.product.category = "Updated Category"
        self.product.subcategory = "Updated Subcategory"
        self.product.save()

        updated_product = Product.objects.get(id=self.product.id)
        self.assertEqual(updated_product.name, "Updated Product")
        self.assertEqual(updated_product.category, "Updated Category")
        self.assertEqual(updated_product.subcategory, "Updated Subcategory")

    def test_delete_product(self):
        product_id = self.product.id
        self.product.delete()
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=product_id)

    def test_str_method(self):
        product = Product.objects.create(
            name="Test Product",
            category="Test Category",
            subcategory="Test Subcategory"
        )
        self.assertEqual(str(product), str(product.id))
        # Ensure it matches the string representation of the id
        
        

class PaymentModelTest(TestCase):

    def setUp(self):
        self.payment = Payment.objects.create(
            customer_id="cust123",
            name="John Doe",
            card_type="Visa",
            card_no="4111111111111111"
        )

    def test_create_payment(self):
        self.assertIsInstance(self.payment, Payment)
        self.assertEqual(self.payment.customer_id, "cust123")
        self.assertEqual(self.payment.name, "John Doe")
        self.assertEqual(self.payment.card_type, "Visa")
        self.assertEqual(self.payment.card_no, "4111111111111111")

    def test_edit_payment(self):
        self.payment.customer_id = "cust456"
        self.payment.name = "Jane Doe"
        self.payment.card_type = "MasterCard"
        self.payment.card_no = "5500000000000004"
        self.payment.save()

        updated_payment = Payment.objects.get(id=self.payment.id)
        self.assertEqual(updated_payment.customer_id, "cust456")
        self.assertEqual(updated_payment.name, "Jane Doe")
        self.assertEqual(updated_payment.card_type, "MasterCard")
        self.assertEqual(updated_payment.card_no, "5500000000000004")

    def test_delete_payment(self):
        payment_id = self.payment.id
        self.payment.delete()
        with self.assertRaises(Payment.DoesNotExist):
            Payment.objects.get(id=payment_id)

    def test_str_method(self):
        payment = Payment.objects.create(
            customer_id="cust123",
            name="John Doe",
            card_type="Visa",
            card_no="4111111111111111"
        )
        self.assertEqual(str(payment), "John Doe")  
        
        
        
        

class ModelsTestCase(TestCase):

    def setUp(self):
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

        self.restaurant_user = restaurantUser.objects.create(
            username="testrestaurant",
            password="password123",
            restaurantName="Test Restaurant",
            address="123 Restaurant Address",
            restaurantContact="+1234567890",
            state=self.state,
            city=self.city,
            place="Test Place"
        )

        self.food_item = foodItems.objects.create(
            name="Test Food Item",
            price=12.99,
            category="Test Category",
            restaurantName=self.restaurant_user
        )

        self.cart = Cart.objects.create(
            number_of_products=2,
            product1="Test Product 1",
            product2="Test Product 2",
            price=19.98,
            total=19.98
        )

        self.product = Product.objects.create(
            name="Test Product",
            category="Test Category",
            subcategory="Test Subcategory"
        )

        self.payment = Payment.objects.create(
            customer_id="12345",
            name="Test Payment",
            card_type="Visa",
            card_no="4111111111111111"
        )

    def test_edit_state(self):
        self.state.name = "Updated State"
        self.state.save()
        self.assertEqual(State.objects.get(id=self.state.id).name, "Updated State")

    def test_delete_city(self):
        city_id = self.city.id
        self.city.delete()
        with self.assertRaises(City.DoesNotExist):
            City.objects.get(id=city_id)

    def test_update_place(self):
        self.place.name = "Updated Place"
        self.place.save()
        self.assertEqual(Place.objects.get(id=self.place.id).name, "Updated Place")

    def test_edit_customer(self):
        self.customer.name = "Updated Customer"
        self.customer.save()
        self.assertEqual(Customer.objects.get(id=self.customer.id).name, "Updated Customer")

    
    def test_edit_cart(self):
        self.cart.number_of_products = 3
        self.cart.save()
        self.assertEqual(Cart.objects.get(id=self.cart.id).number_of_products, 3)


    def test_update_payment(self):
        self.payment.card_no = "4222222222222222"
        self.payment.save()
        self.assertEqual(Payment.objects.get(id=self.payment.id).card_no, "4222222222222222")