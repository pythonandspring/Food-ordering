from django.urls import path
from .views import home, profile, RegisterView

urlpatterns = [
    path('', home, name='customer-home'),
    path('register/', RegisterView.as_view(), name='customer-register'),
    path('profile/', profile, name='customer-profile'),
]
