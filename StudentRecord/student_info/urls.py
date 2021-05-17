from django.urls import path
from .views import student, details

urlpatterns = [
    path('student/', student, name="student_info"),
    path('detail/<int:pk>/', details)

]
