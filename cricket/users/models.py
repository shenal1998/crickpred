from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError, models, router, transaction


class Profile(models.Model):
    user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=100,blank=True)
    zipcode = models.CharField(max_length=20,blank=True)
    bio = models.TextField(max_length=1000,blank=True)
    contact_number = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.user


class runs(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=2)
    match_number = models.IntegerField(null=True)
    runs = models.IntegerField(blank=True,null=True)
    balls_face = models.IntegerField(blank=True,null=True)
    strikerate = models.CharField(max_length=20,blank=True)
    sixers = models.IntegerField(blank=True,null=True)
    fours = models.IntegerField(blank=True,null=True)
    opposite_team = models.CharField(max_length=100,blank=True)
    ground = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.runs


class wickets(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=2)
    match_number = models.IntegerField(null=True)
    overs = models.CharField(max_length=20,blank=True)
    runs = models.IntegerField(blank=True,null=True)
    maidens = models.IntegerField(blank=True,null=True)
    wickets = models.CharField(max_length=20,blank=True)
    econ = models.CharField(max_length=20,blank=True)
    average = models.CharField(max_length=20,blank=True)
    opposite_team = models.CharField(max_length=100,blank=True)
    ground = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.wickets
