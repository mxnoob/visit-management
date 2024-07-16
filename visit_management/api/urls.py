from django.urls import path

from . import views


urlpatterns = [
    path("shops/", views.ShopListViews.as_view(), name="shops"),
    path("visit/<int:shop_id>/", views.VisitViews.as_view(), name="visit"),
]
