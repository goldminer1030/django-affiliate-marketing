from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from common.mixins import LoginRequiredMixin
from profiles.models import User


class DashboardView(LoginRequiredMixin, ListView):
    success_url = '/dashboard/'
    template_name = 'dashboard/overview.html'
    model = User
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.exclude(email=self.request.user.email)


class OffersView(LoginRequiredMixin, CreateView):
    success_url = '/dashboard/offers/'
    template_name = 'dashboard/offers.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(OffersView, self).get_context_data(**kwargs)
        return context


class AffiliatesView(LoginRequiredMixin, ListView):
    success_url = '/dashboard/affiliates/'
    template_name = 'dashboard/affiliates.html'
    model = User
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        return User.objects.exclude(email=self.request.user.email)


class FinancesView(LoginRequiredMixin, CreateView):
    success_url = '/dashboard/finances/'
    template_name = 'dashboard/finances.html'


class MailRoomView(LoginRequiredMixin, CreateView):
    success_url = '/dashboard/mail-room/'
    template_name = 'dashboard/mail-room.html'


class ToolsView(LoginRequiredMixin, CreateView):
    success_url = '/dashboard/tools/'
    template_name = 'dashboard/tools.html'


class AdministrationView(LoginRequiredMixin, CreateView):
    success_url = '/dashboard/administration/'
    template_name = 'dashboard/administration.html'
