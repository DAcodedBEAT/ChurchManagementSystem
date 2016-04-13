from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from Accounting.models import PledgeAccount
from Locations.models import Location

from utils import generate_id


class Family(models.Model):
    name = models.CharField(max_length=200, unique=True)


class FamilyManager(models.Manager):
    def family_for(self, user):
        return self.filter(user.family)

    def parents_for(self, user):
        return self.filter(user.parents)

    def siblings_for(self, user):
        return self.filter(user.siblings)

    def partners_for(self, user):
        return self.filter(user.partners)

    def children_for(self, user):
        return self.filter(user.children)


class UserProfile(models.Model):
    """
    Creates the model of the UserProfile object(s).
    """
    int_uuid = generate_id.int_uuid()

    # System Data
    user = models.OneToOneField(User, parent_link=True)
    slug = models.SlugField(default=str(int_uuid), unique=True)
    created_on = models.DateTimeField(_("created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("updated on"), default=timezone.now)

    # Base Person Data
    gender = models.BooleanField(choices=((True, 'Male'), (False, 'Female')))  # TRUE for male, FALSE for female
    DOB = models.DateField(_("date of birth"), blank=True, null=True)
    DOD = models.DateField(_("date of death"), blank=True, null=True)
    bio = models.TextField(_("bio"), blank=True)
    phone_number = models.CharField(_("phone number"), max_length=10, null=True, blank=True)

    # Family Data
    parents = models.ManyToManyField("UserProfile", related_name='p', verbose_name="Parents", null=True, blank=True)
    siblings = models.ManyToManyField("UserProfile", related_name='s', verbose_name="Siblings", null=True, blank=True)
    partners = models.ManyToManyField("UserProfile", related_name='ps', verbose_name="Partner", null=True, blank=True)
    children = models.ManyToManyField("UserProfile", related_name='c', verbose_name="Children", null=True, blank=True)

    objects = models.Manager()
    family_objs = FamilyManager()

    def __str__(self):
        return self.user.username


class AcctToLocation(models.Model):
    user = models.ForeignKey(UserProfile, primary_key=True)
    location = models.ForeignKey(Location)


class AcctToFamily(models.Model):
    user = models.ForeignKey(UserProfile, primary_key=True)
    family = models.ForeignKey(Family)


class AcctToPledge(models.Model):
    user = models.ForeignKey(UserProfile, primary_key=True)
    pledge_account = models.ForeignKey(PledgeAccount)

## Workaround
#def makeOrGetUserProfile(user):
#    if len(UserProfile.objects.filter(user=user)) != 0:
#        return UserProfile.objects.get(user=user)
#    else:
#        return UserProfile.objects.get_or_create(user=user, location_id=make_uuid())[0]

#User.profile = property(lambda usr: makeOrGetUserProfile(usr))

User.profile = property(lambda usr: UserProfile.objects.get_or_create(user=usr)[0])