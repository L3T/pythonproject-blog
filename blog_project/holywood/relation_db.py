# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse

from relation.models import Api
from servives_relation.models import InitRelation


def Apidb(request):
    api_test = Api(api_id='diary', api_functions='search_diary', sour_s='gaia', dest_s='backend')
    api_test.save()
    return HttpResponse("<p> Succeed! </p>")


def InitDb(request):
    test_data1 = InitRelation(src='gaia', target='backend', weight='23450')
    test_data1.save()

    dic = {'src': 'ship', 'target': 'gaia', 'weight': '230'}
    InitRelation.objects.create(**dic)

    InitRelation.objects.create(src='gaia', target='plutus', weight='450')
    return HttpResponse("<p>Succeed!</p>")


def TotalRelation(request):
    api_list = []

    # for relation_id in range(1, total + 1):
    #     relation_list = InitRelation.objects.get(id=relation_id)
    #     relation_dict = model_to_dict(relation_list)
    #     relation_dict.pop(u'id')
    #     api_list.append(relation_dict)
    for relation in InitRelation.objects.all():
        relation_dict = model_to_dict(relation)
        relation_dict.pop('id')
        api_list.append(relation_dict)

    print api_list
    return JsonResponse(data={"api_list": api_list})
