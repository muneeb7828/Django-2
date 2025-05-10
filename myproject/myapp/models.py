from django.db import models

# Create your models here.
# yaha pe database structure banta he

class Course(models.Model):                                   # ye Model datatypes ke liye he
    title = models.CharField(max_length=100,null=True)        # CharField ye varchar ki tarah hota he
    description = models.CharField(max_length=100)





