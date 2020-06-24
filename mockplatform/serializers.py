from rest_framework import serializers
from .models import Invoice, CardHolderDetails

class InvoiceSerializer(serializers.Serializer):
	seller_id = serializers.IntegerField()
	buyer_id = serializers.IntegerField()
	amount = serializers.FloatField()
	description = serializers.CharField(max_length=150, default=None)

	def create(self, validated_data):
		return Invoice.objects.create(**validated_data)

class CardSerializer(serializers.Serializer):
	uid = serializers.CharField(max_length=100)
	public_key = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return CardHolderDetails.objects.create(**validated_data)