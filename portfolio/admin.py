from django.contrib import admin
from .models import PortfolioItem


class PortfolioAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'https://cdn.tiny.cloud/1/b9k3a3np6zu1ev60uccs4sveuh41wrrftes6etizdpts3sod/tinymce/5/tinymce.min.js',
            'js/tiny_init.js'
        )


admin.site.register(PortfolioItem, PortfolioAdmin)
