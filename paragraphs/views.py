from rest_framework import generics
from .models import Paragraph
from .serializers import ParagraphSerializer

class ParagraphListCreateView(generics.ListCreateAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer

class ParagraphRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer