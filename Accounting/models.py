from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.conf import settings

from Events.models import Event


class PledgeAccount(models.Model):
    """
    Creates the model for pledge accounts.
    """
    pledge_num = models.PositiveSmallIntegerField(unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    total_cash = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_checks = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    annual_goal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)


class AbstractCurrency(models.Model):
    """
    Creates the abstract model for currency.
    """
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True


class AbstractPledge(AbstractCurrency):
    """
    Creates the abstract model for currency going towards a pledge account.
    """
    account = models.ForeignKey(PledgeAccount)
    special = models.BooleanField(default=False, help_text=_("Is the currency given due to a special cause?"))
    description = models.TextField(blank=True)

    if 'Events' in settings.INSTALLED_APPS:
        event = models.ForeignKey(Event)
    else:
        event = models.DateField(default=timezone.now().date())

    class Meta:
        abstract = True


class PledgeCheck(AbstractPledge):
    """
    Creates the model for Checks going towards a pledge account.
    """
    check_num = models.TextField()


class PledgeCash(AbstractPledge):
    """
    Creates the model for Cash going towards a pledge account.
    """
    pass