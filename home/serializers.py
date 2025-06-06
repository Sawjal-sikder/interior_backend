from rest_framework import serializers
from .models import *


class BanarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banar
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class LatestProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestProject
        fields = '__all__'


class ChooseusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chooseus
        fields = '__all__'


class GallarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallary
        fields = '__all__'
