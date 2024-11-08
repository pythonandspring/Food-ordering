from django.urls import path
from . import views

urlpatterns = [
    path('student_list', views.student_list, name='student_list'),
    path('studentr-detail/<int:student_id>/', views.student_detail, name='student_detail') 
]