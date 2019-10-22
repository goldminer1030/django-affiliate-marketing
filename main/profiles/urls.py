from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from .views import SignupView, delete_user
from .forms import LoginForm

app_name = 'profiles'

urlpatterns = [
    path('', TemplateView.as_view(template_name='profiles/home.html'), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html', authentication_form=LoginForm),
         name='auth_login'),
    path('logout/', auth_views.logout_then_login, name='auth_logout'),
    path('user/<int:pk>/delete', delete_user, name='user-delete')
]
