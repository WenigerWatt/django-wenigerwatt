from django.contrib import admin
from .models import MonthlyUsage, YearlyUsage

admin.site.register(MonthlyUsage)
admin.site.register(YearlyUsage)
