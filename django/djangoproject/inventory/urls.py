from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.index, name="index"),
    path('orders/<uuid:id>', views.index2, name="index2"),
]