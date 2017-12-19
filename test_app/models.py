from django.db import models


# Create your models here.
class Diseasefile(models.Model):
    # the file name with the suffix removed, provides a non-redunand list of diseases
    diseasename = models.CharField(max_length=128)
    def __str__(self):
        return self.diseasename


class Predictions(models.Model):
    # foreignkey that links the non-redundant disease list
    disease = models.ForeignKey(Diseasefile, db_index=True,
                                on_delete=models.PROTECT, null=False,
                                blank=False)
    # text name of the genes for searching
    gene_id = models.CharField(db_index=True, max_length=128,
                               null=False, blank=False)
    # prediction values as floats
    prediction = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.gene_id
