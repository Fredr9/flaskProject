import json

import requests

url = "http://localhost:5000/api"
commands = "Available commands: adduser, getusers, getchatrooms, addchatrooms or getmessages \n" \
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
        username = {'username': input("Enter the name of the user you want to add:")}
        newUser = requests.post('http://127.0. 0.1:5000/api/users', json=username)
        print(newUser.json())

    if chooser == "getusers":
        getUser = requests.get('http://127.0.0.1:5000/api/users')
        users = getUser.json()
        print("### Users ###\n")
        for i in range(len(users)):
            user = json.loads(users[i])
            print(user['username'] + ": " + user['id'] + "\n")
        #print(getUser.json())

    if chooser == "deleteuser":
        useriD = requests.get('http://127.0.0.1:5000/api/users')
        deleteuser = requests.delete('http://127.0.0.1:5000/api/users/<userId>')
        print(deleteuser.json())

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

    if chooser == "getmessages":
        id = input("Provide chatroom id:")
        # NEED TO FORMAT ID
        getSpecificChatRoom = requests.get('http://127.0.0.1:5000/api/chat-rooms/{}/messages'.format(id))
        messagetojson = getSpecificChatRoom.json()
        for i in range(len(messagetojson)):
            messages = json.loads(messagetojson[i])
            print(messages['message'] + ": ")

    if chooser == "LesMelding":
        print(requests.get('/api/chat-rooms/<chatroomID>/messages'))

    if chooser == "exit":
        exit()

    if chooser not in ("adduser", "getusers", "getchatrooms", "addchatrooms", "addchatroom", "getmessages"):
        print("You need to specify what you want to do!")


    if __name__ == "__main__":
        print('Finished')
