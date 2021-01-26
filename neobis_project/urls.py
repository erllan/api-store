from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('api/user/token/', jwt_views.TokenObtainPairView.as_view()),
    path('api/user/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('api/product/', views.ListCreateProduct.as_view()),
    path('api/curt/', views.CurtUser.as_view()),
    path('api/user/register/', views.RegisterUser.as_view()),
    path('api/category/', views.LisCreateCategory.as_view()),
    path('api/order/', views.OrderAddToCurt.as_view())

]