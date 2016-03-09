from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100,blank=False,null=True)
    content = models.TextField(blank=False,null=True)
    filepath = models.CharField(max_length=200,blank=True,null=True)
    current = models.BooleanField(default=False)
    next = models.OneToOneField('self',blank=True,null=True)
    
    def __str__(self):
        return "Q."+str(self.pk)+") "+self.title
        
    def is_root(self):
        if self.root:
            return True
        else:
            return False
            
    def is_leaf(self):
        if self.leaf:
            return True
        else:
            return False