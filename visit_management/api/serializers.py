from rest_framework import serializers

from core.models import Visit, Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ("id", "name")


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = (
            "id",
            "date",
            "latitude",
            "longitude",
        )
        write_only_fields = ("latitude", "longitude")
        read_only_fields = ("id", "date")
