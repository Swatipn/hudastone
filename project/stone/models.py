from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    number=models.IntegerField()
    description=models.TextField()

    def __str__(self):
        return self.email +" "+"by"+" "+ self.name


class Posts(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    img=models.ImageField(upload_to='Natural Stones', blank=True , null=True, default='/static/img/default-user.png')

    def __str__(self):
        return self.title