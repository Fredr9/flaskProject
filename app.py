import uuid
from random import random, choice

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json

url = "http://127.0.0.1:5000/"
app = Flask(__name__)
api = Api(app)

# State when starting
users = []
chatrooms = []
idUser = [1, 2, 3, 4, 5, 6]


class Chatroom:
    def __init__(self, id, roomname):
        self.id = str(id)
        self.roomname = roomname
        self.users = []
        self.messages = []

    def toJSONChatroom(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class User:
    def __init__(self, id, username):
        self.id = str(id)
        self.username = username

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Message:
    def __init__(self, text, user):
        self.id = str(id)
        self.text = text
        self.user = user

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


# Define chatRooms
#
# If you forget to type the s at the end
@app.route('/api/chat-room')
def chatRooms():
    return '<h1>Wrong path </h1>' \
           '<p1>If you want to go too the chat-rooms go to 127.0.0.1:5000/chat-rooms</p1>'

# Show all the chatrooms:
@app.route('/api/chat-rooms', methods=['GET'])
def getChatrooms():
    return jsonify([chatroom.toJSONChatroom() for chatroom in chatrooms])


# ADd new chatroom
@app.route('/api/chat-rooms', methods=['POST'])
def addChatrooms():
    content = request.json
    chatroomname = content['chat-room']
    # Random ID to chatrooms
    idchatroom = uuid.uuid1()
    chatroom = Chatroom(idchatroom, chatroomname)
    chatrooms.append(chatroom)
    return jsonify(chatroom.id)

# Get users from a specific room:
@app.route('/api/chat-rooms/<chatroomID>/users', methods=['GET'])
def getUsersInChatroom(chatroomID):
    room = findChatRoom(chatroomID)
    if (room == None):
        return "Cant find room"

    return jsonify([user.toJSON() for user in room.users])

def findChatRoom(chatroomID):
    for i in range(len(chatrooms)):
        if chatrooms[i].id == chatroomID:
            return chatrooms[i]
    return None


@app.route('/api/chat-rooms/<chatroomID>', methods=['GET'])
def getChatroom(chatroomID):
    for i in range(len(chatrooms)):
        if chatrooms[i].chatroomID == chatroomID:
            return chatrooms[i].toJSON()

    return "No such chatroom"


# Abort functions
def abort_if_exists(username):
    if username in users:
        abort(409, message="User aleady exits")

def abort_if_not_reg(username):
    if username not in users:
        abort(5, message="User not registered")



# reqparser() use

# define the classes chatrooms, messages and users


# functions to do a specific task
# command Api.add_resource(name of the class, route)
# after run app.run(debug, deport)
# Gets all the users in the system.

@app.route('/api/users', methods=['GET'])
def getUsers():
    return jsonify([user.toJSON() for user in users])


# ADd new user
@app.route('/api/users', methods=['POST'])
def addUsers():
    content = request.json
    username = content['username']
    # Random ID to users
    id = uuid.uuid1()
    # id = choice(idUser)
    # Prøver å lage en id som er litt mindre kompleks
    user = User(id, username)
    users.append(user)
    #abort_if_exists(username)
    return jsonify(user.id)


# Find one specific user
@app.route('/api/users/<userId>', methods=['GET'])
def getUser(userId):
    for i in range(len(users)):
        if users[i].id == userId:
            return users[i].toJSON()

    return "No such user"


# Delete one specific user
@app.route('/api/users/<userId>', methods=['DELETE'])
def delete(userId):
    index = findSpecificIndex(userId)
    if index == -1:
        return "Cant find user"

    del users[index]
    return "User deleted"


# Function that find index of user
def findSpecificIndex(userId):
    for i in range(len(users)):
        if users[i].id == userId:
            return i
    return -1  # Did not find user


@app.route('/api/room/room-id/messages')
def getMessages():
    return 'Hello, this is a message'


@app.route('/api/room/room-id/user-id/messages')
def getAllMessagesForUSer():
    return 'Hello, this is a message'


@app.route('/')
def server_start():
    return 'You need to specify path'


# class Messages:

if __name__ == "__main__":
    app.run(debug=True)
