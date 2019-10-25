from django.urls import path
from .views import DashboardView, OffersView, AffiliatesView, PaymentsView, SupportView, \
    UserDetailView, StatusView, SmartLinksView, EarningsCreateView, EarningsUpdateView, EarningsDeleteView, \
    PaymentsCreateView, PaymentsUpdateView, PaymentsDeleteView, \
    OffersCreateView, OffersUpdateView, OffersDeleteView, \
    SupportManagerView, SupportManagerCreateView, SupportManagerUpdateView, SupportManagerDeleteView, \
    BalanceUpdateView, UserCreateView, UserUpdateView, UserDeleteView


app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('affiliates/', AffiliatesView.as_view(), name='affiliates'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/create/', UserCreateView.as_view(), name='create-user'),
    path('user/update/<int:pk>', UserUpdateView.as_view(), name='update-user'),
    path('user/delete/<int:pk>', UserDeleteView.as_view(), name='delete-user'),

    path('offers/', OffersView.as_view(), name='offers'),
    path('offers/create/', OffersCreateView.as_view(), name='create-offers'),
    path('offers/update/<int:pk>', OffersUpdateView.as_view(), name='update-offers'),
    path('offers/delete/<int:pk>', OffersDeleteView.as_view(), name='delete-offers'),

    path('earning/create/<slug:slug>', EarningsCreateView.as_view(), name='create-earning'),
    path('earning/update/<int:pk>-<slug:slug>', EarningsUpdateView.as_view(), name='update-earning'),
    path('earning/delete/<int:pk>-<slug:slug>', EarningsDeleteView.as_view(), name='delete-earning'),

    path('payment/create/<slug:slug>', PaymentsCreateView.as_view(), name='create-payment'),
    path('payment/update/<int:pk>-<slug:slug>', PaymentsUpdateView.as_view(), name='update-payment'),
    path('payment/delete/<int:pk>-<slug:slug>', PaymentsDeleteView.as_view(), name='delete-payment'),

    path('balance/update/<int:pk>-<slug:slug>', BalanceUpdateView.as_view(), name='update-balance'),

    path('status/', StatusView.as_view(), name='status'),
    path('smart-links/', SmartLinksView.as_view(), name='smart-links'),
    path('payments/', PaymentsView.as_view(), name='payments'),

    path('support/', SupportView.as_view(), name='support'),
    path('support-manager/', SupportManagerView.as_view(), name='support-manager'),
    path('support-manager/create/', SupportManagerCreateView.as_view(), name='create-support-manager'),
    path('support-manager/update/<int:pk>', SupportManagerUpdateView.as_view(), name='update-support-manager'),
    path('support-manager/delete/<int:pk>', SupportManagerDeleteView.as_view(), name='delete-support-manager'),
]
