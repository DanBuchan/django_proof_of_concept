from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    disease_list = Diseasefile.objects.order_by('-pk')[:100]
    context = {
        'disease_list': disease_list,
    }
    return render(request, 'test_app/index.html', context)


def get(request):
    request_copy = request.POST.copy()
    request_copy.pop('csrfmiddlewaretoken')
    search_string = request_copy.pop('search_string')[0]
    # print(search_string)
    filter_strings = []
    if ',' in search_string:
        filter_strings = search_string.split(',')
    else:
        filter_strings = [search_string]
    disease_list = []
    for diseasename in request_copy:
        disease_list.append(request_copy[diseasename][0])
    # print(filter_strings)
    # print(disease_list)
    results = Predictions.objects.filter(gene_id__in=filter_strings).filter(disease__in=disease_list)
    # print(len(results))
    context = { 'prediction_list': results }
    return render(request, 'test_app/result.html', context)
