from django.db import models


class Bookmark(models.Model):
    title = models.CharField(max_length=64, null=False)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='bookmarks', null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title
