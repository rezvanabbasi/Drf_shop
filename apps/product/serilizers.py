from rest_framework import serializers

from apps.product.models import Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

    def create(self, validated_data, *args, **kwargs):
        title = validated_data['title']
        type = validated_data['type']
        description = validated_data['description']

        cat = ProductCategory(
            title=title,
            type=type,
            description=description
        )
        cat.save()
        return cat


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        category_title = validated_data['category']
        category = ProductCategory.objects.get(
            title__exact=category_title
        )

        product = Product.objects.create(**validated_data)

        product.category = category
        product.save()

        return product
