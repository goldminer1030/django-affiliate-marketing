from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .forms import SignUpForm
from .models import User


# Create your views here.
class SignupView(CreateView):
    template_name = 'profiles/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('profiles:auth_login')


def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    messages.success(request, 'An user has been deleted successfully.')
    return redirect("dashboard:affiliates")

