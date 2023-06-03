from django.db import models


class Event(models.Model):
    description = models.TextField()
    note = models.ForeignKey('logbook.Entry', on_delete=models.CASCADE, related_name='events')

    amount = models.DecimalField(max_digits=19, decimal_places=4)
    currency = models.CharField(max_length=3)

    starts_on = models.DateField(null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.description
