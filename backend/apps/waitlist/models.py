from django.db import models

class Waitlist(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    source = models.CharField(max_length=50, default="landing-page")
    def __str__(self):
        return self.email