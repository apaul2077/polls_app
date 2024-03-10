from django.db import models

class Poll(models.Model):
    question = models.TextField()
    firstOption = models.CharField(max_length = 30)
    secondOption = models.CharField(max_length = 30)
    thirdOption = models.CharField(max_length = 30)
    firstOptionCount = models.IntegerField(default = 0)
    secondOptionCount = models.IntegerField(default = 0)
    thirdOptionCount = models.IntegerField(default = 0)

    def total(self):
        return self.firstOptionCount + self.secondOptionCount + self.thirdOptionCount