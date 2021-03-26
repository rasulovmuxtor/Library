from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user import views

app_name = 'user'

urlpatterns = [
    path("",views.UsersApiRoot.as_view(),name="root-endpoints"),
    path('token-auth/', obtain_auth_token, name='token_auth'),
    path('change-password/',views.ChangePasswordView.as_view(),name='change-password')
]


