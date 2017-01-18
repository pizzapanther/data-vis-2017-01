from django.db import models

class Group (models.Model):
  name = models.CharField(max_length=100)
  original_id = models.PositiveIntegerField()
  
class Venue (models.Model):
  name = models.CharField(max_length=100)
  original_id = models.PositiveIntegerField()
  
class Member (models.Model):
  name = models.CharField(max_length=100)
  joined = models.DateTimeField()
  group = models.ForeignKey(Group)
  original_id = models.PositiveIntegerField()
  
class Event (models.Model):
  name = models.CharField(max_length=100)
  original_id = models.PositiveIntegerField()
  
  group = models.ForeignKey(Group)
  venue = models.ForeignKey(Venue)
  