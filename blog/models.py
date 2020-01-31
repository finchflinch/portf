from django.db import models

class Blog(models.Model):
    desc = models.CharField(max_length=20)
    summary = models.CharField(max_length=200)

    def summ (self):
        return self.summary[:25]
    
    def __str__ (self):
        return self.desc

