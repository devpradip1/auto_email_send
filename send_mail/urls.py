from django.urls import path
from . import views

urlpatterns = [

    path('',views.employeemail.as_view(),name='employeemail')
]