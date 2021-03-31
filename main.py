import requests
import json
import argparse
import os
from User import User
from MyTrello import myTrello
from Card import Card


if __name__ == "__main__":
	with open('config.json') as f:
		data = json.load(f)

	user = User(data)

	trello = myTrello(user)
	boards = trello.getBoards()

	print ("{:<10} {:<20} {:<30} {:<20}".format('Num', 'Name', 'ID', 'Url')) 
	count = 1
	for item in boards:
		print ("{:<10} {:<20} {:<30} {:<10}".format(count, item['name'], item['id'], item['url']))
		count += 1

	boardNumber = input("Type the number of board: ")
	boardNumber = int(boardNumber)
	isExist = True if boardNumber in range(1,count) else False

	if not isExist:
		print("Please retry with existing number: ")
		exit()

	lists = trello.getLists(boards[boardNumber-1]['id'])
	print ("{:<10} {:<20} {:<30}".format('Num', 'Name', 'ID')) 
	count = 1

	for item in lists:
		print ("{:<10} {:<20} {:<30}".format(count, item['name'], item['id'])) 
		count += 1

	listNumber = input("Type the number of list: ")
	listNumber = int(listNumber)
	isExist = True if listNumber in range(1,count) else False

	if not isExist:
		print("Please retry with existing number: ")
		exit()

	newCard = Card(boards[boardNumber-1]['id'], lists[listNumber-1]['id'], user)
	cardName = input("Please type card name: ")
	cardDesc = input("Please type card description: ")
	newCard.addCard(cardName, cardDesc)
	cardInfo = trello.getCards(boards[boardNumber-1]['id'])
	addedcardID = cardInfo[-1]['id']


	cardLabelName = input("Please type label name: ")
	cardLabelColors = ["BLUE", "MINT", "SKY", "BLACK", "RED", "PURPLE", "ORANGE", "GREEN", "PINK", "YELLOW"]
	print("====== Label Color options ======")
	print(cardLabelColors)
	cardLabelColor = input("Please type label color: ")

	cardLabelColor = cardLabelColor.lower() if cardLabelColor.upper() in cardLabelColors else ""
	if cardLabelColor == "": print("Invalid label color. It will be appeared with no color.")
	newCard.setLabel(cardLabelName, cardLabelColor)
	labelInfo = newCard.getLabel()

	newCard.addLabel(addedcardID)


