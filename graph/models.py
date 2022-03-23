from django.db import models

# Create your models here.

class Database(models.Model):
    temperature = models.FloatField(default=27)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return ("la température à l'instant "+ str(self.date_added)+ " est: "+ str(self.temperature)+ " °C")
    class Meta:
        db_table = 'graph_data'