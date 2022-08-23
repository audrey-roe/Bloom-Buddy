from rest_framework import serializers

from .models import membership


class membershipSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)

    class Meta:
        model = membership
        fields = ["name", "price"]