# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

SEVERITY_CHOICES = (
    (1, 'Minor'),
    (2, 'Major'),
    (3, 'Critical'),
    (4, 'Blocker')
)
# Create your models here.
class Ticket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    assignee = models.ForeignKey('auth.User', related_name='assigned', on_delete=models.CASCADE)
    reporter = models.ForeignKey('auth.User', related_name='reported', on_delete=models.CASCADE)
    description = models.TextField()
    penalty = models.TextField()
    severity = models.CharField(choices=SEVERITY_CHOICES, default='Minor', max_length=100)
    is_done = models.BooleanField(default=False)
    done_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('created',)
