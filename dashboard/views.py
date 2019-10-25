from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from common.mixins import LoginRequiredMixin
from .models import SmartLinks, Earnings, Payments, SupportManager, Balance
from .forms import SmartLinksForm, EarningsForm, PaymentsForm, SupportManagerForm, BalanceForm, UserForm
from profiles.models import User


class DashboardView(LoginRequiredMixin, ListView):
    success_url = '/dashboard/'
    template_name = 'dashboard/overview.html'
    model = User
    context_object_name = 'users'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect("dashboard:status")
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return User.objects.exclude(email=self.request.user.email)


class UserDetailView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/user-detail.html'
    model = Earnings
    context_object_name = 'earnings'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)

        customer = User.objects.get(pk=self.kwargs.get('pk'))
        context['customer'] = customer
        context['payments'] = Payments.objects.filter(customer=customer)
        context['smart_links'] = SmartLinks.objects.filter(customer=customer)
        return context

    def get_queryset(self):
        customer = User.objects.get(pk=self.kwargs.get('pk'))
        return Earnings.objects.filter(customer=customer)


class OffersView(LoginRequiredMixin, ListView):
    success_url = '/dashboard/offers/'
    template_name = 'dashboard/offers.html'
    model = SmartLinks
    context_object_name = 'smart_links'
    paginate_by = 10


class AffiliatesView(LoginRequiredMixin, ListView):
    success_url = '/dashboard/affiliates/'
    template_name = 'dashboard/affiliates.html'
    model = User
    context_object_name = 'users'


class StatusView(LoginRequiredMixin, ListView):
    success_url = '/dashboard/status/'
    template_name = 'dashboard/status.html'
    model = Earnings
    context_object_name = 'earnings'
    paginate_by = 30

    def get_queryset(self):
        return Earnings.objects.filter(customer=self.request.user)


class SmartLinksView(LoginRequiredMixin, ListView):
    success_url = '/dashboard/smart-links/'
    template_name = 'dashboard/smart-links.html'
    model = SmartLinks
    context_object_name = 'smart_links'
    paginate_by = 30

    def get_queryset(self):
        return SmartLinks.objects.filter(customer=self.request.user)


class PaymentsView(LoginRequiredMixin, ListView):
    success_url = '/dashboard/payments/'
    template_name = 'dashboard/payments.html'
    model = Payments
    context_object_name = 'payments'
    paginate_by = 30

    def get_queryset(self):
        return Payments.objects.filter(customer=self.request.user)


class SupportView(LoginRequiredMixin, ListView):
    success_url = '/dashboard/support/'
    template_name = 'dashboard/support.html'
    model = SupportManager
    context_object_name = 'supports'


class EarningsCreateView(BSModalCreateView):
    template_name = 'dashboard/include/create-modal.html'
    form_class = EarningsForm
    success_message = 'New earning has been created successfully'

    def get_success_url(self):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            slug = 0
        return reverse_lazy('dashboard:user-detail', kwargs={'pk': slug})


class EarningsUpdateView(BSModalUpdateView):
    model = Earnings
    template_name = 'dashboard/include/update-modal.html'
    form_class = EarningsForm
    success_message = 'An earning has been updated successfully'

    def get_success_url(self):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            slug = 0
        return reverse_lazy('dashboard:user-detail', kwargs={'pk': slug})


class EarningsDeleteView(BSModalDeleteView):
    model = Earnings
    template_name = 'dashboard/include/delete-modal.html'
    success_message = 'An earning has been deleted successfully'

    def get_success_url(self):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            slug = 0
        return reverse_lazy('dashboard:user-detail', kwargs={'pk': slug})


class PaymentsCreateView(BSModalCreateView):
    template_name = 'dashboard/include/create-modal.html'
    form_class = PaymentsForm
    success_message = 'New payment has been created successfully'

    def get_success_url(self):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            slug = 0
        return reverse_lazy('dashboard:user-detail', kwargs={'pk': slug})


class PaymentsUpdateView(BSModalUpdateView):
    model = Payments
    template_name = 'dashboard/include/update-modal.html'
    form_class = PaymentsForm
    success_message = 'A payment has been updated successfully'

    def get_success_url(self):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            slug = 0
        return reverse_lazy('dashboard:user-detail', kwargs={'pk': slug})


class PaymentsDeleteView(BSModalDeleteView):
    model = Payments
    template_name = 'dashboard/include/delete-modal.html'
    success_message = 'A payment has been deleted successfully'

    def get_success_url(self):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            slug = 0
        return reverse_lazy('dashboard:user-detail', kwargs={'pk': slug})


class UserCreateView(BSModalCreateView):
    template_name = 'dashboard/include/create-modal.html'
    form_class = UserForm
    success_message = 'New user has been created successfully'
    success_url = reverse_lazy('dashboard:affiliates')


class UserUpdateView(BSModalUpdateView):
    model = User
    template_name = 'dashboard/include/update-modal.html'
    form_class = UserForm
    success_message = 'An user has been updated successfully'
    success_url = reverse_lazy('dashboard:affiliates')


class UserDeleteView(BSModalDeleteView):
    model = User
    template_name = 'dashboard/include/delete-modal.html'
    success_message = 'An user has been deleted successfully'
    success_url = reverse_lazy('dashboard:affiliates')


class OffersCreateView(BSModalCreateView):
    template_name = 'dashboard/include/create-modal.html'
    form_class = SmartLinksForm
    success_message = 'New smart link has been created successfully'
    success_url = reverse_lazy('dashboard:offers')


class OffersUpdateView(BSModalUpdateView):
    model = SmartLinks
    template_name = 'dashboard/include/update-modal.html'
    form_class = SmartLinksForm
    success_message = 'A smart link has been updated successfully'
    success_url = reverse_lazy('dashboard:offers')


class OffersDeleteView(BSModalDeleteView):
    model = SmartLinks
    template_name = 'dashboard/include/delete-modal.html'
    success_message = 'A smart link has been deleted successfully'
    success_url = reverse_lazy('dashboard:offers')


class SupportManagerView(LoginRequiredMixin, ListView):
    success_url = '/dashboard/support-manager/'
    template_name = 'dashboard/support-manager.html'
    model = SupportManager
    context_object_name = 'supports'


class SupportManagerCreateView(BSModalCreateView):
    template_name = 'dashboard/include/create-modal.html'
    form_class = SupportManagerForm
    success_message = 'New support manager has been created successfully'
    success_url = reverse_lazy('dashboard:support-manager')


class SupportManagerUpdateView(BSModalUpdateView):
    model = SupportManager
    template_name = 'dashboard/include/update-modal.html'
    form_class = SupportManagerForm
    success_message = 'A support manager has been updated successfully'
    success_url = reverse_lazy('dashboard:support-manager')


class SupportManagerDeleteView(BSModalDeleteView):
    model = SupportManager
    template_name = 'dashboard/include/delete-modal.html'
    success_message = 'A smart link has been deleted successfully'
    success_url = reverse_lazy('dashboard:support-manager')


class BalanceUpdateView(BSModalUpdateView):
    model = Balance
    template_name = 'dashboard/include/update-modal.html'
    form_class = BalanceForm
    success_message = 'Balance has been updated successfully'
    success_url = reverse_lazy('dashboard:support-manager')

    def get_success_url(self):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        else:
            slug = 0
        return reverse_lazy('dashboard:user-detail', kwargs={'pk': slug})
