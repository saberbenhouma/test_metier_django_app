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
    logging.warning(f"cfdfdfdf {request.POST.get('cat', '')}")
    cat = request.POST.get("cat", "")
    d = {}
    l = []
    l=get_categ_by_date_and_power(l)

    return render(request, 'index.html', context)


def get_categ_by_date_and_power(categories_list):
    p = 0
    for graph in GraphsCategory.objects.all():
        graphsdatas = GraphsData.objects.filter(json_data__contains=f'"{int(graph.id)}":').order_by('id')
        if graphsdatas:
            initial_date = graphsdatas[0]
            p = graphsdatas[0].data.get(graph.id, 0)
            d = {graph.name: graph.id, "date": initial_date, "power": ""}
            for data in range(1, len(graphsdatas)):
                if graphsdatas[data].dt.day == initial_date.dt.day:
                    p = p + graphsdatas[data].data.get(str(graph.id), 0)
                    d["power"] = p
                else:

                    categories_list.append([graph.name, initial_date.dt.strftime("%d/%m/%Y"), p])
                    p = 0
                    initial_date = graphsdatas[data]
                    d = {graph.name: graph.id, "date": graphsdatas[data].dt, "power": 0}
    return categories_list


@csrf_exempt
def compute(request):
    logging.warning(f"cfdfdfdf {request.POST.get('cat','')}")
    cat = request.POST.get("cat","")
    d={}
    l=[]
    p=0
    for graph in GraphsCategory.objects.all():
        graphsdatas=GraphsData.objects.filter(json_data__contains=f'"{int(graph.id)}":').order_by('id')
        if graphsdatas:
            initial_date = graphsdatas[0]
            p= graphsdatas[0].data.get(graph.id,0)
            d = {graph.name:graph.id, "date":initial_date, "power":""}
            for data in range(1, len(graphsdatas)):
                if graphsdatas[data].dt.day == initial_date.dt.day:
                    p = p+graphsdatas[data].data.get(str(graph.id),0)
                    d["power"] = p
                else:

                    l.append([graph.name,initial_date.dt.strftime("%d/%m/%Y"),p])
                    p = 0
                    initial_date = graphsdatas[data]
                    d={graph.name: graph.id, "date": graphsdatas[data].dt, "power": 0}

    logging.warning(f"cfdfdfdf {l} ")
    li = []
    list=[]
    categories = [{graph.name:graph.id} for graph in GraphsCategory.objects.all()]
    logging.warning(f"cfdfdfdf {categories} ")

    for graph in graphsdatas:
        list.append(graph.get_power_and_data(cat))
    logging.warning(f"cfdfdfdf {list} ")

    return JsonResponse({"o": list})