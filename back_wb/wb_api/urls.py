from django.urls import path
from back_wb.wb_api import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_details),
]