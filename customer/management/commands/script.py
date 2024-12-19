import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from customer.models import State, City, Place, customerUser, Feedback, Contact, Order

fake = Faker()


class Command(BaseCommand):
    help = 'Create initial data for the customer app models'

    def handle(self, *args, **kwargs):
        self.create_states()
        self.create_cities()
        self.create_places()
        self.create_customers()
        self.create_feedbacks()
        self.create_contacts()
        self.create_orders()
        self.stdout.write(self.style.SUCCESS('Data created successfully!'))

    def create_states(self):
        states = [
            'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal',
            'Andaman and Nicobar Islands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Lakshadweep', 'Delhi', 'Puducherry', 'Ladakh', 'Jammu and Kashmir'
        ]
        State.objects.all().delete()
        for name in states:
            State.objects.create(name=name)
        print("States created")

    def create_cities(self):
        cities = [
            {'name': 'Visakhapatnam', 'state': 'Andhra Pradesh'},
            {'name': 'Itanagar', 'state': 'Arunachal Pradesh'},
            {'name': 'Guwahati', 'state': 'Assam'},
            {'name': 'Patna', 'state': 'Bihar'},
            {'name': 'Raipur', 'state': 'Chhattisgarh'},
            {'name': 'Panaji', 'state': 'Goa'},
            {'name': 'Ahmedabad', 'state': 'Gujarat'},
            {'name': 'Chandigarh', 'state': 'Haryana'},
            {'name': 'Shimla', 'state': 'Himachal Pradesh'},
            {'name': 'Ranchi', 'state': 'Jharkhand'},
            {'name': 'Bangalore', 'state': 'Karnataka'},
            {'name': 'Thiruvananthapuram', 'state': 'Kerala'},
            {'name': 'Bhopal', 'state': 'Madhya Pradesh'},
            {'name': 'Mumbai', 'state': 'Maharashtra'},
            {'name': 'Imphal', 'state': 'Manipur'},
            {'name': 'Shillong', 'state': 'Meghalaya'},
            {'name': 'Aizawl', 'state': 'Mizoram'},
            {'name': 'Kohima', 'state': 'Nagaland'},
            {'name': 'Bhubaneswar', 'state': 'Odisha'},
            {'name': 'Chandigarh', 'state': 'Punjab'},
            {'name': 'Jaipur', 'state': 'Rajasthan'},
            {'name': 'Gangtok', 'state': 'Sikkim'},
            {'name': 'Chennai', 'state': 'Tamil Nadu'},
            {'name': 'Hyderabad', 'state': 'Telangana'},
            {'name': 'Agartala', 'state': 'Tripura'},
            {'name': 'Lucknow', 'state': 'Uttar Pradesh'},
            {'name': 'Dehradun', 'state': 'Uttarakhand'},
            {'name': 'Kolkata', 'state': 'West Bengal'},
            {'name': 'Port Blair', 'state': 'Andaman and Nicobar Islands'},
            {'name': 'Chandigarh', 'state': 'Chandigarh'},
            {'name': 'Silvassa', 'state': 'Dadra and Nagar Haveli and Daman and Diu'},
            {'name': 'Kavaratti', 'state': 'Lakshadweep'},
            {'name': 'New Delhi', 'state': 'Delhi'},
            {'name': 'Puducherry', 'state': 'Puducherry'},
            {'name': 'Leh', 'state': 'Ladakh'},
            {'name': 'Srinagar', 'state': 'Jammu and Kashmir'}
        ]
        City.objects.all().delete()
        for city in cities:
            state = State.objects.get(name=city['state'])
            City.objects.create(name=city['name'], state=state)
        print("Cities created")

    def create_places(self):
        places = [
            {'name': 'Gajuwaka', 'city': 'Visakhapatnam'},
            {'name': 'Naharlagun', 'city': 'Itanagar'},
            {'name': 'Dispur', 'city': 'Guwahati'},
            {'name': 'Kankarbagh', 'city': 'Patna'},
            {'name': 'Pandri', 'city': 'Raipur'},
            {'name': 'Miramar', 'city': 'Panaji'},
            {'name': 'Navrangpura', 'city': 'Ahmedabad'},
            {'name': 'Sector 17', 'city': 'Chandigarh'},
            {'name': 'Mall Road', 'city': 'Shimla'},
            {'name': 'Harmu', 'city': 'Ranchi'},
            {'name': 'Koramangala', 'city': 'Bangalore'},
            {'name': 'Kovalam', 'city': 'Thiruvananthapuram'},
            {'name': 'Arera Colony', 'city': 'Bhopal'},
            {'name': 'Andheri', 'city': 'Mumbai'},
            {'name': 'Thangal Bazar', 'city': 'Imphal'},
            {'name': 'Police Bazar', 'city': 'Shillong'},
            {'name': 'Chaltlang', 'city': 'Aizawl'},
            {'name': 'Dimapur', 'city': 'Kohima'},
            {'name': 'Sahid Nagar', 'city': 'Bhubaneswar'},
            {'name': 'Sector 17', 'city': 'Chandigarh'},
            {'name': 'Malviya Nagar', 'city': 'Jaipur'},
            {'name': 'MG Marg', 'city': 'Gangtok'},
            {'name': 'T Nagar', 'city': 'Chennai'},
            {'name': 'Banjara Hills', 'city': 'Hyderabad'},
            {'name': 'Kaman Chowmuhani', 'city': 'Agartala'},
            {'name': 'Hazratganj', 'city': 'Lucknow'},
            {'name': 'Rajpur Road', 'city': 'Dehradun'},
            {'name': 'Park Street', 'city': 'Kolkata'},
            {'name': 'Aberdeen Bazaar', 'city': 'Port Blair'},
            {'name': 'Sector 17', 'city': 'Chandigarh'},
            {'name': 'Silvassa', 'city': 'Silvassa'},
            {'name': 'Kavaratti', 'city': 'Kavaratti'},
            {'name': 'Connaught Place', 'city': 'New Delhi'},
            {'name': 'White Town', 'city': 'Puducherry'},
            {'name': 'Leh Market', 'city': 'Leh'},
            {'name': 'Lal Chowk', 'city': 'Srinagar'}
        ]
        Place.objects.all().delete()
        for place in places:
            city = City.objects.filter(name=place['city']).first()
            if city:
                Place.objects.create(name=place['name'], city=city)
        print("Places created")

    def create_customers(self):
        customers = [
            {'name': 'John Doe', 'email': 'john@example.com', 'username': 'john', 'password': 'password123', 'state': 'Maharashtra', 'city': 'Mumbai', 'place': 'Andheri', 'latitude': 19.119677, 'longitude': 72.846222},
            {'name': 'Jane Smith', 'email': 'jane@example.com', 'username': 'jane', 'password': 'password123', 'state': 'Karnataka', 'city': 'Bangalore', 'place': 'Koramangala', 'latitude': 12.935192, 'longitude': 77.624480},
            {'name': 'Alice Johnson', 'email': 'alice@example.com', 'username': 'alice', 'password': 'password123', 'state': 'Tamil Nadu', 'city': 'Chennai', 'place': 'T Nagar', 'latitude': 13.0422, 'longitude': 80.2337},
            {'name': 'Bob Brown', 'email': 'bob@example.com', 'username': 'bob', 'password': 'password123', 'state': 'Uttar Pradesh', 'city': 'Lucknow', 'place': 'Hazratganj', 'latitude': 26.8500, 'longitude': 80.949997},
            {'name': 'Charlie Davis', 'email': 'charlie@example.com', 'username': 'charlie', 'password': 'password123', 'state': 'West Bengal', 'city': 'Kolkata', 'place': 'Park Street', 'latitude': 22.5726, 'longitude': 88.3639},
            {'name': 'Diana Evans', 'email': 'diana@example.com', 'username': 'diana', 'password': 'password123', 'state': 'Delhi', 'city': 'New Delhi', 'place': 'Connaught Place', 'latitude': 28.6315, 'longitude': 77.2167},
            {'name': 'Eve Foster', 'email': 'eve@example.com', 'username': 'eve', 'password': 'password123', 'state': 'Gujarat', 'city': 'Ahmedabad', 'place': 'Navrangpura', 'latitude': 23.0225, 'longitude': 72.5714}
        ]
        customerUser.objects.all().delete()
        for customer in customers:
            state = State.objects.get(name=customer['state'])
            city = City.objects.get(name=customer['city'])
            place = Place.objects.get(name=customer['place'])
            customerUser.objects.create(
                name=customer['name'],
                email=customer['email'],
                username=customer['username'],
                password=customer['password'],
                is_user=True,
                state=state,
                city=city,
                place=place,
                latitude=customer['latitude'],
                longitude=customer['longitude']
            )
        print("Customers created")

    def create_feedbacks(self):
        feedbacks = [
            {'stars': 5, 'comments': 'Excellent service!'},
            {'stars': 4, 'comments': 'Very good experience.'},
            {'stars': 3, 'comments': 'Average service, could be better.'},
            {'stars': 2, 'comments': 'Not satisfied with the service.'},
            {'stars': 1, 'comments': 'Very poor service, not recommended.'},
            {'stars': 5, 'comments': 'Outstanding experience, highly recommended!'},
            {'stars': 4, 'comments': 'Good service, but room for improvement.'}
        ]
        Feedback.objects.all().delete()
        for feedback in feedbacks:
            Feedback.objects.create(stars=feedback['stars'], comments=feedback['comments'])
        print("Feedbacks created")

    def create_contacts(self):
        contacts = [
            {'name': 'Alice', 'email': 'alice@example.com', 'subject': 'Inquiry about services'},
            {'name': 'Bob', 'email': 'bob@example.com', 'subject': 'Feedback on recent order'},
            {'name': 'Charlie', 'email': 'charlie@example.com', 'subject': 'Complaint about delivery'},
            {'name': 'Diana', 'email': 'diana@example.com', 'subject': 'Suggestion for new menu items'},
            {'name': 'Eve', 'email': 'eve@example.com', 'subject': 'Request for refund'},
            {'name': 'Frank', 'email': 'frank@example.com', 'subject': 'Inquiry about bulk orders'},
            {'name': 'Grace', 'email': 'grace@example.com', 'subject': 'Feedback on customer service'}
        ]
        Contact.objects.all().delete()
        for contact in contacts:
            Contact.objects.create(name=contact['name'], email=contact['email'], subject=contact['subject'])
        print("Contacts created")

    def create_orders(self):
        customers = customerUser.objects.all()
        orders = [
            {'customer': random.choice(customers), 'item': 'Pizza', 'quantity': 2, 'category': 'Food', 'sum_of_price': 500.00, 'order_no': 'ORD001', 'status': 'PENDING', 'delivery_person': 'Delivery Guy', 'delivery_contact': '1234567890', 'restaurant_name': 'Pizzeria', 'comments': 'Extra cheese', 'date_time': timezone.now()},
            {'customer': random.choice(customers), 'item': 'Burger', 'quantity': 1, 'category': 'Food', 'sum_of_price': 200.00, 'order_no': 'ORD002', 'status': 'CONFIRMED', 'delivery_person': 'Delivery Guy', 'delivery_contact': '1234567890', 'restaurant_name': 'Burger Joint', 'comments': 'No onions', 'date_time': timezone.now()}
        ]
        Order.objects.all().delete()
        for order in orders:
            Order.objects.create(**order)
        print("Orders created")