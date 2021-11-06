from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data: dict):
        product_category = validated_data.get('product_category', None)

        if product_category:
            product = Product.objects.create(**validated_data)
        elif validated_data.get('price') <= 100:
            product = Product.objects.create(code=validated_data.get('code'),
                                             name=validated_data.get('name'), description=validated_data.get('description'),
                                             price=validated_data.get('price'), stock=validated_data.get('stock'),
                                             unit=validated_data.get('unit'), product_category='B')
        elif validated_data.get('price') <= 500:
            product = Product.objects.create(code=validated_data.get('code'),
                                             name=validated_data.get('name'), description=validated_data.get('description'),
                                             price=validated_data.get('price'), stock=validated_data.get('stock'),
                                             unit=validated_data.get('unit'), product_category='M')
        elif validated_data.get('price') > 500:
            product = Product.objects.create(code=validated_data.get('code'),
                                             name=validated_data.get('name'), description=validated_data.get('description'),
                                             price=validated_data.get('price'), stock=validated_data.get('stock'),
                                             unit=validated_data.get('unit'), product_category='C')
        return product
