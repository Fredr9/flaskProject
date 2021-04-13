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

# Choose what you want to do with the server:
# It depends on which key word you use:
if chooser == "adduser":
    #user = []
    #user.append(chooser)
    #if user[0] == user[1]:
    #    print(" the user already exist")
    username = {'username': input()}
    newUser = requests.post('http://127.0.0.1:5000/api/users', json=username)
    print(newUser.json())

if chooser == "getusers":
    getUser = requests.get('http://127.0.0.1:5000/api/users')
    print(getUser.json())

if chooser == "addchatrooms":
    chatroom = {'chat-room': input()}
    newChatroom = requests.post('http://127.0.0.1:5000/api/chat-rooms', json=chatroom)
    print(newChatroom.json())

if chooser == "getchatrooms":
    getChatrooms = requests.get('http://127.0.0.1:5000/api/chat-rooms')
    print(getChatrooms.json())

    # Get users from a specific room:
if chooser == "GetSpesificRoom":
    getSpecificChatRoom = requests.get('http://127.0.0.1:5000/api/chat-rooms')

'''
Starting to implement som bot like features;:
if chooser == "Alice":
    print("hello I am Alice")

if chooser == "Bob":
    print("Hello I am Bob")
if chooser == "Ray":
    print(" EEEYo THis is ray")
if chooser == "Batman":
    print("Batman is here to save the day!")

'''

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