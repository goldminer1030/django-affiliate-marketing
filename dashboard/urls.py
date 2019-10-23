from django.urls import path
from .views import DashboardView, OffersView, AffiliatesView, PaymentsView, SupportView, \
    delete_smart_link, UserDetailView, NewEarningView, earning_link, payment_link, NewPaymentView, \
    StatusView, SmartLinksView


app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('offers/', OffersView.as_view(), name='offers'),
    path('affiliates/', AffiliatesView.as_view(), name='affiliates'),
    path('new-earning/', NewEarningView.as_view(), name='new-earning'),
    path('new-payment/', NewPaymentView.as_view(), name='new-payment'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('link/<int:pk>/delete', delete_smart_link, name='link-delete'),
    path('earning/<int:pk>-<slug:slug>/delete', earning_link, name='earning-delete'),
    path('payment/<int:pk>-<slug:slug>/delete', payment_link, name='payment-delete'),

    path('status/', StatusView.as_view(), name='status'),
    path('smart-links/', SmartLinksView.as_view(), name='smart-links'),
    path('payments/', PaymentsView.as_view(), name='payments'),
    path('support/', SupportView.as_view(), name='support'),
]
