from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.Modelserializer):
    class Meta:
        model = Customer:
        fields =  '__all__'


class OrderSerializer(serializer.Modelserializer):
    class meta:
        model = Order
        fields - '__all__'
