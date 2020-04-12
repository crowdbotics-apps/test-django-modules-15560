from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    CreateUserView,
    SignupViewSet,
    LoginViewSet,
    # HomePageViewSet,
    # CustomTextViewSet,
    AppReportView
)

router = DefaultRouter()
router.register('login', LoginViewSet, basename='login')
# router.register('customtext', CustomTextViewSet)
# router.register('homepage', HomePageViewSet)

urlpatterns = [
    path('', include('djoser.urls')),

    path("", include(router.urls)),
    path('signup', CreateUserView.as_view(), name='signup'),

    path("report", AppReportView.as_view(), name="app_report"),
]
