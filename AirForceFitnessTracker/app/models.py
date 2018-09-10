"""
Definition of models.
"""

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1)
    age = models.CharField(max_length=60)
    paygrade = models.CharField(max_length=30)
    

class AFPT_Scores(models.Model):
    name = models.ForeignKey(User)

    push_ups_raw = models.CharField(max_length=3)
    push_ups_points = models.CharField(max_length=4)
    push_ups_HR = models.CharField(max_length=15)

    sit_ups_raw = models.CharField(max_length=3)
    sit_ups_points = models.CharField(max_length=4)
    sit_ups_HR = models.CharField(max_length=15)

    run_time_raw = models.CharField(max_length=5)
    run_time_points = models.CharField(max_length=4)
    run_time_HR = models.CharField(max_length=15)

    BMI_raw = models.CharField(max_length=10)
    BMI_points = models.CharField(max_length=4)
    BMI_HR = models.CharField(max_length=15)

class Age_Groups(models.Model):
    Under_Thirty = models.CharField(max_length=10)
    Thirty_to_ThirtyNine = models.CharField(max_length=10)
    Forty_to_FortyNine = models.CharField(max_length=10)
    Fifty_to_FiftyNine = models.CharField(max_length=10)
    Sixty_and_Over = models.CharField(max_length=10)
