from django.db import models

# Create your models here.
class Voters(models.Model):
    PESEL = models.IntegerField()
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    login = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    commune = models.ForeignKey('Communes', on_delete=models.CASCADE)


class Communes(models.Model):
    name = models.CharField(max_length=45)
    country = models.ForeignKey('Counties', on_delete=models.CASCADE)


class Counties(models.Model):
    name = models.CharField(max_length=45)
    constituency = models.ForeignKey('Constituencies', on_delete=models.CASCADE)


class Constituencies(models.Model):
    voivodeship = models.CharField(max_length=45)


class Candidates(models.Model):
    number_on_list = models.IntegerField()
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    number_of_votes = models.IntegerField()
    election_committe = models.ForeignKey('ElectionCommittes', on_delete=models.CASCADE)
    commune = models.ForeignKey('Communes', on_delete=models.CASCADE)


class ElectionCommittes(models.Model):
    name = models.CharField(max_length=45)
    drawn_number = models.IntegerField()
    number_of_votes = models.IntegerField()
    nov_in_percents = models.FloatField()
    
