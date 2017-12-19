import os
import django
import csv
import glob

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'test_project.settings')

django.setup()
from test_app.models import *

for csvfile in glob.glob('example_data/*.csv'):
    disease_name = csvfile[13:-4]
    print(disease_name)
    d = Diseasefile.objects.create(diseasename=disease_name)
    d.save()
    with open(csvfile, "r") as csvfh:
        diseasereader = csv.reader(csvfh, delimiter=',', quotechar='|')
        for row in diseasereader:
            p = Predictions(disease=d, gene_id=row[0], prediction=row[1])
            p.save()
