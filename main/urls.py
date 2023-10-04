from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import home, contacts, ProductListView, ProductDetailView, ProductCreatelView, ProductUpdatelView, \
    ProductDeleteView, CategoryListView

app_name = MainConfig.name

urlpatterns = [
    path('', cache_page(60)(ProductListView.as_view()), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('product/create/', ProductCreatelView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdatelView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]

