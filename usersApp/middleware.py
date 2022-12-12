from ipware import get_client_ip
from django.http import HttpResponse
import requests

from .models import SideVisits

class IPIsValid:
    """
    __init__ : sirve como constructor
    __call__ : se ejecuta antes de mostrar la vista
    """

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        print("ip", ip)
        response_ip = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=40213bf4125645b6b0ef263b4aeaf88f&ip_address=" + ip)
        print(response_ip.status_code)

        if response_ip.status_code == 200:
          
          data_ip = response_ip.json()
          print(data_ip)
          data = {
            'ip_address': data_ip['ip_address'],
            'city': data_ip['city'],
            'country': data_ip['country'],
            'country_code': data_ip['country_code'],
          }
          # print(data)
          new_visit = SideVisits(**data)
          new_visit.save()

        response = self.get_response(request)

        return response
        # if data["country"] == "Peru":
        #     return response
        # else:
        #     return HttpResponse("Esto es solo para Peru", status=401)