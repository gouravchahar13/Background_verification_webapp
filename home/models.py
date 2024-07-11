from django.db import models
# import relationship


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=100,null=True)
    govt_id = models.IntegerField(primary_key=True)
    cases=models.ForeignKey('Case', on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class Case(models.Model):
    case_id = models.IntegerField(primary_key=True)
    case_status = models.CharField(max_length=100)
    case_description = models.CharField(max_length=100)

    def __str__(self):
        return self.case_type