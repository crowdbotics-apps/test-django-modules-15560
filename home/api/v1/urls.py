from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    AccommodationViewSet,
    # CreateUserView,
    LoginViewSet,
    # HomePageViewSet,
    # CustomTextViewSet,
    AppReportView
)

router = DefaultRouter()
# router.register('login', LoginViewSet, basename='login')
# router.register('customtext', CustomTextViewSet)
# router.register('homepage', HomePageViewSet)
router.register("accommodation", AccommodationViewSet)


urlpatterns = [
    path("", include(router.urls)),
    # path('auth/signup', CreateUserView.as_view(), name='signup'),

    path("report", AppReportView.as_view(), name="app_report"),
]
