import requests
from requests.auth import HTTPBasicAuth

# Class for creating document in Therefore Document Management System with REST API


class CreateDocument:

    def __init__(self, json, user, password):
        self.url = 'https://teamworkarapovic.thereforeonline.com/theservice/v0001/restun/CreateDocument'
        self.headers = {'TenantName': 'TeamworkArapovic'}
        self.json = json
        self.user = user
        self.password = password

    def create_document(self):

        r = requests.post(self.url, headers=self.headers, auth=HTTPBasicAuth(self.user, self.password), json=self.json)
        response = r.json()

        return response['DocNo']


