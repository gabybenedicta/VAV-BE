import firebase_admin
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests

from .serializers import InvoiceSerializer, CardSerializer
from .models import Invoice, CardHolderDetails

# Initialize Firebase SDK
default_app = firebase_admin.initialize_app()

# Create your views here.
def index(request):
  return HttpResponse("Hello, world. Welcome to the Mock Platform")

@api_view(['POST'])
def create_invoice(request):
	if request.method == 'POST':
		try:
			seller = CardHolderDetails.objects.get(uid = request.data["seller_id"])
		except CardHolderDetails.DoesNotExist:
			message={"content": "Seller does not exist"}
			return Response(message, status=status.HTTP_404_NOT_FOUND)
		
		try: 
			buyer = CardHolderDetails.objects.get(uid = request.data["buyer_id"])
		except CardHolderDetails.DoesNotExist:
			message={"content": "Buyer does not exist"}
			return Response(message, status=status.HTTP_404_NOT_FOUND)

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
		invoice.transaction_status = "I"
		invoice.save()
		#make payment call to THS and update status according to THS
		try: 
			buyer = CardHolderDetails.objects.get(uid = invoice.buyer_id)
		except CardHolderDetails.DoesNotExist:
			message={"content": "Buyer does not exist"}
			return Response(message, status=status.HTTP_404_NOT_FOUND)
		try:
			seller = CardHolderDetails.objects.get(uid = invoice.seller_id)
		except CardHolderDetails.DoesNotExist:
			message={"content": "Seller does not exist"}
			return Response(message, status=status.HTTP_404_NOT_FOUND)
		transactionObj = {
			"sender_key": buyer.public_key,
			"recipient_key": seller.public_key,
			"amount": invoice.amount,
			"currency": invoice.currency
		}

		response = requests.post("https://e-context-279708.df.r.appspot.com/transaction", data = transactionObj)
		json_data = response.json()

		if response.status_code == 200:
			invoice.transaction_status = "S"
			invoice.transaction_id = json_data['transactionIdentifier']
			invoice.save()
			
			message = {"content": "Transaction successful!", "transaction_id": invoice.transaction_id }
			return Response(message, status = status.HTTP_200_OK)
		else:
			invoice.transaction_status = "F"
			invoice.save()
			return Response(response.content, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def save_card(request):
	print(request)
	content =request.data
	email = content['email']
	card_number = content['card_number']
	full_name = content['full_name']
	expiry_date = content['expiry_date']
	ccv = content['ccv']
	uid = content['uid']

	cardObj = {
    "email": email,
    "card_number": card_number,
    "full_name": full_name,
    "expiry_date": expiry_date,
    "ccv": ccv
	}

	response = requests.post("https://e-context-279708.df.r.appspot.com/card", data=cardObj)
	if response.status_code == 201:
		json_data = response.json()
		cardholder_data = {
			"uid": uid,
			"public_key": json_data['public_key']
		}

		serializer = CardSerializer(data=cardholder_data)
		if serializer.is_valid():
			serializer.save()
		message = { "content": "Card saved successfully"}
		return Response(message, status = status.HTTP_201_CREATED)
	return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def view_card(request, uid):
	try:
		card = CardHolderDetails.objects.get(uid=uid)
	except CardHolderDetails.DoesNotExist:
		message = {"content": "Card does not exist in the database"}
		return Response(message, status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		public_key = card.public_key
		response = requests.get("https://e-context-279708.df.r.appspot.com/card/"+public_key)
		json_data= response.json()
		return Response(json_data, status = status.HTTP_200_OK)
	return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def del_card(request, uid):
	try:
		card_qs = CardHolderDetails.objects.get(uid=uid)
		public_key=card_qs.public_key
		card_qs.delete()
	except CardHolderDetails.DoesNotExist:
		message = {"content": "Card does not exist in the database"}
		return Response(message, status=status.HTTP_404_NOT_FOUND)	
		
	response = requests.delete("https://e-context-279708.df.r.appspot.com/card/"+public_key)
	message = {"content": "Deleted Successfully"}
	return Response(message, status = status.HTTP_200_OK)

