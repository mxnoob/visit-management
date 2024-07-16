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
        extra_kwargs = {
            "date": {"required": False, "allow_null": True},
            "latitude": {
                "required": True,
                "allow_null": False,
                "write_only": True,
            },
            "longitude": {
                "required": True,
                "allow_null": False,
                "write_only": True,
            },
        }
        read_only_fields = ("id", "date")
