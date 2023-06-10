from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.CustomUserCreateView.as_view(), name='signup'),
    path('login/', views.CustomAuthToken.as_view(), name='login'),
]
