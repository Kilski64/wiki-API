import requests

USERNAME = "USERNAME"
PASSWORD = "PASSWORD"


S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

# Step 1: Retrive login token first
PARAMS_0 = {
    'action': "query",
    'meta': "tokens",
    'type': "login",
    'format': "json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step 2: Send a POST request to login. Using the main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword

PARAMS_1 = {
    'action': "login",
    'lgname': USERNAME,
    'lgpassword': PASSWORD,
    'lgtoken': LOGIN_TOKEN,
    'format': "json"
}

R = S.post(URL, data=PARAMS_1)
DATA = R.json()

# Step 3: GET request to fetch CSRF token
PARAMS_2 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

# Step 4: sned a POST request to Logout
PARAMS_3 = {
    "action": "logout",
    "token": CSRF_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_3)
DATA = R.json()

print(DATA)