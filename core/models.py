from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


import os
import uuid

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

RATING_CHOICES = (
    (0, 'None'),
    (1, 'weak'),
    (2, 'fair'),
    (3, 'standard'),
    (4, 'strong'),
    (5, 'exclusive'),
    )

MULTI_CHOICES = (
    (0, '1'),
    (1, '2'),
    (2, '3'),
    (3, '4'),
    (4, '5'),
    (5, '6+'),
    )

SPEED_CHOICES = (
    (0, 'constant speed'),
    (1, 'can accelerate')
    )

PLURAL_CHOICES = (
    (0, 'None'),
    (1, 'Minimal'),
    (2, 'Some'),
    (3, 'Ample')
    )

YESNO_CHOICES = (
    (0, 'No'),
    (1, 'Yes'),
    )


# Create your models here.
class Robot(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    axes = models.IntegerField(choices=MULTI_CHOICES, null=True, blank=True)
    motionrange = models.IntegerField(choices=PLURAL_CHOICES, null=True, blank=True)
    speed = models.IntegerField(choices=SPEED_CHOICES, null=True, blank=True)
    repeatability = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    payload = models.IntegerField(choices=PLURAL_CHOICES, null=True, blank=True)
    mass = models.IntegerField(choices=MULTI_CHOICES, null=True, blank=True)
    vreach = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    hreach = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    structure = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(viewname="robot_list", args=[self.id])

    def get_reviews(self):
        return self.review_set.all()

class Review(models.Model):
    robot = models.ForeignKey(Robot)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
