from django.urls import path
from . import views


urlpatterns = [
    path('', views.Courses, name='Home-Page'),
    path('<int:course_id>', views.Details, name='Details-Page'),
]
