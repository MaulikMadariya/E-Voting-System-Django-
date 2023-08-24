from django.db import models

# Create your models here.
class party(models.Model):
    pid=models.IntegerField(primary_key=True,auto_created=True,unique=True,verbose_name='PID')
    name=models.CharField(max_length=100)
    pnumber=models.BigIntegerField()
    image=models.ImageField(upload_to='image')
    paddress=models.TextField(max_length=200)
    city=models.TextField(max_length=200)
    discription = models.TextField(max_length=200)
    total=models.BigIntegerField(default=0)
    email = models.EmailField()
    
    
    def __str__(self):
        return self.name



class userName(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    password = models.TextField(max_length=20)
    cpassword = models.TextField(max_length=20)
    address = models.TextField(max_length=100)
    number = models.BigIntegerField(unique=True)
    email = models.EmailField()
    panNumber = models.TextField(max_length=10)
    aadharNumber = models.TextField(max_length=12,unique=True)
    vote = models.BooleanField(default=False)

    def __str__(self):
        return self.fname

      
   
    