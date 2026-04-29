from django.urls import path

from . import views

urlpatterns = [
    path('', views.PlanFormView.as_view(), name='index'),
]
