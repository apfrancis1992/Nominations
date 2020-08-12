from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Contracts(models.Model):
    contract_id = models.IntegerField(primary_key=True)
    producer = models.CharField(max_length=100)
    marketer = models.CharField(max_length=100, blank=True, null=True)
    contract_type = models.CharField(max_length=100, blank=True, null=True)
    day_due = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'contracts'

    def __int__(self):
        return self.contract_id

class Nomination(models.Model):
    contract = models.ForeignKey(Contracts, to_field='contract_id', related_name='contract', on_delete=models.CASCADE, verbose_name='Contract')
    day_nom = models.DateField(null=False)
    day_nom_value = models.IntegerField(null=False, validators=[MinValueValidator(0), MaxValueValidator(100000)])
    downstream_contract = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    downstream_ba = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    rank = models.IntegerField(null=False, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    published_date = models.DateTimeField(default=timezone.now(), null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __int__(self):
        return self.contract