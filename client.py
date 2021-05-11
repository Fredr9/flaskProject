import json

import requests

url = "http://localhost:5000/api"
commands = "Available commands: adduser, getusers, deleteuser, getchatrooms, addchatrooms, deletechatroom, sendmessage " \
           "or getmessages \n" \
           "** or exit to stop the program:"
# chooser = input(commands).lower()

# Choose what you want to do with the server:
# It depends on which key word you use:
while True:
    chooser = input(commands).lower()
    if chooser == "adduser":
        # user = []
        # user.append(chooser)
        # if user[0] == user[1]:
        #    print(" the user already exist")
        username = {'username': input("Enter the name of the user you want to add:\n")}
        newUser = requests.post('http://127.0.0.1:5000/api/users', json=username)
        print(newUser.json())

    if chooser == "getusers":
        getUser = requests.get('http://127.0.0.1:5000/api/users')
        users = getUser.json()
        # if users is None:
        #    exit("There is not any users!")
        print("### Users ###\n")
        # if users is None:
        #    exit("There is not any users!")
        for i in range(len(users)):
            user = json.loads(users[i])
            print(user['username'] + ": " + user['id'] + "\n")
        # print(getUser.json())

    if chooser == "deleteuser":
        userid = input("Type the id of the user you want to delete:")
        # useriD = requests.get('http://127.0.0.1:5000/api/users')
        deleteuser = requests.delete('http://127.0.0.1:5000/api/users/{}'.format(userid))
        # checkifuserisdeleted = requests.post('http://127.0.0.1:5000/api/users/{}'.format(userid))
        print(deleteuser.text)

    if chooser in ("addchatrooms", "addchatroom"):
        chatroom = {'chat-room': input("Add chatroom and you choose the name:")}
        newChatroom = requests.post('http://127.0.0.1:5000/api/chat-rooms', json=chatroom)
        print(newChatroom.json())

    if chooser == "getchatrooms":
        getChatrooms = requests.get('http://127.0.0.1:5000/api/chat-rooms')
        chatrooms = getChatrooms.json()
        print("### Chatrooms ###\n")
        for i in range(len(chatrooms)):
            room = json.loads(chatrooms[i])
            print(room['roomname'] + ": " + room['id'] + "\n")
        # Get users from a specific room:
    if chooser == "GetSpesificRoom":
        getSpecificChatRoom = requests.get('http://127.0.0.1:5000/api/chat-rooms')
        print(getSpecificChatRoom)

    if chooser == "deletechatroom":
        chatroomid = input("Type the id of the chatroom you want to delete:")
        deletechatroom = requests.delete('http://127.0.0.1:5000/api/chat-rooms/{}'.format(chatroomid))
        print(deletechatroom.text)

    if chooser == "getmessages":
        id = input("Provide chatroom id:")
        # NEED TO FORMAT ID
        getSpecificChatRoom = requests.get('http://127.0.0.1:5000/api/chat-rooms/{}/messages'.format(id))
        messagetojson = getSpecificChatRoom.json()
        for i in range(len(messagetojson)):
            message = json.loads(messagetojson[i])
            user = json.loads(message['user'])
            print(user['username'] + ": " + message['text'])

    if chooser == "sendmessage":
        roomId = input("Input room id of the room you want to send message in:")
        userid = input("Input user id of the user you want to send message from:")
        if roomId is not None:
            requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/users'.format(roomId), json={"userId": userid},
                          headers={"Content-Type": "application/json"})
        text = input("What would you like to say:")
        if roomId and userid and text is not None:
            re = requests.post('http://127.0.0.1:5000/api/chat-rooms/{}/{}/messages'.format(roomId, userid),
                               json={"text": text},
                               headers={"Content-Type": "application/json"})
        print("\n ### A NEW MESSAGE POSTED ### \n")
        print(userid + ": " + text)
        print("\n### MESSAGE ENDED ###\n")

    if chooser == "LesMelding":
        print(requests.get('/api/chat-rooms/<chatroomID>/messages'))

    if chooser == "exit":
        exit()

    if chooser not in ("adduser", "getusers", "getchatrooms", "addchatrooms",
                       "addchatroom", "getmessages", "deleteuser", "deletechatroom", "sendmessage"):
        print("\n\nYou need to specify what you want to do!")

    if __name__ == "__main__":
        print("***********\n\n")
