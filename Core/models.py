from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    region = models.CharField(max_length=200)


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not Mentioned'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    birthDate = models.DateField(auto_now=False, auto_now_add=False)
    phoneNumber = models.CharField(max_length=15)
    oneLinerStatus = models.CharField(max_length=140)
    location = models.OneToOneField(Location, null=True)
    profilePicture = models.ImageField()

    def __str__(self):
        return self.user.first_name + self.user.last_name


class UserSportsInterest(models.Model):
    userInfo = models.ForeignKey('UserInfo')
    # Todo change this to manytomany field
    sport = models.ForeignKey('Sports')


class SportsType(models.Model):
    categoryName = models.CharField(max_length=140)

    def __str__(self):
        return self.categoryName


class Sports(models.Model):
    sportName = models.CharField(max_length=140)
    sportType = models.ForeignKey('SportsType')

    def __str__(self):
        return self.sportName


class Events(models.Model):
    owner = models.OneToOneField(User)
    sport = models.ManyToManyField(Sports)
    name = models.CharField(max_length=80)
    desc = models.CharField(max_length=250)
    startDate = models.DateField()
    location = models.OneToOneField(Location)
    numberOfPlayers = models.IntegerField(default=0)
    EventPicture = models.ImageField()


class EventPlayers(models.Model):
    event = models.OneToOneField(Events)
    players = models.ManyToManyField(User)


