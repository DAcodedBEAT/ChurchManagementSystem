from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.translation import gettext as _

from Locations.models import Location

from utils import generate_id


class EventType(models.Model):
    """
    Creates the model for Event Types, or categorization of Events.
    """
    recurr_choices = (
        (0, _("Never")),
        (1, _("Weekly")),
        (2, _("Bi-Weekly")),
        (3, _("Monthly")),
        (4, _("Quarterly")),
        (5, _("Semi-Annually")),
        (6, _("Annually")),
    )
    name = models.CharField(max_length=250, unique=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    recurrence = models.PositiveSmallIntegerField(choices=recurr_choices)
    recurr_start = models.DateField()
    recurr_end = models.DateField()


class EventManager(models.Manager):
    def event_type_for(self, type):
        return self.filter(event_type=type)

    def title_for(self, title):
        return self.filter(title__icontains=title)

    def location_for(self, loc):
        return self.filter(location=loc)

    def creator_for(self, user):
        return self.filter(User.get_full_name() | Q(User.username))

    def start_for(self, start):
        return self.filter(start=start)

    def end_for(self, end):
        return self.filter(end=end)

    def start_date_for(self, date):
        return self.filter(start__datetime__day=date.day,
                           start__datetime__month=date.month,
                           start__datetime__year=date.year)

    def end_date_for(self, date):
        return self.filter(end__datetime__day=date.day,
                           end__datetime__month=date.month,
                           end__datetime__year=date.year)

    def start_and_end_date_for(self, date):
        return self.filter(start__datetime__day=date.day,
                           start__datetime__month=date.month,
                           start__datetime__year=date.year,
                           end__datetime__day=date.day,
                           end__datetime__month=date.month,
                           end__datetime__year=date.year)

    def start_today_for(self):
        today = timezone.datetime.today()
        return self.start_date_for(today)

    def end_today_for(self):
        today = timezone.datetime.today()
        return self.filter(end__datetime__day=today.day,
                           end__datetime__month=today.month,
                           end__datetime__year=today.year)

    def start_and_end_today_for(self):
        today = timezone.datetime.today()
        return self.filter(start__datetime__day=today.day,
                           start__datetime__month=today.month,
                           start__datetime__year=today.year,
                           end__datetime__day=today.day,
                           end__datetime__month=today.month,
                           end__datetime__year=today.year)


class Event(models.Model):
    """
    Creates the model for Events.
    """
    # event object DB stuff
    slug = models.SlugField(max_length=100, unique=True)
    created_on = models.DateTimeField(_("created on"), default=timezone.now)
    updated_on = models.DateTimeField(_("updated on"), default=timezone.now)
    # basic description
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=100, blank=True, help_text=_('A short sentence description of the event'))
    description = models.TextField(blank=True, help_text=_('All event details which we have.'))
    if 'Locations' in settings.INSTALLED_APPS:
        location = models.ForeignKey(Location, blank=True, null=True)
    else:
        location = models.CharField(max_length=250, blank=True, null=True)
    start = models.DateTimeField(_("start"), help_text=_("The start time must be earlier than the end time."))
    end = models.DateTimeField(_("end"), help_text=_("The end time must be later than the start time."))
    creator = models.ForeignKey(User, null=True, blank=True, verbose_name=_("creator"), related_name='creator')
    # type of event
    event_type = models.ForeignKey(EventType, verbose_name=_("event type"), related_name='event type')

    objects = models.Manager()
    event_objs = EventManager()

    class Meta:
        ordering = ('start',)
        verbose_name = _('event')
        verbose_name_plural = _('events')
        db_table = 'events'

    def __str__(self):
        return str(self.title) + "(" + str(self.created_on) + ")"

    def clean(self):
        if self.start > self.end:
            raise ValidationError('Start date must be earlier than end date.')