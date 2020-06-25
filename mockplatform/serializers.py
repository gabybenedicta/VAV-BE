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
		print("CREATING...")
		return Invoice.objects.create(**validated_data)
	def update(self, instance, validated_data):
			print("UPDATING...")
			# instance.seller_id = validated_data.get('seller_id', instance.seller_id)
			# instance.buyer_id = validated_data.get('buyer_id', instance.buyer_id)
			# instance.amount = validated_data.get('amount', instance.amount)
			# instance.transaction_status = validated_data.get('transaction_status', instance.transaction_status)
			# instance.currency = validated_data.get('currency', instance.currency)
			# instance.transaction_id = validated_data.get('transaction_id', instance.transaction_id)
			# instance.save()
			updated = Invoice.objects.get(id = validated_data["id"]).update(**validated_data)
			updated.save()
			return updated

class CardSerializer(serializers.Serializer):
	uid = serializers.CharField(max_length=100)
	public_key = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return CardHolderDetails.objects.create(**validated_data)
