from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.user.api.v1.api import RegisterAPIView, EmailTokenObtainPairView, LoginApiView

app_name = "user"
urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('token/obtain/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]