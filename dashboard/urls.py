from django.urls import path
from .views import DashboardView, OffersView, AffiliatesView, PaymentsView, SupportView, \
    UserDetailView, NewEarningView, NewPaymentView, \
    StatusView, SmartLinksView, EarningsCreateView, EarningsUpdateView, EarningsDeleteView, \
    PaymentsCreateView, PaymentsUpdateView, PaymentsDeleteView, \
    OffersCreateView, OffersUpdateView, OffersDeleteView


app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('affiliates/', AffiliatesView.as_view(), name='affiliates'),
    path('new-earning/', NewEarningView.as_view(), name='new-earning'),
    path('new-payment/', NewPaymentView.as_view(), name='new-payment'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('offers/', OffersView.as_view(), name='offers'),
    path('offers/create/', OffersCreateView.as_view(), name='create-offers'),
    path('offers/update/<int:pk>', OffersUpdateView.as_view(), name='update-offers'),
    path('offers/delete/<int:pk>', OffersDeleteView.as_view(), name='delete-offers'),

    path('earning/create/', EarningsCreateView.as_view(), name='create-earning'),
    path('earning/update/<int:pk>', EarningsUpdateView.as_view(), name='update-earning'),
    path('earning/delete/<int:pk>', EarningsDeleteView.as_view(), name='delete-earning'),

    path('payment/create/', PaymentsCreateView.as_view(), name='create-payment'),
    path('payment/update/<int:pk>', PaymentsUpdateView.as_view(), name='update-payment'),
    path('payment/delete/<int:pk>', PaymentsDeleteView.as_view(), name='delete-payment'),

    # path('payment/<int:pk>-<slug:slug>/delete', payment_link, name='payment-delete'),

    path('status/', StatusView.as_view(), name='status'),
    path('smart-links/', SmartLinksView.as_view(), name='smart-links'),
    path('payments/', PaymentsView.as_view(), name='payments'),
    path('support/', SupportView.as_view(), name='support'),
]
