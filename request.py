import requests
from datetime import datetime

TOKEN= "fwefrrehtrhtrh"
USER_NAME="lymh"
GRAPH_ID="kuki09"


create_newuser = {
    "token": "fwefrrehtrhtrh",
    "username": "lymh",
    "agreeTermsOfService": "yes",
    "notMinor":"yes"

}

create_graph = {
    "id":"kuki09",
    "name": "study_hours",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
    "timezone": "UTC"

}

URL='https://pixe.la/v1/users'

#------------Step 1------------

##Here the account was created once the account is created, follow the step #2

#response = requests.post(url=URL,json=create_newuser)


#-----------Step 2--------------

TOKEN_USER ={
    "X-USER-TOKEN":TOKEN
}

#response = requests.post(url=f'{URL}/{USER_NAME}/graphs',json=create_graph,headers=TOKEN_USER)
#print(response.text)


#---------Step 3----------------

CURRENT_TIME = datetime.now()
NOW = CURRENT_TIME.strftime("%Y%m%d")

INSERT_DATA = {
    "date": NOW,
    "quantity":"1.30"
}

response = requests.post(url=f'{URL}/{USER_NAME}/graphs/{GRAPH_ID}',json=INSERT_DATA,headers=TOKEN_USER)
print(response.text)
