# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .serializers import SuraSerializer, AyahSerializer
from .models import Sura, Ayah


class SuraListView(generics.ListAPIView):
    serializer_class = SuraSerializer
    queryset = Sura.objects.all()


class SuraAyatTextView(generics.ListAPIView):
    serializer_class = AyahSerializer
    lookup_field = 'sura_id'
    lookup_url_kwargs = 'sura_num'

    def get_queryset(self):
        # TODO return 404 if no ayat
        qs = Ayah.objects.filter(sura_id=self.kwargs['sura_num'])
        return qs


class AyahRangeTextView(generics.ListAPIView):
    serializer_class = AyahSerializer

    def get_queryset(self):
        from_ayah = self.kwargs['ayah_from_num']
        to_ayah = self.kwargs['ayah_to_num']
        sura_id = self.kwargs['sura_num']
        qs = Ayah.objects.filter(sura_id=sura_id, number__lte=to_ayah, number__gte=from_ayah)
        return qs
