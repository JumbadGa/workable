from django.urls import path
from . import views

urlpatterns = [
    path('resumes', views.display_resumes, name='display-resumes'),
    path('resume/new', views.ResumeCreateView.as_view(), name='create-resume')
]
