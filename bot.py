import json
import random
import sys
# from typing import Dict

import requests

url = "http://localhost:5000/api"
# chooser = input().lower()
botname = sys.argv[1]

# list of words

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
        f = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(roomId), json={"userId": userid},
                          headers={"Content-Type": "application/json"})
        print(f.status_code)
        '''
        requests.post('/api/chat-rooms/<chatroomID>/users'.format(roomId), json={"userId": userid},
                      headers={"Content-Type": "application/json"})
        '''
        # Bot sends message:
        random.choice(greetings)
        text = "testing"

        re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                           data=text.format(text),
                           json={"userId": userid},
                           headers={"Content-Type": "application/json"})
        print("HER DA?", re.status_code)
        '''       
        q = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid), json={"text": texst},
                      headers={"Content-Type": "application/json"})
        print(q)
        #print(f'A bot has joined, {roomId}'.format(roomId))
                      '''
    else:
        #getChatrooms2 = requests.get('http://127.0.0.1:5000/api/chat-rooms')
        #data2 = getChatrooms2.json()
        print("No room exists, you need to create one")
        # Create a room:
        chatroom = {'chat-room': 'NYTTCHATROOM'}
        newChatroom = requests.post('http://127.0.0.1:5000/api/chat-rooms', json=chatroom)
        print(newChatroom.json())
        #print(data2)
        print("Rom laget", newChatroom.json())

        # Tries to make the bot join the room it made.
        #newChatroom = json.loads(data2[0])
        chatroomid = newChatroom.json()
        k = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(chatroomid),
                          json={"userId": userid},
                          headers={"Content-Type": "application/json"})
        print(k.status_code, "FAEN DA")




else:
    print("ukjent bot")

# botname = "Fredrik"
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
        requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/messages'.format(roomId), json={"userId": userid},
                      headers={"Content-Type": "application/json"})

        '''
        requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/messages'.format(roomId),
                      json={"text": "test 123"},
                      headers={"Content-Type": "application/json"})
        print(requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/messages'.format(roomId),
                            json={"text": "test 123"},
                            headers={"Content-Type": "application/json"}))


'''

    else:
        print("There isnt a room to join")
        print(data)
        print("Dette er en bot")

else:
    print("ukjent bot")

'''
if __name__ == "__main__":
    print('test 123')
'''
