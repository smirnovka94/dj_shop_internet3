from django.urls import path

from main.apps import MainConfig
from main.views import home, contacts, ProductListView, ProductDetailView, ProductCreatelView, ProductUpdatelView, \
    ProductDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product/create/', ProductCreatelView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdatelView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]

