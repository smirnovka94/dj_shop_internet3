from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserVerificationView, UserResetView,  UserReset_password_sent,UserResetView, UserUpdateView, send_new_password, resert


app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verification/', UserVerificationView.as_view(), name='verification'),
    # path('resert/', UserResetView.as_view(), name='resert'),
    path('resert_password_sent/', UserReset_password_sent.as_view(), name='resert_password_sent'),
    # path('resert/', UserUpdateView.as_view(), name='resert'),
    path('resert/', resert, name='resert'),
    path('send_new_password/', send_new_password, name='send_new_password'),
]

