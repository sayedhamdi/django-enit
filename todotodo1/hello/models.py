from django.db import models

# Create your models here.


class Todo(models.Model):
    text = models.CharField(max_length=50)
    done = models.BooleanField()
    def __str__(self):
        return self.text + '--' + str(self.done)