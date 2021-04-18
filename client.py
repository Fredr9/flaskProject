import requests

url = "http://localhost:5000/api"
chooser = input().lower()

# Choose what you want to do with the server:
# It depends on which key word you use:
if chooser == "adduser":
    # user = []
    # user.append(chooser)
    # if user[0] == user[1]:
    #    print(" the user already exist")
    username = {'username': input()}
    newUser = requests.post('http://127.0.0.1:5000/api/users', json=username)
    print(newUser.json())

if chooser == "getusers":
    getUser = requests.get('http://127.0.0.1:5000/api/users')
    print(getUser.json())

if chooser == "deleteuser":
    useriD = requests.get('http://127.0.0.1:5000/api/users')
    deleteuser = requests.delete('http://127.0.0.1:5000/api/users/<userId>')
    print(deleteuser.json())

if chooser in ("addchatrooms", "addchatroom"):
    chatroom = {'chat-room': input()}
    newChatroom = requests.post('http://127.0.0.1:5000/api/chat-rooms', json=chatroom)
    print(newChatroom.json())

if chooser == "getchatrooms":
    getChatrooms = requests.get('http://127.0.0.1:5000/api/chat-rooms')
    print(getChatrooms.json())

    # Get users from a specific room:
if chooser == "GetSpesificRoom":
    getSpecificChatRoom = requests.get('http://127.0.0.1:5000/api/chat-rooms')

if chooser == "LegTilMelding":
    getSpecificChatRoom = requests.get('/api/chat-rooms/<chatroomID>/messages')

if chooser == "LesMelding":
    print(requests.get('/api/chat-rooms/<chatroomID>/messages'))

if chooser not in ("adduser", "getusers", "getchatrooms", "addchatrooms", "addchatroom"):
    print("You need to specify what you want to do!")

if __name__ == "__main__":
    print('test 123')


