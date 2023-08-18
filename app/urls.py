from django.urls import path
from app import views
urlpatterns = [
    path('', views.home, name="home"),   
    path('products/', views.products_view, name="products") ,
    path('product/<str:pk>/', views.product_view, name="product") 
]
