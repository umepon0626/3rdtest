from django.shortcuts import render
from rest_framework import generics
from e_journal.models import E_journal
from .serializers import JournalSerializer

# Create your views here.
class JournalAPIView(generics.ListAPIView):
    queryset = E_journal.objects.all()
    serializer_class = JournalSerializer
