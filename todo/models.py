from django.db import models

PRIORITY_CHOICES = (
    ('1', "high"),
    ('2', "medium"),
    ('3', "low"),
)

# Create your models here.
class todo(models.Model):
    content = models.CharField(max_length=150)
    priority = models.CharField(max_length = 3, 
        choices = PRIORITY_CHOICES, 
        default = '1')
    on_time = models.TimeField(auto_now_add=True)
    on_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id} : {self.content} {self.priority} {self.on_time} {self.on_date}'