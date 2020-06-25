from rest_framework import serializers
from .models import Invoice, CardHolderDetails

class InvoiceSerializer(serializers.Serializer):
	seller_id = serializers.CharField(max_length=100)
	buyer_id = serializers.CharField(max_length=100)
	amount = serializers.FloatField()
	description = serializers.CharField(max_length=150, default=None)
	transaction_status = serializers.CharField(
        default= "C",
        max_length = 1
  )
	currency = serializers.CharField(max_length=3, default= "SGD")
	transaction_id = serializers.CharField(max_length=150, default="")

	def create(self, validated_data):
		return Invoice.objects.create(**validated_data)

class CardSerializer(serializers.Serializer):
	uid = serializers.CharField(max_length=100)
	public_key = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return CardHolderDetails.objects.create(**validated_data)
