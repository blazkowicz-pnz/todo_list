from django.urls import path

from todo_list.bot import views

urlpatterns = [
    path('verify', views.VerificationView.as_view(), name="verify-user"),
]