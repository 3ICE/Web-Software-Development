from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=8, unique=True)

    # countries = models.ManyToManyField('Country')

    class Meta:
        ordering = ['name']


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capital = models.CharField(max_length=255)
    code = models.CharField(max_length=8, unique=True)
    population = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    continent = models.ForeignKey(Continent, related_name="countries")

    class Meta:
        ordering = ['name']


"""<field type="CharField" name="name">Åland Islands</field>
       <field type="CharField" name="capital">Mariehamn</field>
       <field type="CharField" name="code">ax</field>
       <field type="PositiveIntegerField" name="population">26711</field>
       <field type="PositiveIntegerField" name="area">0</field>
       <field to="countrydata.continent" name="continent" rel="ManyToOneRel">6</field>"""
