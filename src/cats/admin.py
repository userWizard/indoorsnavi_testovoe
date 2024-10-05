from django.contrib import admin

from src.cats.models.cats import CatsModel


@admin.register(CatsModel)
class CatsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'age',
        'breed',
        'hairines',
        'created_at',
        'updated_at',
    )
