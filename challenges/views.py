import json
from django.http import HttpResponse
from django.shortcuts import render
import requests
# from django.http import HttpResponse
# Create your views here.
def index(request):
    data = getData()
    return HttpResponse(data,content_type="application/json")

def getData():
    reponse = requests.get("https://codeforces.com/api/user.ratedList")
    coders = reponse.json()["result"]
    # print(coders[0])
    kgp_coders = []
    for coder in coders:
        try:
          if coder["organization"] == "IIT Kharagpur":
            kgp_coders.append(coder)
        except:
           pass

    return json.dumps( {"status":"OK" ,"results": kgp_coders})
