import requests
import json

class Card:
    def __init__(self, boardID, listID, user):
        self.user = user
        self.boardID = boardID
        self.listID = listID
        self.name = ""
        self.desc = ""
        self.labelID = ""
    
    def setName(self, name):
        self.name = name
    
    def setDesc(self, desc):
        self.desc = desc
    
    def getLabel(self):
        url = "https://api.trello.com/1/boards/"+self.boardID+"/labels"

        query = {
           'key': self.user.key,
           'token': self.user.token
        }
        
        try:
            response = requests.request(
                "GET",
                url,
                params=query
            )
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
        
        labelInfo = json.loads(response.text)
        self.labelID = labelInfo[-1]['id']
    
    def setLabel(self, name="", color=""):
        url = "https://api.trello.com/1/labels"

        query = {
            'key': self.user.key,
            'token': self.user.token,
            'name': name,
            'color': color,
            'idBoard': self.boardID
        }
        
        try:
            response = requests.request(
                "POST",
                url,
                params=query
            )
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)

        self.getLabel()
        
    
    def addCard(self, cardname, carddesc):
        url = "https://api.trello.com/1/cards"
        
        self.setName(cardname)
        self.setDesc(carddesc)
        query = {
            'key': self.user.key,
            'token': self.user.token,
            'idList': self.listID,
            'name': self.name,
            'desc': self.desc,
        }

        try:
            response = requests.request(
               "POST",
               url,
               params=query
            )
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)

    def addLabel(self, cardID):
        url = "https://api.trello.com/1/cards/"+ cardID +"/idLabels"

        query = {
            'key': self.user.key,
            'token': self.user.token,
            'value': self.labelID,
        }
        
        try:
            response = requests.request(
               "POST",
               url,
               params=query
            )
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
