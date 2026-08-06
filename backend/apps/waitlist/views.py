from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WaitlistSerializer
from .services import send_welcome_email


class WaitlistView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        print("=" * 50)
        print("REQUEST:", request.data)

        serializer = WaitlistSerializer(data=request.data)

        print("VALID:", serializer.is_valid())
        print("ERRORS:", serializer.errors)

        if serializer.is_valid():

            waitlist = serializer.save()
            print("SAVED:", waitlist.email)

            try:
                send_welcome_email(waitlist.email)
                print("EMAIL SENT")
            except Exception as e:
                print("EMAIL ERROR:", e)

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