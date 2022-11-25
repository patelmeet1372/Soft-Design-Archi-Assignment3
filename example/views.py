from django.shortcuts import render
from django.http import HttpResponse
from .models import ProdInvt
# Create your views here.


def index(request):
    return render(request, 'form.html')


def search(request):
    search_input = request.POST.get('barcode')
    data = list(ProdInvt.objects.filter(item_bc=search_input).values_list('item_details', flat=True))
    return render(request, 'result.html', {"data": data})
