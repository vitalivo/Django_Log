from django.urls import path
from . import views

urlpatterns = [
    path('test-error/', views.test_error, name='test_error'),
]
