from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AccommodationViewSet, CustomTextViewSet, HomePageViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
    AppReportView,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("accommodation", AccommodationViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("report", AppReportView.as_view(), name="app_report"),
]
