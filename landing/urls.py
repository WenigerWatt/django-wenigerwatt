from django.urls import path
from .views import landing_page, co2_monthly_api, yearly_usage_api, monthly_kwh_api

urlpatterns = [
    path('', landing_page, name='landing'),
    path('api/monthly-kwh/', monthly_kwh_api, name='monthly_kwh_api'),
    path('api/co2-monthly/', co2_monthly_api, name='co2_monthly_api'),
    path('api/yearly/', yearly_usage_api, name='yearly_usage_api'),
]