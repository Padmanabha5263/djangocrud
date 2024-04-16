from rest_framework import serializers
from crud.models import Customers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        # fields='__all__'
        fields=['id',"name","age","phone"]
        