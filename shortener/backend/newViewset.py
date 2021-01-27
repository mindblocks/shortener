

import time
import hashlib
import secrets

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ShortenerSerializer
from .models import Shortener

# Shortener Viewset

class ShortenerViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ShortenerSerializer

    def get_queryset(self):
        return None






    def create(self, request, *args, **kwargs):

        def QRcode(QRdata):
            QRobject = QRCode(QRdata, encoding='utf-8')
            qrName = "QR_{}.svg".format(hashlib.sha224(bytes("{} - {}".format(QRdata, time.time()), 'utf-8')).hexdigest())
            QRobject.svg("media/{}".format(qrName), scale = 3)
            return qrName

        def uniqueSlug():
            slug = secrets.token_urlsafe(8)
            try:
                Shortener.objects.get(slug=slug)
                return uniqueSlug()
            except:
                return slug

        #check slug
        slug = self.request.data['slug']
        if slug == "":
            slug = uniqueSlug()

        shortUrl = Shortener.objects.create(
            slug = slug,
            url  = self.request.data['url'],
        )


    class Meta:
       model = Shortener
       fields = (
           'uid',
           'slug',
           'url',
           'date',
           )

