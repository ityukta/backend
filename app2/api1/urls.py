from django.urls import path, include
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('initialregister', views.InitialRegistrationView.as_view(), basename='InitialRegistration')

urlpatterns = [
    # path('', include(router.urls)),
    path('initialregister', views.InitialRegistrationView.as_view()),
    path('login', views.LoginView.as_view())
]
