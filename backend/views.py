import requests
import json
from django.shortcuts import render


def get_data(request):
    api_key = "ZTRlZTE0YjctYzQxYy00NDlkLThhYWItZDM0NThiMTgyMjU5"
    data = {'x-api-key': api_key}
    url = 'https://api.clockify.me/api/v1/workspaces/6359526f380707416dd956c3/projects/635952e9e7b7d85fb687fa31/tasks'
    response = requests.get(url, headers=data)
    response = json.loads(response.text)
    name = [i['name'] for i in response]
    return render(request, 'base.html', {'name': name})





