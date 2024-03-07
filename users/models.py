import uuid
from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    info = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)
    social_instagram = models.CharField(max_length=200, null=True, blank=True)
    social_telegram = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="profiles", default="media/default_profile.webp")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.user.username)


class Skill(models.Model):
    user = models.ForeignKey(Profil, on_delete=models.CASCADE, null=True, blank=True, related_name='skill')
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)

# Signal.connect(post_save, create_profile, sender=User)
# Signal.connect(post_delete, delete_user, sender=Profil)
