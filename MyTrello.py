import requests
import json

class myTrello:
    def __init__(self, user):
        self.user = user
        self.boards = []
        self.cards = []
        self.lists = []
        
    def setBoards(self):
        url = "https://api.trello.com/1/members/me/boards"
        params = (
            ('fields', 'name,url'),
            ('key', self.user.key),
            ('token', self.user.token),
        )
        
        try:
            response = requests.get(url, params=params)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
            
        self.boards = json.loads(response.text)
    
    def getBoards(self):
        self.setBoards()
                
        return self.boards
    
#     def getBoard(self, boardID):
#         url = "https://api.trello.com/1/boards/" + boardID
#         params = (
#             ('fields', 'name,url'),
#             ('key', user.key),
#             ('token', user.token),
#         )
        
#         try:
#             response = requests.get(url, params=params)
#         except requests.exceptions.RequestException as e:  # This is the correct syntax
#             raise SystemExit(e)
        
    def setCards(self, boardID):
        url = "https://api.trello.com/1/boards/" + boardID + "/cards"
        params = (
            ('key', self.user.key),
            ('token', self.user.token),
        )
        
        try:
            response = requests.get(url, params=params)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
        
        # print(response.text)
        self.cards = json.loads(response.text)
    
    def getCards(self, boardID):
        self.setCards(boardID)
        return self.cards
        
    def setLists(self, boardID):
        url = "https://api.trello.com/1/boards/" + boardID + "/lists"
        params = (
            ('key', self.user.key),
            ('token', self.user.token),
        )
        
        try:
            response = requests.get(url, params=params)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
        
        self.lists = json.loads(response.text) 
    
    def getLists(self, boardID):
        self.setLists(boardID)
        return self.lists
        