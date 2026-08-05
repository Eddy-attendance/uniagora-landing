from rest_framework import serializers
from .models import Waitlist


class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = ("email",)

    def validate_email(self, value):
        value = value.lower().strip()

        if Waitlist.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "This email is already on the waitlist."
            )

        return value