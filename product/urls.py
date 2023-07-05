from django.urls import path
from . import views

urlpatterns = [
    path('',views.product,name="products"),
    path('delete/<int:id>/',views.delete_product,name="delete_product"),
    path('update/<int:id>/',views.update_product,name="update_product"),
]