from django.urls import path

from . import views

urlpatterns = [
    path('', views.PlanFormView.as_view(), name='index'),
    path('cidades/', views.CityListView.as_view(), name='city_list'),
    path('pesos/', views.PlanWithWeightsFormView.as_view(), name='index_peso'),
]
