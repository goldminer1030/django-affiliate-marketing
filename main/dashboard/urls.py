from django.urls import path
from .views import DashboardView, OffersView, AffiliatesView, FinancesView, MailRoomView, ToolsView, \
    AdministrationView, delete_smart_link, UserDetailView, NewEarningView, earning_link, payment_link, NewPaymentView


app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('offers/', OffersView.as_view(), name='offers'),
    path('affiliates/', AffiliatesView.as_view(), name='affiliates'),
    path('finances/', FinancesView.as_view(), name='finances'),
    path('mail-room/', MailRoomView.as_view(), name='mail-room'),
    path('tools/', ToolsView.as_view(), name='tools'),
    path('administration/', AdministrationView.as_view(), name='administration'),
    path('new-earning/', NewEarningView.as_view(), name='new-earning'),
    path('new-payment/', NewPaymentView.as_view(), name='new-payment'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('link/<int:pk>/delete', delete_smart_link, name='link-delete'),
    path('earning/<int:pk>-<slug:slug>/delete', earning_link, name='earning-delete'),
    path('payment/<int:pk>-<slug:slug>/delete', payment_link, name='payment-delete'),
]
