from django.contrib import admin
from django.urls import path
from favorite import views
from fitnes.views import *
from pro_version.views import *
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="FirBreak API",
        default_version='v3',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('api/v1/favorite-exercises/', views.FavoriteExerciseListCreateAPIView.as_view()),
    path('api/v1/favorite-exercises/<int:id>/', views.FavoriteExerciseListCreateAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('api/v1/eye/', EyeTrainingView.as_view()),
    path('api/v1/hand/', HandTrainingView.as_view()),
    path('api/v1/neck/', NeckTrainingView.as_view()),
    path('api/v1/leg/', LegTrainingView.as_view()),
    path('api/v1/back/', BackTrainingView.as_view()),
    path('api/v1/plusversion/', ProVersionView.as_view()),
    path('api/v1/start/', StartStopView.as_view()),

    path('accounts/', include('allauth.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/users/', include('register.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
