from django.db import models


class Note(models.Model):
    description = models.TextField(null=False)
    entry = models.ForeignKey('logbook.Entry', on_delete=models.CASCADE, related_name='notes', null=False)

    files = models.JSONField(default=list)
    minimized = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.description
