# Testclockify
An app that receive a list of records entered in Clockify through the API. 
In our case, these are tasks that were recorded earlier through the site. App is devided for two parts: 'backend' - where we have our logic and 'frontend' - which will help us to provide separation of concerns in the future when it will be necessary. 

# TechStack 
- Django
- DRF
- clockify API

# Firing up our project:
With PIP:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py runserver 8000
```
With docker-compose:
```
```
With poetry:
```
```
When you are running the server you are going to the main page where there are all tasks from clockify. If we want to receive report on stdout we need to go to backend.views file, and there we have 2 functions, which we can print and receive: 
1. Total time for each task by dateRangeStart and dateRangeEnd;
2. Total project time (All tasks);

