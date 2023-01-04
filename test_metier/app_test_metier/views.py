import logging

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import GraphsCategory, GraphsData
from django.contrib.auth import authenticate, login



def home(request):

    categories = GraphsCategory.objects.all()
    data = GraphsData.objects.all()
    context = {'categories': categories,'data': data}

    return render(request, 'index.html', context)
@csrf_exempt
def compute(request):
    logging.warning(f"cfdfdfdf {request.POST.get('cat','')}")
    cat = request.POST.get("cat","")
    graphsdatas=GraphsData.objects.filter(json_data__contains=f'"{int(cat)}":')
    logging.warning(f"cfdfdfdf {len(graphsdatas)}{graphsdatas} ")
    logging.warning(f"cfdfdfdf {graphsdatas[0].json_data} ")
    list=[]
    for graph in graphsdatas:
        list.append(graph.get_power_and_data(cat))
    logging.warning(f"cfdfdfdf {list} ")

    return JsonResponse({"o": list})