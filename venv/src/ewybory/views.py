# from django.shortcuts import render

# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import viewsets
# from .models import Wyborcy, Kandydaci, Wojewodztwo, Partie
# from .selializers import WyborcySerializer, KandydaciSerializer, WojewodztwoSerializer, PartieSerializer


from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

from rest_framework import viewsets
from .models import Wyborcy, Kandydaci
from .selializers import WyborcySerializer, KandydaciSerializer

from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import F


class WyborcyView(viewsets.ModelViewSet):
    #def get(self, request):
    queryset = Wyborcy.objects.all()
    serializer_class = WyborcySerializer


class KandydaciView(viewsets.ModelViewSet):
    queryset = Kandydaci.objects.all()
    serializer_class = KandydaciSerializer

    
# class WojewodztwoView(viewsets.ModelViewSet):
#     queryset = Wojewodztwo.objects.all()
#     serializer_class = WojewodztwoSerializer

    
# class PartieView(viewsets.ModelViewSet):
#     queryset = Partie.objects.all()
#     serializer_class = PartieSerializer


# Create your views here.

@api_view(["POST"])
def WybierzListe(data):
    d = JSONParser().parse(data)
    wojewodztwo = d['wojewodztwo']
    print(wojewodztwo)
    lista_kandydatow = Kandydaci.objects.order_by('partia').filter(wojewodztwo=wojewodztwo)
    print(lista_kandydatow)
    stringus = ""
    for i in lista_kandydatow:
        stringus += i.imie+" "
        stringus += i.nazwisko+" "
        stringus += i.partia+" | "
    
    return JsonResponse(stringus,safe=False)
   

@api_view(["POST"])
def Zaglosuj(data):
    d = JSONParser().parse(data)
    wojewodztwo = d['wojewodztwo']
    imie_wyborcy = d['imie_wyborcy']
    nazwisko_wyborcy = d['nazwisko_wyborcy']
    PESEL = d['PESEL']
    nr_dowodu = d['nr_dowodu']
    imie_kandydata = d['imie_kandydata']
    nazwisko_kandydata = d['nazwisko_kandydata']
    partia = d['partia']

    wyborca = Wyborcy.objects.all().filter(wojewodztwo=wojewodztwo,imie=imie_wyborcy,nazwisko=nazwisko_wyborcy,PESEL=PESEL,nr_dowodu=nr_dowodu)

    if wyborca:
        kandydat = Kandydaci.objects.all().filter(imie=imie_kandydata,nazwisko=nazwisko_kandydata,partia=partia)

        for i in kandydat:
            woj_kan = i.wojewodztwo
            id_kan = i.id

        for i in wyborca:
            woj_wyb = i.wojewodztwo

        if kandydat:
            print(woj_kan + " " + woj_wyb)
            if woj_kan == woj_wyb:
                print("Zajebiście")
                Kandydaci.objects.all().filter(id=id_kan).update(liczba_glosow=F('liczba_glosow') + 1)


    lista_kandydatow = Kandydaci.objects.order_by('partia').filter(wojewodztwo=wojewodztwo)
    return JsonResponse("",safe=False)



@api_view(["POST"])
def IdealWeight(heightdata):
    try:
        height=json.loads(heightdata.body)
        weight=str(height*10)
        return JsonResponse("Ideal weight should be:"+weight+" kg",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)