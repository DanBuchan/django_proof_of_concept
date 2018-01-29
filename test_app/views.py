from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    # we return a list of all the diseases known so that it can be used to prepare the form on
    # index page
    disease_list = Diseasefile.objects.order_by('-pk')
    context = {
        'disease_list': disease_list,
    }
    return render(request, 'test_app/index.html', context)


def get(request):
    # These first twenty lines parse the form from the user and get the data in a form we
    # can use for the table query
    request_copy = request.POST.copy() # make a copy of the FORM data as it is immutable
    request_copy.pop('csrfmiddlewaretoken') # remove the CSRF token as we don't need it
    search_string = request_copy.pop('search_string')[0] # Get the Search string
    # print(search_string)
    filter_strings = []
    # test if the seach strings have commas and if so we split it, then we push
    # all the search terms to filter list
    if ',' in search_string:
        filter_strings = search_string.split(',')
    else:
        filter_strings = [search_string]

    disease_list = []
    # as the form uses a checkbox of the diseases here we loop over over the remaining form elements
    # and push each disease type to a disease search list
    for diseasename in request_copy:
        disease_list.append(request_copy[str(diseasename)])
        
    # run the database query filtering on all search strings and disease values the user provided in the form
    results = Predictions.objects.filter(gene_id__in=filter_strings).filter(disease__in=disease_list)
    # print(len(results))
    # prep the object for return and then call render for the template we want.
    context = { 'prediction_list': results }
    return render(request, 'test_app/result.html', context)
