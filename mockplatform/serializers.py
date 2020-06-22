from rest_framework import serializers
from .models import Products, Invoice

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Products
		fields = ('name', 'date', 'description')

class InvoiceSerializer(serializers.Serializer):
	seller_id = serializers.IntegerField()
	buyer_id = serializers.IntegerField()
	amount = serializers.FloatField()
	description = serializers.CharField(max_length=150, default=None)

	def create(self, validated_data):
		return Invoice.objects.create(**validated_data)