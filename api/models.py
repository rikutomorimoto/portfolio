from django.db import models

class BigThree(models.Model):
    username = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    weight = models.IntegerField()
    reps = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def _get_max_rm(self):
        div = 0
        if self.title == "ベンチプレス":
            div = 40.0
        else:
            div = 33.3
        return self.weight * self.reps // div + self.weight
    rm = property(_get_max_rm)