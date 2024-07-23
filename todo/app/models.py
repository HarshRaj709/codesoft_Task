from django.db import models

# Create your models here.
class AddTask(models.Model):
    task_name = models.CharField(max_length=150)
    description = models.TextField(null=True,blank=True)
    duedate = models.DateField()
    duetime = models.TimeField()
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.task_name