from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .const import *
from .timestamp import convert_unix
from .log_gen import get_log_data
import json

id_list, data =  get_log_data('api/logs/logs.txt')

def process_data(var, from_time, to_time, region, gpu, cluster, id, search):

    if var == 'all':
        
        filtered_data = [item for item in data if item['Region'] in region and item['GPU'] in gpu and item['Cluster'] in cluster and from_time <= convert_unix(item['Timestamp']) <= to_time and item['ID'] in id and search in item['Log'].lower()]
        return JsonResponse(filtered_data, safe=False)

    elif var == 'id':
        filtered_data = [item for item in data if item['ID'] != '' and item['Region'] == region and from_time <= convert_unix(item['Timestamp']) <= to_time]
        return JsonResponse(filtered_data, safe=False)

    # filtered_data = [item for item in data if item['ID'] != '' and item['Region'] == 'region']
    # return JsonResponse(filtered_data, safe=False)


def add_all(fetched_list, variable_list) -> list:
    if 'All' in fetched_list:
        fetched_list.pop()
        fetched_list.append('')
        fetched_list.extend(variable_list)
        return fetched_list
    else: return fetched_list

# @api_view([GET])
# def data_request(request, var):
#     if var == 'all':
#         return JsonResponse(data, safe=False)
#     elif var == 'id':
#         filtered_data = [item for item in data if item['ID'] != '']
#         return JsonResponse(filtered_data, safe=False)
#     elif var == 'no_id':
#         filtered_data = [item for item in data if item['ID'] == '']
#         return JsonResponse(filtered_data, safe=False)
#     elif var == 'id_list':
#         return Response({"id":id_list})
#         return Response([{"id": id} for id in id_list])
    
@api_view([GET])
def page(request, var):
    from_time = int(request.GET.get("from", None))
    to_time = int(request.GET.get("to", None))
    region = add_all(request.GET.getlist("var-Region", None), region_list)
    gpu = add_all(request.GET.getlist("var-gpu", None), gpu_list)
    cluster = add_all(request.GET.getlist("var-cluster", None), cluster_list)
    id = add_all(request.GET.getlist("var-id", None), id_list)
    search = request.GET.get("var-search", '').lower()



    print(var, from_time, to_time, region, gpu, cluster, id, search)

    return process_data(var, from_time, to_time, region, gpu, cluster, id, search)

@api_view([GET])
def list_query(request, var):
    print(gpu_list)
    if  var == 'gpu':
        return JsonResponse(gpu_list, safe=False)
    elif  var == 'cluster':
        return JsonResponse(cluster_list, safe=False)
    elif  var == 'region':
        return JsonResponse(region_list, safe=False)
    elif var == 'id':
        return JsonResponse(id_list, safe=False)