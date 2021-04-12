import uuid

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json

app = Flask(__name__)
api = Api(app)

# State when starting
users = []
chatrooms = []


class Chatroom:
    def __init__(self, id, roomname):
        self.id = str(id)
        self.roomname = roomname


    def toJSONChatroom(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class User:
    def __init__(self, id, username):
        self.id = str(id)
        self.username = username

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


# Define chatRooms
#

@app.route('/chat-rooms')
def chatRooms():
    return 'Here should the chat-rooms appear, E.G 127.0.0.1:5000/chat-rooms'

@app.route('/chat-room', methods=['GET'])
def getChatrooms():
    return jsonify([chatroom.toJSONChatroom() for chatroom in chatrooms])

'''
@app.route('/chat-room', methods=['GET'])
def getChatrooms():
    return jsonify([chatroom.toJSONChatroom()] for chatroom in chatrooms)
'''


# ADd new chatroom
@app.route('/chat-room', methods=['POST'])
def addChatrooms():
    content = request.json
    chatroomname = content['chat-room']
    # Random ID to chatrooms
    idchatroom = uuid.uuid1()
    chatroom = Chatroom(idchatroom, chatroomname)
    chatrooms.append(chatroom)
    return jsonify(chatroom.id)


@app.route('/chat-room/<chatroomID>', methods=['GET'])
def getChatroom(chatroomID):
    for i in range(len(chatrooms)):
        if chatrooms[i].chatroomID == chatroomID:
            return chatrooms[i].toJson()

    return "No such chatroom"


# Abort functions

# reqparser() use

# define the classes chatrooms, messages and users


# functions to do a specific task
# command Api.add_resource(name of the class, route)
# after run app.run(debug, deport)
# Gets all the users in the system.

@app.route('/users', methods=['GET'])
def getUsers():
    return jsonify([user.toJSON() for user in users])


# ADd new user
@app.route('/users', methods=['POST'])
def addUsers():
    content = request.json
    username = content['username']
    # Random ID to users
    id = uuid.uuid1()
    user = User(id, username)
    users.append(user)
    return jsonify(user.id)


# Find one specific user
@app.route('/users/<userId>', methods=['GET'])
def getUser(userId):
    for i in range(len(users)):
        if users[i].id == userId:
            return users[i].toJson()

    return "No such user"


# Delete one specific user
@app.route('/users/<userId>', methods=['DELETE'])
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


@app.route('/messages')
def getMessages():
    return 'Hello, this is a message'


@app.route('/')
def server_start():
    return 'You need to specify path'

# class Messages:
