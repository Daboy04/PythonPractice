from rest_framework.response import Response
from rest_framework.decorators import api_view
from ActivityModel.models import Report
from .serializers import ReportSerializer

@api_view(['GET'])
def getData(request):
    reports = Report.objects.all()
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addReport(request):
    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
