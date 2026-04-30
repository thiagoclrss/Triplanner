# Register your models here.
# https://docs.djangoproject.com/pt-br/6.0/intro/tutorial07/#customize-the-admin-form
from django.contrib import admin

from . import models


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    # campos de listagem
    list_display = ['name', 'importance', 'count_routes']
    search_fields = ['name']
    list_filter = ['importance']

    class RouteInline(admin.TabularInline):
        model = models.Route
        fk_name = 'src'
        extra = 0
        classes = ['collapse']

    # campos de edição
    prepopulated_fields = {"slug": ["name"]}
    inlines = [RouteInline]

    def count_routes(self, obj: models.City):
        return obj.routes.count()
    count_routes.short_description = 'número de rotas'


@admin.register(models.Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'cost', 'time']
