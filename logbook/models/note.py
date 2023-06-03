from django.db import models


class Note(models.Model):
    description = models.TextField()
    note = models.ForeignKey('logbook.Entry', on_delete=models.CASCADE, related_name='notes')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.description
