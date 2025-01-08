# forms.py



from django import forms
from customer.models import City, Place , State
from restaurant.models import restaurantUser, foodItems
# forms.py

class SearchForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False, empty_label="Select a City")
    query = forms.CharField(max_length=100, required=False, label="Search for Restaurants or Food Items")

