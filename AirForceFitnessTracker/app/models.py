"""
Definition of models.
"""

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=1)
    age = models.CharField(max_length=2)
    unit = models.CharField(max_length=60)
    paygrade = models.CharField(max_length=5)

    def __init__(self, name, gender, age, unit, paygrade):
        return self.name + self.gender + self.age + self.unit + self.paygrade
    
class Age_Groups(models.Model):
    def Under_Thirty(self, age):
        if self.age < 30:
            return self.self
        else:
            pass            
    Under_Thirty = models.CharField(max_length=10)

    def Thirty_to_ThirtyNine(self, age):
        if self.age >= 30:
            if self.age < 40:
                return self.self
            else:
                pass
        else:
            pass
    Thirty_to_ThirtyNine = models.CharField(max_length=10)

    def Forty_to_FortyNine(self, age):
        if self.age >= 40:
            if self.age < 50:
                return self.self
            else:
                pass
        else:
            pass
    Forty_to_FortyNine = models.CharField(max_length=10)

    def Fifty_to_FiftyNine(self, age):
        if self.age >= 50:
            if self.age < 60:
                return self.self
            else:
                pass
        else:
            pass
    Fifty_to_FiftyNine = models.CharField(max_length=10)

    def Sixty_and_Over(self, age):
        if self.age > 60:
            return self.self
        else:
            pass
    Sixty_and_Over = models.CharField(max_length=10)

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

    total_score = models.CharField(max_length=10)
    total_HR = models.CharField(max_length=15)
