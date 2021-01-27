
import re
import secrets

from rest_framework import status
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

    def create(self, serializer):

        def isurl(url):
            regex = re.compile(
                r'^(?:http|ftp)s?://' # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
                r'localhost|' # localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                r'(?::\d+)?' # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)
            if re.search(regex, url):
                return True
            return False

        def isslug(slug):
            if slug != '':
                regex = re.compile(r'^[a-z0-9_-]+$')
                if re.search(regex, slug):
                    return True
            return False

        def uniqueSlug():
            slug = secrets.token_urlsafe(8)
            if Shortener.objects.filter(slug=slug).exists():
                return uniqueSlug()
            return slug


        try:
            url = self.request.data['url']
            slug = self.request.data.get('slug', '')
        except KeyError as e:
            return Response({'Error': 'Invalid URL.'}, status=status.HTTP_400_BAD_REQUEST)

        if isurl(url):
            if isslug(slug):
                if Shortener.objects.filter(slug=slug).count() > 0:
                    return Response({'Error': 'Slug is Registered.'}, status=status.HTTP_409_CONFLICT)
            elif slug == '':
                slug = uniqueSlug()
            else:
                return Response({'Error': 'Invalid Slug.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error': 'Invalid URL.'}, status=status.HTTP_400_BAD_REQUEST)

        Shortener.objects.create(url=url, slug=slug).save()
        responseData = { 'url': url, 'slug':slug }

        return Response(responseData, status=status.HTTP_200_OK)
