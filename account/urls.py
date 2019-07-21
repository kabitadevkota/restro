from django.urls import path
from django.contrib.auth import views
from account import views as account_view

urlpatterns = [
   
  path('login/', views.LoginView.as_view(template_name="account/login.html"), name='login'),
  path('logout/', views.LogoutView.as_view(template_name="account/logout.html"), name='logout'),
 path('signup/', account_view.UserSignUpView.as_view(), name='signup'),
]