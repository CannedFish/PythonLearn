import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
  question_text = models.CharField(max_length = 200);
  pub_date = models.DateTimeField('data published');

  def __unicode__(self):
    return self.question_text;

  def was_published_resently(self):
    now = timezone.now();
    return timezone.now() - datetime.timedelta(days = 1) <= self.pub_date <= now;
  was_published_resently.admin_order_field = 'pub_date';
  was_published_resently.boolean = True;
  was_published_resently.short_description = 'Published recently?';

class Choice(models.Model):
  question = models.ForeignKey(Question);
  choice_text = models.CharField(max_length = 200);
  votes = models.IntegerField(default = 0);

  def __unicode__(self):
    return self.choice_text;

