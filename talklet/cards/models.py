from django.db import models

# Create your models here.

class Cards(models.Model):
    question_text = models.CharField(max_length=75)
    answer_text = models.CharField(max_length=75)

    def __str__(self):
        return self.question_text + "/" + self.answer_text