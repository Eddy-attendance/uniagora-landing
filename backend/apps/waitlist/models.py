from django.db import models


class Waitlist(models.Model):
    email = models.EmailField(unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ["-joined_at"]

    def __str__(self):
        return self.email