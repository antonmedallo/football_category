from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from categoryApp.models import Categories,Players
from categoryApp.serializers import CategorySerializer,PlayerSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def categoryApi(request,id=0):
    if request.method=='GET':
        categories = Categories.objects.all()
        categories_serializer=CategorySerializer(categories,many=True)
        return JsonResponse(categories_serializer.data,safe=False)
    elif request.method=='POST':
        category_data=JSONParser().parse(request)
        categories_serializer=CategorySerializer(data=category_data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        category_data=JSONParser().parse(request)
        category=Categories.objects.get(CategoryId=category_data['CategoryId'])
        categories_serializer=CategorySerializer(category,data=category_data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        category=Categories.objects.get(CategoryId=id)
        category.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def playerApi(request,id=0):
    if request.method=='GET':
        players=Players.objects.all()
        players_serializer=PlayerSerializer(players,many=True)
        return JsonResponse(players_serializer.data,safe=False)
    elif request.method=='POST':
        player_data=JSONParser().parse(request)
        players_serializer=PlayerSerializer(data=player_data)
        if players_serializer.is_valid():
            players_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        player_data=JSONParser().parse(request)
        player=Players.objects.get(PlayerId=player_data['PlayerId'])
        players_serializer=PlayerSerializer(player,data=player_data)
        if players_serializer.is_valid():
            players_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        player=Players.objects.get(PlayerId=id)
        player.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)