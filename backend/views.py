from urllib import request
import requests
import json
from django.shortcuts import render
from requests import Response
"""
All tasks at the page
"""

def get_data(request):
    api_key = "ZTRlZTE0YjctYzQxYy00NDlkLThhYWItZDM0NThiMTgyMjU5"
    data = {'x-api-key': api_key}
    url = 'https://api.clockify.me/api/v1/workspaces/6359526f380707416dd956c3/projects/635952e9e7b7d85fb687fa31/tasks'
    response = requests.get(url, headers=data)
    response = json.loads(response.text)
    name = [i['name'] for i in response]
    return render(request, 'base.html', {'name': name})


def get_homepage(request):
    return render(request, 'home.html')


"""
Total project time (All tasks)
"""


def get_report_summary():
    urlReport = 'https://reports.api.clockify.me/v1'
    key = "ZTRlZTE0YjctYzQxYy00NDlkLThhYWItZDM0NThiMTgyMjU5"
    request_payload = {
        "dateRangeStart": "2022-10-10T00:00:00.000",
        "dateRangeEnd": "2022-11-16T23:59:59.000",
        "summaryFilter": {
            "groups": [
                "USER",
                "PROJECT",
                "TIMEENTRY"]
        }
    }
    workspaceId = '6359526f380707416dd956c3'
    response = requests.post(
        f'{urlReport}/workspaces/{workspaceId}/reports/summary', headers={'X-Api-Key': key}, json=request_payload)
    print('Total project time (All tasks)')
    print('response.status_code:', response.status_code)
    response = json.loads(response.text)
    #   json_formatted_str = json.dumps(response, indent=2)
    print(response)


get_report_summary()


"""
Total time for each task by dateRangeStart and dateRangeEnd
"""

def get_report_detail():
    urlReport = 'https://reports.api.clockify.me/v1'
    key = "ZTRlZTE0YjctYzQxYy00NDlkLThhYWItZDM0NThiMTgyMjU5"
    request_payload = {'dateRangeStart': '2022-01-01T00:00:00.000Z', 'dateRangeEnd': '2022-12-31T23:59:59.999Z',
                       'detailedFilter': {'page': 1, 'pageSize': 50}}
    workspaceId = '6359526f380707416dd956c3'
    response = requests.post(
        f'{urlReport}/workspaces/{workspaceId}/reports/detailed', headers={'X-Api-Key': key}, json=request_payload)
    print('________________________________________')
    print('total time for each task by dateRangeStart and dateRangeEnd')
    print('response.status_code:', response.status_code)
    response = json.loads(response.text)
    #   json_formatted_str = json.dumps(response, indent=2)
    print(response)


get_report_detail()

