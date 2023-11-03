from django.urls import path

from .views.token import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    CustomTokenBlacklistView,
)
from .views.user import (
    CurrentUserDetailView
)


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', CustomTokenVerifyView.as_view(), name='token-verify'),
    path('token/blacklist/', CustomTokenBlacklistView.as_view(),
         name='token-blacklist'),
    path('user/me/', CurrentUserDetailView.as_view(), name='user-me')
]
