import sys
import os
import json
import requests

# Path where you want the project to sit
path = "/Users/Akhilesh/Development/"

def create():
    # Creates folder
    folderName = str(sys.argv[1])
    # In this directory
    os.makedirs(path + folderName)
    # Call GitHub Create Repo API
    github_create(folderName)

def github_create(folderName):
    # Get API Token from https://github.com/settings/tokens
    api_token = 'e79fb763183420bdb9cef0ef89f9840b5cce912d'
    user='akhilesh-k'
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'token ' + api_token
            }
    data = {
            "name": folderName,
            "description": "Initializing the project.",
            "homepage": "https://akhilesh-k.github.io/"+folderName,
            "private": 'true',
            "auto_init": 'true'
            }
    # Convert Python object to JSON string            
    data_json = json.dumps(data)

    response = requests.post('https://api.github.com/' + 'user/repos', auth=(user,api_token), data=data_json)
    print(response)
    print('Intialized the Project and created new GitHub Repository '+folderName)
    # Uncomment below if you want to see the Response of the API
    #print(response.text)
    
    # Parse a JSON string
    json_response = json.loads(response.text)

    # Command to clone the repo
    print('git clone '+json_response['clone_url'])

if __name__ == "__main__":
    create()