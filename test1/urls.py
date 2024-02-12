from django.urls import path
from . import views

urlpatterns = [
    path('data_list/',views.DataLists.as_view()),
    path('depart/',views.Department.as_view())
]