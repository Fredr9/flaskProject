import uuid

# import nltk as nltk
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json

# import numpy
# import tflearn
# import tensorflow


url = "http://127.0.0.1:5000/"
app = Flask(__name__)
api = Api(app)

# State when starting
users = []
chatrooms = []
idUser = [1, 2, 3, 4, 5, 6]
idCounter = 0

'''
with open("bots.json", encoding="utf8") as file:
    bots = json.load(file)

words = []
labels = []
docs = []


for intent in bots ["BotA", "BotB", "BotC", "BotD"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs.append(pattern)

        if intent ["tag"] not in labels:
            labels.append(intent["tag"])


'''


class Chatroom:
    def __init__(self, id, roomname):
        self.id = str(id)
        self.roomname = roomname
        self.users = []
        self.messages = []

    def toJSONChatroom(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class User:
    def __init__(self, id, username):
        self.id = str(id)
        self.username = username

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Message:
    def __init__(self, text, user):
        self.id = str(id)
        self.text = text
        self.user = user

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


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
    idchatroom = 15#uuid.uuid1()
    chatroom = Chatroom(idchatroom, chatroomname)
    chatrooms.append(chatroom)
    return jsonify(chatroom.id)


# Get users from a specific room:
@app.route('/api/chat-rooms/<chatroomID>/users', methods=['GET'])
def getUsersInChatroom(chatroomID):
    room = findChatRoom(chatroomID)
    if (room == None):
        return "Cant find room"

    return jsonify([user() for user in room.users])


# Add users to a room
@app.route('/api/chat-rooms/<chatroomID>/users', methods=['POST'])
def addUserChatroom(chatroomID):
    room = findChatRoom(chatroomID)
    if (room == None):
        return "Cant find the room"  # SER UT TIL Å FEILE HER!==!?

    # Read which user id that should be added from request-body
    print("agaskk og hopp")
    print(request)
    content = request.json
    print(content)
    userId = content['userId']
    print("Finne bruker?")
    user = getUser(userId)
    print("Hvor er feileN?")
    #print(user)
    if (user == "No such user"):
        return "Cant find user"
    print("er den her? ")
    room.users.append(user)  # ADding the user to teh room list
    print(" YSER WAS ADDED")
    #print(room.toJSONChatroom)
    return "The user was added"


# Get the messages from a chatroom
@app.route('/api/chat-rooms/<chatroomID>/messages', methods=['GET'])
def getChatroomMessages(chatroomID):
    room = findChatRoom(chatroomID)
    if (room == None):
        return "Cant find the room"

    content = request.json
    if content is None:
        return "UserId must be provided"
    userId = content['userId']
    user = getUser(userId)
    if (user == None):
        return "cant find user"

    # Return all the users in the room
    return jsonify([message.toJSON() for message in room.messages])


# Get messages from a users in a chatroom
@app.route('/api/<chatroomID>/<userId>/messages', methods=['POST', 'GET'])
def getChatroomMessagesFromUser(chatroomID, userId):
    room = findChatRoom(chatroomID)
    if (room == None):
        return "Cant find the room"

    user = findUserInChatroom(room, userId)
    if (user == None):
        return " Cant find the user in this room"

    userMessages = []
    for message in room.messages:
        if message.userId == user.id:  # Only add the messages you want
            userMessages.append(message)

    # Return all the messages to user in this room
    return jsonify([message.toJSON() for message in userMessages])


# post messages in one chatroom
@app.route('/api/chat-rooms/<chatroomID>/<userId>/messages', methods=['POST', 'GET'])
def addChatroomMessagesForUser(chatroomID, userId):
    room = findChatRoom(chatroomID)
    if (room == None):
        return " cant find the room"

    # Check if the user is in the room
    user = findUserInChatroom(room, userId)
    if (user == None):
        print("hvoer er brukeren=!=!=")
        return "The user is not in this room"

    # Read the message from request
    content = request.json
    print("FUNBGERERE DETTE?")
    print(content)
    if content == None:
        return "Need to provide a message"
    text = content['text']
    message = Message(text, user)
    room.messages.append(message)  # Adding message in list of messages
    return "Messages added"


def findUserInChatroom(room, userId):
    for i in range(len(room.users)):
        if room.users[i] == userId:
            return room.users[i]
    return None  # Didnt find any user


def findChatRoom(chatroomID):
    for i in range(len(chatrooms)):
        if chatrooms[i].id == chatroomID:
            return chatrooms[i]
    return None


@app.route('/api/chat-rooms/<chatroomID>/messages', methods=['GET'])
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
    # id = users
    id = 50 #uuid.uuid1()
    # print(str(users))
    # id = choice(idUser)
    # Prøver å lage en id som er litt mindre kompleks
    user = User(id, username)
    users.append(user)
    return jsonify(user.id, username)
    # abort_if_exists(username)


# Find one specific user
@app.route('/api/users/<userId>', methods=['GET'])
def getUser(userId):
    for i in range(len(users)):
        if users[i].id == userId:
            return users[i].toJSON

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


@app.route('/')
def server_start():
    return 'You need to specify path!'


if __name__ == "__main__":
    app.run(debug=True)
