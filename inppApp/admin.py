from django.contrib import admin
from .models import Site, SousReseaux, Equipement

# Register your models here.
@admin.register(Site)
class Site(admin.ModelAdmin):
    pass

@admin.register(SousReseaux)
class SousReseau(admin.ModelAdmin):
    pass

@admin.register(Equipement)
class Equipment(admin.ModelAdmin):

    actions = ['get_nom']

    @admin.action(description="ouvrir putty")
    def get_nom(self, request, queryset):
        obj = self.get_queryset(request)[0]
        print(obj.nom, f" => {type(obj.nom)}")
