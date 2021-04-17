import json
import random
import sys
from typing import Dict

import requests

url = "http://localhost:5000/api"
# chooser = input().lower()
botname = "Joakim"

#list of words

greetings = ["Hello", "Hi", "Hello there", "Heihei"]

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
        random.choice(greetings)
        #text = "testing"
        '''
        requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                      data=text.format(text),
                      json={"userId": userid},
                      headers={"Content-Type": "application/json"})
                      '''
    else:
        print("No room exists")
        print(data)
else:
    print("ukjent bot")


botname = "Fredrik"
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
        print(" Fant et chatroom")
        print(room['id'])
        # Make a variable with room id extracted
        roomId = room['id']
        # Bot joining the first room:
        requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(roomId), json={"userId": userid},
                      headers={"Content-Type": "application/json"})
        # Bot sends message:


        requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/messages'.format(roomId), json={"text": "test 123"},
                      headers={"Content-Type": "application/json"})
        print(requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/messages'.format(roomId), json={"text": "test 123"},
                      headers={"Content-Type": "application/json"}))


    else:
        print("There isnt a room to join")

else:
    print("ukjent bot")


if __name__ == "__main__":
    print('test 123')
