from django.urls import path

from . import views

app_name = 'new_candyshop'

urlpatterns = [
    path('', views.product_all, name='new_candyshop_home'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('new_candyshop/<slug:category_slug>/', views.category_list, name='category_list'),
]