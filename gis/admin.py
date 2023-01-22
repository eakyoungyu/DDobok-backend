from django.contrib import admin
from . import models


@admin.register(models.Gi)
class GiAdmin(admin.ModelAdmin):

    """Gi Admin Definition"""

    list_display = (
        "name",
        "brand",
        "link_store",
        "price",
        "priority",
        "color",
    )

    search_fields = (
        "name",
        "priority",
        "color",
    )

    ordering = (
        "priority",
        "name",
    )
