from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WaitlistSerializer
from .services import send_welcome_email


class WaitlistView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = WaitlistSerializer(data=request.data)

        if serializer.is_valid():

            waitlist = serializer.save()

            # Send welcome email
            try:
                send_welcome_email(waitlist.email)
            except Exception as e:
                print(f"Email Error: {e}")

            return Response(
                {
                    "success": True,
                    "message": "Welcome to the UniAGORA waitlist!",
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "success": False,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )