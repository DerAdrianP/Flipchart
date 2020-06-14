from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    COLOR_0 = 0
    COLOR_1 = 1
    COLOR_2 = 2
    COLOR_3 = 3
    COLOR_4 = 4
    COLOR_5 = 5
    COLOR_6 = 6
    COLOR_CHOICES = (
        (COLOR_0, 'blue'),
        (COLOR_1, 'yellow'),
        (COLOR_2, 'green'),
        (COLOR_3, 'blueviolet'),
        (COLOR_4, 'orangered'),
        (COLOR_5, 'orange'),
        (COLOR_6, 'red'),
    )

    FONT_0 = 0
    FONT_1 = 1
    FONT_2 = 2
    FONT_3 = 3
    FONT_4 = 4
    FONT_5 = 5
    FONT_6 = 6
    FONT_CHOICES = (
        (FONT_0, '1em'),
        (FONT_1, '1.3em'),
        (FONT_2, '1.6em'),
        (FONT_3, '1.9em'),
        (FONT_4, '2.2em'),
        (FONT_5, '2.5em'),
        (FONT_6, '2.8em'),
    )

    STATUS_0 = 0
    STATUS_1 = 1
    STATUS_2 = 2
    STATUS_CHOICES = (
        (STATUS_0, 'to be discussed'),
        (STATUS_1, 'being discussed'),
        (STATUS_2, 'already discussed'),
    )
    question_text = models.CharField(max_length=200)
    color = models.SmallIntegerField(choices=COLOR_CHOICES,default=COLOR_0)
    font = models.SmallIntegerField(choices=FONT_CHOICES,default=FONT_0)
    status = models.SmallIntegerField(choices=STATUS_CHOICES,default=STATUS_0)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)   
    voters = models.ManyToManyField(User, related_name="choice_voters")
    choice_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.choice_text

