from rest_framework import serializers
from .models import (Product, Category, User, Curt, Order)

"""User"""


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        user.curt_set.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


"""Category"""


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


"""Product"""


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'


"""Order"""


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id','product', 'total', 'total_price']


class AddOrderOnCurt(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'total']

    def create(self, validated_data):
        curt_id = self.context['curt_id']
        curt = Curt.objects.get(id=curt_id)
        order = Order.objects.create(cart=curt, **validated_data)
        return order


"""Curt"""


class CurtSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Curt
        fields = ['id', 'user', 'total_sum', 'orders']
