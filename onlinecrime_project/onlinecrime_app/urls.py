from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import report_complaint
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('complaints/', views.all_complaints, name='all_complaints'),
    path('complaints/<int:complaint_id>/', views.complaints_detail, name='complaints_detail'),
    path('complaints/new/', views.new_complaint, name='new_complaint'),
    path('report_complaint/', views.report_complaint, name='report_complaint'),

]
