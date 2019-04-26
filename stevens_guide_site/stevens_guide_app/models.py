from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return "Id as Primary Key"


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)
        userprofile.save()


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    score = models.IntegerField()
    logo = models.ImageField(upload_to="images/restaurants")
    description = models.TextField(max_length=1000)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return "To %s from %s" % (self.restaurant, self.user)

    def get_absolute_url(self):
        return reverse("comment", args=[self.restaurant])


class Wishlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return "To %s from %s" % (self.restaurant, self.user)


class Votelist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return "To %s from %s" % (self.restaurant, self.user)
