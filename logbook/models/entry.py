from django.db import models


class Entry(models.Model):
    title = models.CharField(max_length=64, null=False)
    description = models.TextField()
    topic = models.ForeignKey('logbook.Topic', on_delete=models.CASCADE, related_name='entries')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title
