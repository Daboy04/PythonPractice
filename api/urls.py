from django.urls import path 
from . import views

urlpatterns = [
    #view data
    path('',views.getData),

    #add report
    #path('add/',views.addReport),
    #delete report
    #path('delete/<int:pk>/', views.deleteReport, name='delete_report'),
]