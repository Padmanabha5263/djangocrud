from django.db import models


# Create your models here.

class Customers(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    phone=models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table="Customer"