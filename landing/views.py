from django.shortcuts import render
from django.http import JsonResponse
from .models import MonthlyUsage, YearlyUsage

def landing_page(request):
    return render(request, 'landing/index.html')


def monthly_kwh_api(request):
    months = ['Jan', 'Feb', 'Mrz', 'Apr', 'Mai', 'Jun',
              'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez']

    def get_data(year):
        values = MonthlyUsage.objects.filter(year=year).order_by('month').values_list('consumption', flat=True)
        return list(values)

    return JsonResponse({
        "labels": months,
        "datasets": {
            "2024": get_data(2024),
            "2025": get_data(2025)
        }
    })


def co2_monthly_api(request):
    co2_factor = 0.35

    months = ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun',
              'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez']
    
    data_2024 = MonthlyUsage.objects.filter(year=2024).order_by('month')
    data_2025 = MonthlyUsage.objects.filter(year=2025).order_by('month')

    co2_2024 = [round((entry.consumption / 1000) * co2_factor, 2) for entry in data_2024]
    co2_2025 = [round((entry.consumption / 1000) * co2_factor, 2) for entry in data_2025]

    return JsonResponse({
        "labels": months,
        "datasets": {
            "2024": co2_2024,
            "2025": co2_2025
        }
    })


def yearly_usage_api(request):
    co2_factor = 0.35

    usages = YearlyUsage.objects.all().order_by('year')
    labels = [str(u.year) for u in usages]
    energy = [round(u.energy_mwh, 2) for u in usages]
    co2 = [round(u.energy_mwh * co2_factor, 2) for u in usages]

    return JsonResponse({
        "labels": labels,
        "energy": energy,
        "co2": co2
    })