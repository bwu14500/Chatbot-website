from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from playground.bot.JOI import JOI
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def chat(request):
    return render(request, 'index.html')


@csrf_exempt
def response(request):
    json_data = json.loads(request.body)
    text = json_data['message']
    debug = 0
    access = False if debug == 1 else True      
    name = "brandon"
    ai = JOI(name, access = access)
    response = ai.response(text)
    # print(response)
    message = {"answer" : response}
    # print(message)
    return JsonResponse(message)