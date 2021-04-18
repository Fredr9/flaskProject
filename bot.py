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
greetingsIfNoroom = ["Hello, do i have to make a room?!?", "Is it my job to make a room? ok!"]

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
        # Bot sends message:

        text = random.choice(greetings)
        re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                           json={"text": text},
                           headers={"Content-Type": "application/json"})
        print("HER DA?", re.status_code)
    else:
        # getChatrooms2 = requests.get('http://127.0.0.1:5000/api/chat-rooms')
        # data2 = getChatrooms2.json()
        print("No room exists, I will create one!")
        # Create a room:
        chatroom = {'chat-room': 'NYTTCHATROOM'}
        newChatroom = requests.post('http://127.0.0.1:5000/api/chat-rooms', json=chatroom)
        print(newChatroom.json())
        # print(data2)
        print("I made a room with ID:", newChatroom.json())

        # Tries to make the bot join the room it made.
        # newChatroom = json.loads(data2[0])
        chatroomid = newChatroom.json()
        k = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(chatroomid),
                          json={"userId": userid},
                          headers={"Content-Type": "application/json"})

        text = random.choice(greetingsIfNoroom)
        # Trying to send a message:
        melding = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                                json={"text": text},
                                headers={"Content-Type": "application/json"}
                                )
        print(text)
        print("Good bye!")

elif botname == "Fredrik":
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
        f = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(roomId), json={"userId": userid},
                          headers={"Content-Type": "application/json"})
        print(f.status_code)
        # Bot sends message:

        text = random.choice(greetings)
        re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                           json={"text": text},
                           headers={"Content-Type": "application/json"})
        print("HER DA?", re.status_code)
    else:
        # getChatrooms2 = requests.get('http://127.0.0.1:5000/api/chat-rooms')
        # data2 = getChatrooms2.json()
        print("No room exists, I will create one!")
        # Create a room:
        chatroom = {'chat-room': 'NYTTCHATROOM'}
        newChatroom = requests.post('http://127.0.0.1:5000/api/chat-rooms', json=chatroom)
        print(newChatroom.json())
        # print(data2)
        print("I made a room with ID:", newChatroom.json())

        # Tries to make the bot join the room it made.
        # newChatroom = json.loads(data2[0])
        chatroomid = newChatroom.json()
        k = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(chatroomid),
                          json={"userId": userid},
                          headers={"Content-Type": "application/json"})

        text = random.choice(greetingsIfNoroom)
        # Trying to send a message:
        melding = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                                json={"text": text},
                                headers={"Content-Type": "application/json"}
                                )
        print(text)
        print("Good bye!")





elif botname == "Jesper":
    username = {'username': 'Jesper'}
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
        # Bot sends message:

        text = random.choice(greetings)
        re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                           json={"text": text},
                           headers={"Content-Type": "application/json"})
        print("HER DA?", re.status_code)
    else:
        # getChatrooms2 = requests.get('http://127.0.0.1:5000/api/chat-rooms')
        # data2 = getChatrooms2.json()
        print("No room exists, I will create one!")
        # Create a room:
        chatroom = {'chat-room': 'NYTTCHATROOM'}
        newChatroom = requests.post('http://127.0.0.1:5000/api/chat-rooms', json=chatroom)
        print(newChatroom.json())
        # print(data2)
        print("I made a room with ID:", newChatroom.json())

        # Tries to make the bot join the room it made.
        # newChatroom = json.loads(data2[0])
        chatroomid = newChatroom.json()
        k = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(chatroomid),
                          json={"userId": userid},
                          headers={"Content-Type": "application/json"})

        text = random.choice(greetingsIfNoroom)
        # Trying to send a message:
        melding = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                                json={"text": text},
                                headers={"Content-Type": "application/json"}
                                )
        print(text)
        print("Good bye!")


elif botname == "Alex":
    username = {'username': 'Alex'}
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
        # Bot sends message:

        text = random.choice(greetings)
        re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                           json={"text": text},
                           headers={"Content-Type": "application/json"})
        print("HER DA?", re.status_code)
    else:
        # getChatrooms2 = requests.get('http://127.0.0.1:5000/api/chat-rooms')
        # data2 = getChatrooms2.json()
        print("No room exists, I will create one!")
        # Create a room:
        chatroom = {'chat-room': 'NYTTCHATROOM'}
        newChatroom = requests.post('http://127.0.0.1:5000/api/chat-rooms', json=chatroom)
        print(newChatroom.json())
        # print(data2)
        print("I made a room with ID:", newChatroom.json())

        # Tries to make the bot join the room it made.
        # newChatroom = json.loads(data2[0])
        chatroomid = newChatroom.json()
        k = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(chatroomid),
                          json={"userId": userid},
                          headers={"Content-Type": "application/json"})

        text = random.choice(greetingsIfNoroom)
        # Trying to send a message:
        melding = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                                json={"text": text},
                                headers={"Content-Type": "application/json"}
                                )
        print(text)
        print("Good bye!")




'''
# botname = "Fredrik"
# Just a duplicate for now
elif botname == "Fredrik":
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


    else:
        print("There isnt a room to join")
        print(data)
        print("Dette er en bot")

else:
    print("Good bye")

'''

if botname not in {"Joakim", "Fredrik", "Alex", "Jesper"}:
    print("You need to choose one of theese bots: Joakim, Fredrik, Alex or Jesper")
