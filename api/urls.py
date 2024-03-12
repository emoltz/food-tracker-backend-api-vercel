from django.urls import path, include

from api.views import HomePageView

urlpatterns = [
    path('hello/', HomePageView.as_view(), name='hello'),
]