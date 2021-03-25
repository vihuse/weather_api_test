from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)

    def get_weather(self):
        return self.name + ': ' + str(self.temperature) + ' ºF. ' + self.description + '.'
