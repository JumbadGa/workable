from django.urls import path
from . import views

urlpatterns = [
    path('vacancies', views.VacanciesListView.as_view(), name='display-vacancies'),
    path('vacancy/new', views.VacancyCreateView.as_view(), name='create-vacancy')
]
