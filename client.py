import json
import sys

import flask
from flask import Flask, request, jsonify
import requests
from flask_restful import Api, Resource, reqparse, abort


url = "http://localhost:5000/api"
chooser = input().lower()
#Hello = sys.argv[0]


#showUser = requests.get('http://127.0.0.1:5000/api/chat-rooms')
#print(showUser)
if chooser == "adduser":
    username = {'username': input()}
    newUser = requests.post('http://127.0.0.1:5000/api/users', json=username)
    print(newUser.json())

if chooser == "getusers":
    getUser = requests.get('http://127.0.0.1:5000/api/users')
    print(getUser.json())

if chooser == "getchatrooms":
    getChatroom = requests.get('http://127.0.0.1:5000/api/chat-rooms')
    print(getChatroom.json())

if chooser == "addchatrooms":
    chatroom = {'chat-room': input()}
    newChatroom = requests.post('http://127.0.0.1:5000/api/chat-rooms', json=chatroom)
    print(newChatroom.json())


if chooser not in ("adduser", "getusers", "getchatrooms", "addchatrooms"):
    print("You need to specify what you want to do!")

#r = requests.get('http://127.0.0.1:5000/api/users')
#print(newUser.json())

'''

En slags skallkode, må utbroderes kraftig
Legge til botter og eventuelle svar
while (true)
  print: Velg Kommando:
    1: Hent alle rom.
    2: Lag rom.
    3: Lag bruker
 input  = readInput()

if (input = "1")
  response = request("localhost:5000/rooms")
  print(response)
'''