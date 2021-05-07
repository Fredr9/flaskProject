import json
import random
# import sys
# from typing import Dict
import time

import requests

url = "http://localhost:5000/api"
availablebots = "Available bots are: Joakim, Fredrik, Alex or Jesper, Type the name of the bot you want too choose:"
botname = input(availablebots).lower()
# botname = sys.argv[1]

# list of words

greetingsJoakim = ["Hello", "Hi", "Hello there", "Heihei"]
greetingsIfNoroomJoakim = ["Hello, I made a new ROOM even if it wasnt my job!",
                           "You didnt care to make a new room, so i did!"]
greetingsFedrik = ["Hallo", "Hei", "Næmmen er det noen her", "Jeg har ankommet"]
greetingsIfNoroom2 = ["Hello? anyone here? I make a room for anyone wants to join"]
greetingsJesper = ["Hallo der", "God morgen", "morn", "Hvorfor er jeg her"]
greetingsIfNoroom3 = ["Looks like I have to make a room then"]
greetingsAlex = ["Mr.Alex har ankommet festen", "Haihai", "welcome me", "I have arrived"]
greetingsIfNoroom4 = ["I have to take responsibility and make a room"]

if botname == "joakim":
    username = {'username': 'Joakim'}
    newUser = requests.post('http://127.0.0.1:5000/api/users', json=username)
    if newUser.status_code == 409:
        print("User already exists")
        exit(409)

    print(newUser.json())
    data = newUser.json()
    userid = data[0]
    # print(userid)

    getChatrooms = requests.get('http://127.0.0.1:5000/api/chat-rooms')
    data = getChatrooms.json()

    if len(data) > 0:
        room = json.loads(data[0])
        # print(room)
        # Printing the name of the room you are joining:
        print(" Joining a chatroom with name " + room['roomname'])
        # print(room['id'])
        # Make a variable with room id extracted
        roomId = room['id']
        # Bot joining the first room:
        f = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(roomId), json={"userId": userid},
                          headers={"Content-Type": "application/json"})

        # Bot sends message:

        text = random.choice(greetingsJoakim)
        re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                           json={"text": text},
                           headers={"Content-Type": "application/json"})

        print("\n ### A NEW MESSAGE POSTED ### \n")
        print(botname + ": " + text)
        print("\n### MESSAGE ENDED ###\n")

    else:
        # getChatrooms2 = requests.get('http://127.0.0.1:5000/api/chat-rooms')
        # data2 = getChatrooms2.json()
        print("No room exists, I will create one!")
        # Create a room:
        chatroom = {'chat-room': input("Make a new chatroom:")}

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

        text = random.choice(greetingsIfNoroomJoakim)
        # Trying to send a message:
        melding = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                                json={"text": text},
                                headers={"Content-Type": "application/json"}
                                )
        print("\n ### A NEW MESSAGE POSTED ### \n")
        print(text)
        print("\n### MESSAGE ENDED ###\n")
        time.sleep(3)
        text2 = "This is my second message"
        # Trying to send a message:
        requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                      json={"text": text2},
                      headers={"Content-Type": "application/json"})
        print("\n ### A NEW MESSAGE POSTED ### \n")
        print(text2)
        print("\n### MESSAGE ENDED ###\n")
        print("Good bye!")

elif botname == "fredrik":
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
        f = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(roomId), json={"userId": userid},
                          headers={"Content-Type": "application/json"})

        # Bot sends message:

        text = random.choice(greetingsFedrik)
        re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                           json={"text": text},
                           headers={"Content-Type": "application/json"})

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

        text = random.choice(greetingsIfNoroom2)
        # Trying to send a message:
        melding = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                                json={"text": text},
                                headers={"Content-Type": "application/json"}
                                )
        print(text)
        print("Good bye!")





elif botname == "jesper":
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

        text = random.choice(greetingsJesper)
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

        text = random.choice(greetingsIfNoroom3)
        # Trying to send a message:
        melding = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                                json={"text": text},
                                headers={"Content-Type": "application/json"}
                                )
        print(text)
        print("Good bye!")


elif botname == "alex":
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
        # Bot sends message:
        text = random.choice(greetingsAlex)
        re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                           json={"text": text},
                           headers={"Content-Type": "application/json"})
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

        text = random.choice(greetingsIfNoroom4)
        # Trying to send a message:
        melding = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                                json={"text": text},
                                headers={"Content-Type": "application/json"}
                                )
        print(text)
        print("Good bye!")

if botname not in {"joakim", "fredrik", "alex", "jesper"}:
    print("You need to choose one of these bots: Joakim, Fredrik, Alex or Jesper")
