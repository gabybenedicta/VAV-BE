import firebase_admin
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import InvoiceSerializer
from .models import Invoice

# Initialize Firebase SDK
default_app = firebase_admin.initialize_app()

# Create your views here.
def index(request):
  return HttpResponse("Hello, world. Welcome to the Mock Platform")

@api_view(['POST'])
def create_invoice(request):
	if request.method == 'POST':
		serializer = InvoiceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_invoice(request, pk):
	try:
		invoice = Invoice.objects.get(pk=pk)
	except Invoice.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		serializer = InvoiceSerializer(invoice)
		return Response(serializer.data, status = status.HTTP_200_OK)
	return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def make_payment(request, pk):
	if request.method == 'POST':
		try:
			invoice = Invoice.objects.get(pk=pk)
		except Invoice.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		
		#change status to IN PROCESS
		new_invoice = invoice
		new_invoice.transaction_status = "I"
		serializer = InvoiceSerializer(invoice, data=new_invoice)

		#make payment call to THS and update status according to THS