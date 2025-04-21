import requests

USERNAME = "USERNAME"
PASSWORD = "PASSWORD"

S = requests.Session()

URL = "https://www.mediawiki.org/w/api.php"

# Retrieve Login token first
PARAMS_0 = {
    'action': "query",
    'meta': "tokens",
    'type': "login",
    'format': "json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

print(LOGIN_TOKEN)

PARAMS_1 = {
    'action': "login",
    'lgname': USERNAME,
    'lgpassword': PASSWORD,
    'lgtoken': LOGIN_TOKEN,
    'format': "json"
}

R = S.post(URL, data=PARAMS_1)
DATA = R.json()

print(DATA)
assert DATA['login']['result'] == 'Success'

