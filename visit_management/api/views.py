from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from core.models import Worker, Shop, Visit
from .serializers import VisitSerializer, ShopSerializer


class ShopListViews(APIView):
    def get(self, request, format=None):
        shops = request.user.shops
        if not shops:
            return Response({"message": "No shops found"}, status=404)

        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)


class VisitViews(APIView):
    def post(self, request, shop_id, format=None):
        worker = request.user
        get_object_or_404(Shop, id=shop_id, worker=worker)
        serializer = VisitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(worker=worker, shop_id=shop_id)

        return Response(serializer.data, status=201)
