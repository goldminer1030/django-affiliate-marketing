from django.urls import path
from .views import DashboardView, OffersView, AffiliatesView, FinancesView, MailRoomView, ToolsView, AdministrationView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('offers/', OffersView.as_view(), name='offers'),
    path('affiliates/', AffiliatesView.as_view(), name='affiliates'),
    path('finances/', FinancesView.as_view(), name='finances'),
    path('mail-room/', MailRoomView.as_view(), name='mail-room'),
    path('tools/', ToolsView.as_view(), name='tools'),
    path('administration/', AdministrationView.as_view(), name='administration'),
]
