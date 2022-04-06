from django.urls import path

from .views import HomePageView

app_name = 'page'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]