# Requirements
1. python3
2. django2

# Setup/install
1. git clone https://github.com/DanBuchan/django_proof_of_concept.git
2. pip install django
3. cd django_proof_of_concept/
4. rm db.sqlite3
5. python manage.py makemigrations test_app
6. python manager.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver

## Browser endpoints
http://127.0.0.1:8000/test_app/

http://127.0.0.1:8000/admin


## Notes
Both test_app/views.py and test_app/models.py contain comments that describe what they are doing. These have been left with the standard django names. There is no need to change them and using the same nomenclature as everyone else it makes it easier to find/google help

# Development testing:
  Records can be added by hand using the django admin interface

# Production instance:
  The following todos are not addressed for Produuction

1. Test coverage for all functions
2. loading data directly from CSV, given the following db details. A toy example is given in populate.py
  * Models:
    * Diseasefile - stores a non-redundant list of the disease files
      * diseasename - the name of the file with the file suffix ('.csv') removed
    * Predictions -
      * disease - ForeignKey link that connects each record to the file it came from
      * gene_id - plain text name of the gene_id
      * prediction - float value of the prediction
4. Switch database to postgres (you can't run SQLite in production)
5. Ensure templates are valid HTML
6. Add CSS and styling
7. Graceful handling missing or empty results
8. Fix hard coded URL in the form
9. Deploy with nginx or apache (depends what you're more familiar with, nginx is probably best in this instance though)
