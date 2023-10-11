from django.urls import path
from . import views
from .views import PasswordsChangeView
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('', views.login_user, name='login'),
  path('logout_user', views.logout_user, name='logout'),
  path('settings/change-password/', PasswordsChangeView.as_view(template_name='authentication/change-password.html'), name='change-password'),
  path('manage/', views.manage, name='manage'),
  path('manage/add-user/', views.add_user, name='add-user'),
  path('delete_user/<int:user_id>/', views.delete_user, name='delete-user'),
  path('audit/', views.audit_log, name='audit-log'),
]