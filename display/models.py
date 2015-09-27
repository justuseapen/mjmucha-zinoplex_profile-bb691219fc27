from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from graph_zinoplex.models import GraphNode, GraphTreeNode

from datetime import datetime
# Create your models here.


class Profile(models.Model):

    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    honor = models.CharField(max_length=25, blank=True, null=True)
    degree = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    user_account = models.OneToOneField(User, blank=True, null=True)
    picture_url = models.CharField(max_length=150,default=static("Person-icon-grey.jpg"), null=True, blank=True)
    linkedin_url = models.URLField(blank=True, null=True)

    graph_node = models.OneToOneField(GraphNode)

    director_id = models.IntegerField(blank=True, null=True)

    def name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return 'Profile:'+ self.name()

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    user_profile = models.ForeignKey(Profile)
    company = models.ForeignKey(Company)
    position = models.CharField(max_length=50, blank=True, null=True)
    date_started = models.DateField(blank=True, null=True)
    date_ended = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user_profile.name() + '-' + self.company.name

class PPI_scorecard(models.Model):
    user_profile = models.ForeignKey(Profile)
    index_b = models.IntegerField(default=0)
    index_c = models.IntegerField(default=0)
    index_d = models.IntegerField(default=0)
    index_e = models.IntegerField(default=0)
    date_created = models.DateTimeField(blank=True,null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            if not self.date_created:
                self.created = datetime.now()

        super(PPI_scorecard, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_profile.name()+':scorecard'