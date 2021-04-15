import json
import sys

import flask
from flask import Flask, request, jsonify
import requests
from flask_restful import Api, Resource, reqparse, abort

url = "http://localhost:5000/api"
#chooser = input().lower()
botname = sys.argv[1]

if botname == "Joakim":
    username = {'username': 'Joakim'}
    newUser = requests.post('http://127.0.0.1:5000/api/users', json=username)
    print(newUser.json())
    data = newUser.json()
    userid = data[0]
    print(userid)

    getChatrooms = requests.get('http://127.0.0.1:5000/api/chat-rooms')
    data = getChatrooms.json()

    if len(data) > 0:
        room = json.loads(data[0])
        print(room)
        print(" Fant et cahtroom")
        print(room['id'])
        # Make a variable with room id extracted
        roomId = room['id']
        # Bot joining the first room:
        requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(roomId), json={"userId": userid},
                      headers={"Content-Type": "application/json"})
        # Bot sends message:
        text = "testing"
        requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid), data=text.format(text), json={"userId": userid},
                      headers={"Content-Type": "application/json"})

    else:
        print("Det finnes ingen rom")
    print(data)
    print("Dette er en bot")
else:
    print("ukjent bot")


# Just a duplicate for now
if botname == "Fredrik":
    username = {'username': 'Fredrik'}
    newUser = requests.post('http://127.0.0.1:5000/api/users', json=username)
    print(newUser.json())
    data = newUser.json()
    userid = data[0]
    print(userid)

    getChatrooms = requests.get('http://127.0.0.1:5000/api/chat-rooms')
    data = getChatrooms.json()

    if len(data) > 0:
        room = json.loads(data[0])
        print(room)
        print(" Fant et cahtroom")
        print(room['id'])
        # Make a variable with room id extracted
        roomId = room['id']
        # Bot joining the first room:
        requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(roomId), json={"userId": userid},
                      headers={"Content-Type": "application/json"})
        # Bot sends message:
        requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/messages'.format(roomId), json={"userId": userid},
                      headers={"Content-Type": "application/json"})

    else:
        print("Det finnes ingen rom")
    print(data)
    print("Dette er en bot")
else:
    print("ukjent bot")