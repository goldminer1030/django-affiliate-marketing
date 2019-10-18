from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm


# Create your views here.
class SignupView(CreateView):
    template_name = 'profiles/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('profiles:auth_login')

