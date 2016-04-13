from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from utils import generate_id


class AbstractMedia(models.Model):
    """
    Creates the abstract model for the media objects.
    """
    int_uuid = generate_id.int_uuid()
    slug = models.SlugField(default=str(int_uuid), unique=True)
    user = models.ForeignKey(User)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True


class Photo(AbstractMedia):
    """
    Creates the model for uploaded Photos.
    """
    media = models.ImageField(upload_to="""enter valid upload path here""")
    thumb = models.ImageField(upload_to="""enter valid upload path here""")
    image_height = models.PositiveIntegerField(editable=False)
    image_width = models.PositiveIntegerField(editable=False)
    default = models.BooleanField(default=False)


class Video(AbstractMedia):
    """
    Creates the model for uploaded Videos.
    """
    media = models.FileField(upload_to="""enter valid upload path here""")
    thumb = models.ImageField(upload_to="""enter valid upload path here""")


class Music(AbstractMedia):
    """
    Creates the model for uploaded Music.
    """
    media = models.FileField(upload_to="""enter valid upload path here""")
    thumb = models.ImageField(upload_to="""enter valid upload path here""")


class Post(models.Model):
    """
    Creates the model for posts.
    """
    int_uuid = generate_id.int_uuid()
    slug = models.SlugField(default=str(int_uuid), unique=True)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(User, related_name="post_sender")
    recipient = models.ForeignKey(User, related_name="post_recipient", blank=True, null=True)
    # various fields
    # medias = models.ManyToManyField(AbstractMedia, null=True, blank=True)