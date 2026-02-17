from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, PatientViewSet, DoctorViewSet, MappingViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'doctors', DoctorViewSet)
router.register(r'mappings', MappingViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('', include(router.urls)),
]
