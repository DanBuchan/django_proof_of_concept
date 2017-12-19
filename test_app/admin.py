from django.contrib import admin

from .models import *


class DiseasefileAdmin(admin.ModelAdmin):
    list_display = ('diseasename', )


class PredictionAdmin(admin.ModelAdmin):
    list_display = ('disease', 'gene_id', 'prediction')


admin.site.register(Diseasefile, DiseasefileAdmin)
admin.site.register(Predictions, PredictionAdmin)


# Register your models here.
