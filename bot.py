import json
import random
import time

import requests



url = "http://localhost:5000/api"
availablebots = "Available bots are: Joakim, Fredrik, Alex or Jesper, Type the name of the bot you want too choose:"
botname = input(availablebots).lower()

# list of words

greetingsJoakim = ["Hello", "Hi", "Hello there", "Heihei"]
greetingsIfNoroomJoakim = ["Hello, I made a new ROOM even if it wasnt my job!",
                           "You didnt care to make a new room, so i did!"]
greetingsFredrik = ["Hallo", "Hei", "Oh is it really someone here??", "I have arrived!!", "Hey I'm Fredrik"]
greetingsIfNoroomFredrik = ["Hello? anyone here? I made a room for anyone wants to join",
                            "It was stricly necesseray for me to make a room, since it wasn't any rooms :S"]
greetingsJesper = ["Hello there", "Good morning", "morning", "Why am i here?", "I'm confused but, hello!"]
greetingsIfNoroomJesper = ["Looks like I had to make a room then",
                           "Please don't punch me, but i had to make a room to stay in"]
greetingsAlex = ["Mr.Alex has arrived to the party", "Haihai", "Welcome me", "I have arrived"]
greetingsIfNoroomAlex = ["I had to take responsibility so i made a room"]

if botname == "joakim":
    username = {'username': 'Joakim'}
    newUser = requests.post('http://127.0.0.1:5000/api/users', json=username)
    if newUser.status_code == 409:
        print("User Joakim already exists")
        exit(409)
    print(newUser.json())
    data = newUser.json()
    userid = data[0]
    # print(userid)

    getChatrooms = requests.get('http://127.0.0.1:5000/api/chat-rooms')
    data = getChatrooms.json()

    if len(data) > 0:
        room = json.loads(data[0])

        # Bot joining the first room:
        print("\n\nWhich room do you want the bot to join?" + " this are the available rooms:\n ")

        print("### Chatrooms ###\n")
        for i in range(len(data)):
            room = json.loads(data[i])
            print(room['roomname'] + ": " + room['id'] + "\n")
        roomId = input("\nInput roomid here:")
        f = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(roomId), json={"userId": userid},
                          headers={"Content-Type": "application/json"})

        print("\n\n Joining a chatroom with name " + room['roomname'])

        # Bot sends message:

        text = random.choice(greetingsJoakim)
        re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                           json={"text": text},
                           headers={"Content-Type": "application/json"})

        print("\n ### A NEW MESSAGE POSTED ### \n")
        print(botname + ": " + text)
        print("\n### MESSAGE ENDED ###\n")

        # Bot gets messages in the room:
        messagesfromotherbots = requests.get('http://127.0.0.1:5000/api/chat-rooms/{}/messages'.format(roomId),
                                             json={"text": text},
                                             headers={"Content-Type": "application/json"})

        # print(messagesfromotherbots.text)
        print("*********************")
        # Fetches the messages from the room
        meldinger = json.loads(messagesfromotherbots.text)
        for j in range(len(meldinger)):
            melding = json.loads(meldinger[j])
            user = json.loads(melding['user'])
            print(user['username'] + ": " + melding['text'] + "\n")


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
    if newUser.status_code == 409:
        print("User Fredrik already exists")
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
        #print(" Joining a chatroom with name " + room['roomname'])
        # print(room['id'])
        # Make a variable with room id extracted
        # Bot joining the first room:
        print("\n\nWhich room do you want the bot to join?" + " this are the available rooms:\n ")

        print("### Chatrooms ###\n")
        for i in range(len(data)):
            room = json.loads(data[i])
            print(room['roomname'] + ": " + room['id'] + "\n")
        roomId = input("\nInput roomid here:")
        f = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(roomId), json={"userId": userid},
                          headers={"Content-Type": "application/json"})

        print("\n\n Joining a chatroom with name " + room['roomname'])
        # Bot sends message:

        text = random.choice(greetingsFredrik)
        re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                           json={"text": text},
                           headers={"Content-Type": "application/json"})

        print("\n ### A NEW MESSAGE POSTED ### \n")
        print(botname + ": " + text)
        print("\n### MESSAGE ENDED ###\n")

        # Bot gets messages in the room:
        messagesfromotherbots = requests.get('http://127.0.0.1:5000/api/chat-rooms/{}/messages'.format(roomId),
                                             json={"text": text},
                                             headers={"Content-Type": "application/json"})

        # print(messagesfromotherbots.text)
        print("*********************")
        # Fetches the messages from the room
        meldinger = json.loads(messagesfromotherbots.text)
        for j in range(len(meldinger)):
            melding = json.loads(meldinger[j])
            user = json.loads(melding['user'])
            print(user['username'] + ": " + melding['text'])

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

        text = random.choice(greetingsIfNoroomFredrik)
        # Trying to send a message:
        melding = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                                json={"text": text},
                                headers={"Content-Type": "application/json"}
                                )
        print("\n ### A NEW MESSAGE POSTED ### \n")
        print(text)
        print("\n### MESSAGE ENDED ###\n")
        time.sleep(3)
        text2 = "This is Fredrik's second message"
        # Trying to send a message:
        requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                      json={"text": text2},
                      headers={"Content-Type": "application/json"})
        print("\n ### A NEW MESSAGE POSTED ### \n")
        print(text2)
        print("\n### MESSAGE ENDED ###\n")
        print("Good bye!")


elif botname == "jesper":
    username = {'username': 'Jesper'}
    newUser = requests.post('http://127.0.0.1:5000/api/users', json=username)
    if newUser.status_code == 409:
        print("User Jesper already exists")
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

        # print(room['id'])
        # Make a variable with room id extracted
        #roomId = room['id']
        # Bot joining the room of your choice:
        # New
        print("\n\nWhich room do you want the bot to join?" + " this are the available rooms:\n ")

        print("### Chatrooms ###\n")
        for i in range(len(data)):
            room = json.loads(data[i])
            print(room['roomname'] + ": " + room['id'] + "\n")
        roomId = input("\nInput roomid here:")
        f = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(roomId), json={"userId": userid},
                          headers={"Content-Type": "application/json"})

        print("\n\n Joining a chatroom with name " + room['roomname'])
        # Bot sends message:

        text = random.choice(greetingsJesper)
        re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                           json={"text": text},
                           headers={"Content-Type": "application/json"})



        print("\n ### A NEW MESSAGE POSTED ### \n")
        print(botname + ": " + text)
        print("\n### MESSAGE ENDED ###\n")
        # Bot gets messages in the room:
        messagesfromotherbots = requests.get('http://127.0.0.1:5000/api/chat-rooms/{}/messages'.format(roomId),
                           json={"text": text},
                           headers={"Content-Type": "application/json"})

        #print(messagesfromotherbots.text)
        print("*********************")
        # Fetches the messages from the room
        meldinger = json.loads(messagesfromotherbots.text)
        for j in range(len(meldinger)):
            melding = json.loads(meldinger[j])
            user = json.loads(melding['user'])
            print(user['username'] + ": " + melding['text'])

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

        text = random.choice(greetingsIfNoroomJesper)
        # Trying to send a message:
        melding = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                                json={"text": text},
                                headers={"Content-Type": "application/json"}
                                )
        print("\n ### A NEW MESSAGE POSTED ### \n")
        print(text)
        print("\n### MESSAGE ENDED ###\n")
        time.sleep(3)
        text2 = "This is Jesper's second message"
        # Trying to send a message:
        requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                      json={"text": text2},
                      headers={"Content-Type": "application/json"})
        print("\n ### A NEW MESSAGE POSTED ### \n")
        print(text2)
        print("\n### MESSAGE ENDED ###\n")
        print("Good bye!")


elif botname == "alex":
    username = {'username': 'Alex'}
    newUser = requests.post('http://127.0.0.1:5000/api/users', json=username)
    if newUser.status_code == 409:
        print("User Alex already exists")
        exit(409)
    print(newUser.json())
    data = newUser.json()
    userid = data[0]
    # print(userid)

    getChatrooms = requests.get('http://127.0.0.1:5000/api/chat-rooms')
    data = getChatrooms.json()

    if len(data) > 0:
        while True:

            time.sleep(3)
            room = json.loads(data[0])
            # print(room)
            # Printing the name of the room you are joining:
            print(" Joining a chatroom with name " + room['roomname'])
            # print(room['id'])
            # Make a variable with room id extracted
            #roomId = room['id']
            # Bot joining the room of your choice:
            print("\n\nWhich room do you want the bot to join?" + " this are the available rooms:\n ")

            print("### Chatrooms ###\n")
            for i in range(len(data)):
                room = json.loads(data[i])
                print(room['roomname'] + ": " + room['id'] + "\n")
            roomId = input("\nInput roomid here:")
            f = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(roomId), json={"userId": userid},
                              headers={"Content-Type": "application/json"})

            print("\n\n Joining a chatroom with name " + room['roomname'])


            # Bot sends message:

            text = random.choice(greetingsAlex)
            re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                               json={"text": text},
                               headers={"Content-Type": "application/json"})

            print("\n ### A NEW MESSAGE POSTED ### \n")
            print(botname + ": " + text)
            print("\n### MESSAGE ENDED ###\n")

            # Bot gets messages in the room:
            messagesfromotherbots = requests.get('http://127.0.0.1:5000/api/chat-rooms/{}/messages'.format(roomId),
                                                 json={"text": text},
                                                 headers={"Content-Type": "application/json"})

            # print(messagesfromotherbots.text)
            print("*********************")
            # Fetches the messages from the room
            meldinger = json.loads(messagesfromotherbots.text)
            for j in range(len(meldinger)):
                melding = json.loads(meldinger[j])
                user = json.loads(melding['user'])
                print(user['username'] + ": " + melding['text'])
            breakpoint(print("its my time!", exit()))

    else:
        while True:

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

            text = random.choice(greetingsIfNoroomAlex)
            time.sleep(3)
            # Trying to send a message:
            melding = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                                    json={"text": text},
                                    headers={"Content-Type": "application/json"}
                                    )
            print("\n ### A NEW MESSAGE POSTED ### \n")
            print(text)
            print("\n### MESSAGE ENDED ###\n")
            time.sleep(3)
            text2 = "This is Alex's second message"
            # Trying to send a message:
            requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
                          json={"text": text2},
                          headers={"Content-Type": "application/json"})
            time.sleep(3)
            print("\n ### A NEW MESSAGE POSTED ### \n")
            print(text2)
            print("\n### MESSAGE ENDED ###\n")

            #test = requests.get('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(chatroomid, userid),
            #              headers={"Content-Type": "application/json"})
            #print(test)
            print("Good bye!")
            '''
            if input("Do you want to exit?") == "exit" or newUser.status_code == 409:
                breakpoint(input(), exit("STOPP"))
            else:
                if input() not in "exit":
                    print("Continue:")
            '''
            breakpoint(print("its my time!", exit()))

if botname not in {"joakim", "fredrik", "alex", "jesper"}:
    print("You need to choose one of these bots: Joakim, Fredrik, Alex or Jesper")
