from django.db import models
    
class Categories(models.Model):
    CategoryId = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=500)
    CategoryAncestorId = models.PositiveIntegerField()

class Players(models.Model):
    PlayerId = models.AutoField(primary_key=True)
    PlayerName = models.CharField(max_length=500)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    DateOfBirth = models.DateField()
    PhotoFileName = models.CharField(max_length=500)