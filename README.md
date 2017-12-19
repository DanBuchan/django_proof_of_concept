# Requirements
1. python3
2. django2

# Setup/install
1. python manage.py makemigrationtest_app
2. python manage.py migrate
3. python manage.py createsuperuser

# Development testing:
  Records can be added by hand using the django admin interface

# Production instance:
  The following todos are not addressed for Produuction

1. Test coverage for all functions
2. loading data from CSV
  * Models:
    * Diseasefile - stores a non-redundant list of the disease files
      * diseasename - the name of the file with the file suffix ('.csv') removed
    * Predictions -
      * disease - ForeignKey link that connects each record to the file it came from
      * gene_id - plain text name of the gene_id
      * prediction - float value of the prediction
3. Make templates in to valid HTML
4. Add CSS and styling
5. Graceful handling missing or empty results
