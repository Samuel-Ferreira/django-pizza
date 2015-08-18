from django.contrib import admin

from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Pizza, PizzaAdmin)
