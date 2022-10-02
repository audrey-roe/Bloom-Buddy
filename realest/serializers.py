from rest_framework import serializers
from .models import realEstate_offer, realEstate_Purpose

class realEstate_offerSerializer(serializers.ModelSerializer):

    class Meta:
        model = realEstate_offer
        fields = ('__all__')

class realEstate_purposeSerializer(serializers.ModelSerializer):

    class Meta:
        model = realEstate_Purpose
        fields = ('__all__')

