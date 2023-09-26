from django.urls import path
from . import views
from .views import PasswordsChangeView
# from django.contrib.auth import views as auth_views


urlpatterns = [
  path('', views.login_user, name='login'),
  path('logout_user', views.logout_user, name='logout'),
  # path('settings/change-password/', auth_views.PasswordChangeView.as_view(template_name='authentication/change-password.html'), name='change-password'),
  path('settings/change-password/', PasswordsChangeView.as_view(template_name='authentication/change-password.html'), name='change-password')
]