from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignupView
from .forms import LoginForm

app_name = 'profiles'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html', authentication_form=LoginForm),
         name='auth_login'),
    path('logout/', auth_views.logout_then_login, name='auth_logout'),
]
