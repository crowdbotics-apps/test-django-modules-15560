
import json
import requests

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework.response import Response


class UserActivationView(APIView):
    """
    Custom view to handle GET request on registration User activation.
    """

    def get (self, request, uid, token):
        site = get_current_site(self.request)
        domain = getattr(settings, 'DOMAIN', '') or site.domain
        protocol = 'https://' if request.is_secure() else 'http://'
        activation_url = reverse('user-activation')
        activation_url = f'{protocol}{domain}{activation_url}'

        post_data = {'uid': uid, 'token': token}
        result = requests.post(activation_url, data=post_data)
        content = json.dumps(result.text)
        return Response(content, status=result.status_code)
