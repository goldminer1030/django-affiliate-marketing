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
        return User.objects.all()


class OffersView(LoginRequiredMixin, CreateView):
    success_url = '/dashboard/offers/'
    template_name = 'dashboard/offers.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(OffersView, self).get_context_data(**kwargs)
        return context


class AffiliatesView(LoginRequiredMixin, CreateView):
    success_url = '/dashboard/affiliates/'
    template_name = 'dashboard/affiliates.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(AffiliatesView, self).get_context_data(**kwargs)
        return context


class FinancesView(LoginRequiredMixin, CreateView):
    success_url = '/dashboard/finances/'
    template_name = 'dashboard/finances.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(FinancesView, self).get_context_data(**kwargs)
        return context


class MailRoomView(LoginRequiredMixin, CreateView):
    success_url = '/dashboard/mail-room/'
    template_name = 'dashboard/mail-room.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(MailRoomView, self).get_context_data(**kwargs)
        return context


class ToolsView(LoginRequiredMixin, CreateView):
    success_url = '/dashboard/tools/'
    template_name = 'dashboard/tools.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(ToolsView, self).get_context_data(**kwargs)
        return context


class AdministrationView(LoginRequiredMixin, CreateView):
    success_url = '/dashboard/administration/'
    template_name = 'dashboard/administration.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(AdministrationView, self).get_context_data(**kwargs)
        return context
