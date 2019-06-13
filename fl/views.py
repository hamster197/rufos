from rest_framework import viewsets
from .serializers import PageDetailSerializer, PageIndexSerializer
from .models import page



class PageViewSet(viewsets.ReadOnlyModelViewSet):
   queryset = page.objects.all()

   def get_serializer_class(self):
       if self.action == 'list':
           return PageIndexSerializer
       return PageDetailSerializer