from django.db import models


# Create your models here.
class Diseasefile(models.Model):
    diseasename = models.CharField(max_length=128)

    def __str__(self):
        return self.diseasename


class Predictions(models.Model):
    disease = models.ForeignKey(Diseasefile, db_index=True,
                                on_delete=models.PROTECT, null=False,
                                blank=False)
    gene_id = models.CharField(db_index=True, max_length=128,
                               null=False, blank=False)
    prediction = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.gene_id
