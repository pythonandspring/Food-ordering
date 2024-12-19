from rest_framework import serializers
from customer.models import customerUser,Feedback,Contact

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customerUser
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


