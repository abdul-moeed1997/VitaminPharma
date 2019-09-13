from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('products/', views.products, name='products'),
    path('product/<int:myid>', views.product_details, name='product-details'),
    path('about/', views.about, name='AboutUs'),
    path('search/', views.search, name='Search'),
    path('cart/', views.cart, name='Cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='tracker'),
    path('checkout/', views.checkout, name='checkout'),
    path('brand/', views.brand, name='brand'),
    path('category/', views.category, name='category')
]