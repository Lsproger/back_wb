from django.contrib.auth.models import User, Group
from rest_framework import serializers
from back_wb.wb_api.models import Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class ProductSerializer(serializers.ModelField):
#     class Meta:
#         model = Product
#         fields = ['id', 'title', 'category', 'price', 'discount', "count"]
    
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField(required=False, allow_blank=True, max_length=100)
    title = serializers.CharField(required=False, allow_blank=True, max_length=500)
    price = serializers.FloatField(required=False)
    discount = serializers.IntegerField(required=False)
    count = serializers.IntegerField(required=False)
    image_url = serializers.URLField(required=False, allow_blank=True, max_length=500,)


    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.category = validated_data.get('category', instance.category)
        instance.price = validated_data.get('price', instance.price)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.count = validated_data.get('count', instance.count)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.save()
        return instance