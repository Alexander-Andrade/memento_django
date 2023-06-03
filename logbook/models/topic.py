from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=64, null=False)
    bookmark = models.ForeignKey('logbook.Bookmark', on_delete=models.CASCADE, related_name='topics')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name
