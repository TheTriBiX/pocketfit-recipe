from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

class HealthCheckView(APIView):
    def get(self, request, format=None):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return Response({"status": "OK", "current_time": current_time})