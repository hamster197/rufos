
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PageDetailSer
from .models import page


class PageDetailView(APIView):
    def get(self, request, pk):
        subj = page.objects.filter(pk=pk)
        serializer =PageDetailSer(subj, many=True)
        return Response({"subj": serializer.data})