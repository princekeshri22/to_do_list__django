from django.db import models

class List(models.Model):
    field_no = models.BigIntegerField()
    task = models.TextField()
    desc = models.TextField()
    check_task = models.BooleanField()


    def __str__(self):
        return str(self.field_no)
    
