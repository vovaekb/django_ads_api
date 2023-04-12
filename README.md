# django_ads_api

:newspaper: Simple REST API application for ads on Python Django REST Framework.

Features:
- list ads in database
- option for setting the status "paid" or "rejected" for the list of teasers

## Run application
Clone the repo, change to the project root folder. Install dependencies from requirements.txt file:

```bash
pip install -r requirements.txt
```
Run the application:
```bash
python manage.py runserver
```

Open admin panel: http://127.0.0.1:8000/admin. 

Under admin account you can edit lessons and teachers in database. 

Navigate to url http://127.0.0.1:8000/ in browser.

REST API endpoints:

* /ads/list (GET) - Returns ads API data.
* /ads/status (POST) - set the status "paid" or "octase" for the list of teasers in format of JSON: {"ids": []}. returns list of ads in JSON.
* /swagger/ (GET) - Swagger documentation
