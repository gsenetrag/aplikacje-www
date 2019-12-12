from rest_framework import serializers
from .models import Wyborcy, Kandydaci


class WyborcySerializer(serializers.ModelSerializer):
    class Meta:
        model = Wyborcy
        fields = '__all__'


# class WojewodztwoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wojewodztwo
#         fields = '__all__'


# class PartieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Partie
#         fields = ('nazwa','ilosc_glosow')


class KandydaciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kandydaci
        fields = '__all__'