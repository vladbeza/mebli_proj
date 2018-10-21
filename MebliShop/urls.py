from django.urls import path

from . import views

app_name = 'MebliShop'
urlpatterns = [
    path('', views.index, name='main'),
    path('sub_cat/<int:sub_cat_id>/', views.sub_category_view, name='sub_category_view'),
    path('product/<int:product_id>/', views.product_view, name='product_view'),
    path('product/thanks/<int:product_id>/', views.thanks_view, name='thanks_view'),
    path('address/', views.map_view, name='address'),
    path('get_discount/', views.cheaper_view, name='get_discount'),
]
