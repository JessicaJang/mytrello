import requests
import json

class User:
    def __init__(self, data):
        # self.username = data[username]
        self.key = data['apikey']
        self.token = data['secret']
    
    def getKey(self):
        return self.key
    
    def getToken(self):
        return self.token