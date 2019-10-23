from django.views.generic.edit import CreateView, FormMixin, FormView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from common.mixins import LoginRequiredMixin
from .models import SmartLinks, Earnings, Payments
from .forms import SmartLinksForm, EarningsForm, PaymentsForm
from profiles.models import User
from profiles.forms import SignUpForm


class DashboardView(LoginRequiredMixin, ListView):
    success_url = '/dashboard/'
    template_name = 'dashboard/overview.html'
    model = User
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.exclude(email=self.request.user.email)


class UserDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/user-detail.html'

    def get(self, request, *args, **kwargs):
        customer = User.objects.get(pk=self.kwargs.get('pk'))

        context = self.get_context_data(**kwargs)
        context['user'] = customer
        context['earnings'] = Earnings.objects.filter(customer=customer)
        context['payments'] = Payments.objects.filter(customer=customer)
        context['smart_links'] = SmartLinks.objects.filter(customer=customer)
        context['earnings_form'] = EarningsForm(self.request.GET or None)
        context['payments_form'] = PaymentsForm(self.request.GET or None)

        return self.render_to_response(context)


class NewEarningView(FormView):
    form_class = EarningsForm
    template_name = 'dashboard/user-detail.html'

    def post(self, request, *args, **kwargs):
        earnings_form = self.form_class(request.POST)
        if earnings_form.is_valid():
            earnings_form.save()
            messages.success(self.request, 'Added a new earning successfully.')
        else:
            messages.error(self.request, earnings_form.errors)

        return redirect(reverse_lazy('dashboard:user-detail', kwargs={'pk': request.POST.get('customer')}))


class NewPaymentView(FormView):
    form_class = PaymentsForm
    template_name = 'dashboard/user-detail.html'

    def post(self, request, *args, **kwargs):
        payment_form = self.form_class(request.POST)
        if payment_form.is_valid():
            payment_form.save()
            messages.success(self.request, 'Added a new payment successfully.')
        else:
            messages.error(self.request, payment_form.errors)

        return redirect(reverse_lazy('dashboard:user-detail', kwargs={'pk': request.POST.get('customer')}))


class OffersView(LoginRequiredMixin, FormMixin, ListView):
    success_url = '/dashboard/offers/'
    template_name = 'dashboard/offers.html'
    model = SmartLinks
    context_object_name = 'smart_links'
    paginate_by = 10

    # form mixin
    form_class = SmartLinksForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        try:
            form.save()
            messages.success(self.request, 'Added a new smart link successfully.')
        except Exception as e:
            messages.error(self.request, 'Unfortunately failed')
        return super(OffersView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(OffersView, self).form_valid(form)


def delete_smart_link(request, pk):
    smart_link = SmartLinks.objects.get(id=pk)
    smart_link.delete()
    messages.success(request, 'Removed a smart link successfully.')
    return redirect("dashboard:offers")


def earning_link(request, pk, slug):
    earning = Earnings.objects.get(id=pk)
    earning.delete()
    messages.success(request, 'Removed an earning successfully.')
    return redirect(reverse_lazy('dashboard:user-detail', kwargs={'pk': slug}))


def payment_link(request, pk, slug):
    payment = Payments.objects.get(id=pk)
    payment.delete()
    messages.success(request, 'Removed a payment successfully.')
    return redirect(reverse_lazy('dashboard:user-detail', kwargs={'pk': slug}))


class AffiliatesView(LoginRequiredMixin, FormMixin, ListView):
    success_url = '/dashboard/affiliates/'
    template_name = 'dashboard/affiliates.html'
    model = User
    context_object_name = 'users'
    paginate_by = 10

    # form mixin
    form_class = SignUpForm

    def get_queryset(self):
        return User.objects.exclude(email=self.request.user.email)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        try:
            form.save()
            messages.success(self.request, 'Added a new user successfully.')
        except Exception as e:
            messages.error(self.request, 'Unfortunately failed')
        return super(AffiliatesView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(AffiliatesView, self).form_valid(form)


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
