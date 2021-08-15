from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, TextField
# 
class word(models.Model):
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE, null=True, blank=True)
    
    wordname = models.CharField(max_length=200)
    synonyme = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    sense = models.TextField(null=True, blank=True)
    mastered = models.BooleanField(default=False)
    create = models.DateTimeField( auto_now=True)
    
    def __str__(self):
        return self.wordname
    
    class Meta:
        ordering = ["mastered"]