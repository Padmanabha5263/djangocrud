from django.shortcuts import render
from crud.serializers import CustomerSerializer
from crud.models import Customers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class CustomerView(APIView):
    def get(self,request, id=None):
        if(id is not None):
            try:
                customer = Customers.objects.get(id=id)
                serializeddata = CustomerSerializer(customer)
                return Response(serializeddata.data, status=200)
            except Customers.DoesNotExist:
                return Response({"message":"Customer not exist!!"}, status=404)
        customersQset = Customers.objects.all()
        serializeddata = CustomerSerializer(customersQset, many=True)
        return Response(serializeddata.data, status=200)
    
    def post(self, request):
        serializeddata=CustomerSerializer(data=request.data)
        if(serializeddata.is_valid()):
            serializeddata.save()
            return Response(serializeddata.data, status=201)
        return Response(serializeddata.errors, status=404)
    
    def put(self,request, id=None):
        try:
            customer = Customers.objects.get(id=id)
        except Customers.DoesNotExist:
            return Response(status=404)
        serializerdata= CustomerSerializer(customer,data=request.data)
        if(serializerdata.is_valid()):
            serializerdata.save()
            return Response(serializerdata.data, status=200)
        return Response(serializerdata.errors, status=404)
            
    def delete(self,request, id=None):
        try:
            customer = Customers.objects.get(id=id)
        except Customers.DoesNotExist:
            return Response(status=404)
        customer.delete()
        return Response({"message":"Customer deleted successfully!!"}, status=200)