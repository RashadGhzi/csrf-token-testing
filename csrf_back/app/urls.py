from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView, name='product_add'),
    path('csrf/', views.csrf_cookie, name='csrf_cookie'),
]
