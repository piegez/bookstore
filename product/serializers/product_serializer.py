from rest_framework import serializers

from product.models import Category
from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )
    category = CategorySerializer(
        many=True, read_only=True
    )  # Certifique-se de que esse campo está presente

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "active",
            "category",  # Inclua esse campo se for necessário na resposta
            "categories_id",
        ]

    def create(self, validate_data):
        category_data = validate_data.pop("categories_id")
        product = Product.objects.create(**validate_data)
        product.category.set(
            category_data
        )  # Use set para garantir que as categorias estão associadas corretamente
        return product
