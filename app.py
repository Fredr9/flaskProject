import uuid

from flask import Flask, request, jsonify

app = Flask(__name__)

# State when starting
users = []

@app.route('/chat-rooms')
def chatRooms():
    return 'Hallo Joakim!'

# Gets all the users in the system.
@app.route('/users', methods=['GET'])
def getUsers():
    return jsonify([user for user in users])

# ADd new user
@app.route('/users', methods=['POST'])
def addUsers():
    content = request.json
    username = content['username']
    # Random ID to users
    id = uuid.uuid1()
    user = User(id, username)
    users.append(user)
    return jsonify([user for user in users])


# Find one specific user
@app.route('/messages')
def getUser(userId):
    for i in range(len(users)):
        if users[i].id == userId:
            return users[i].toJson()

    return "No such user"

@app.route('/messages')
def getMessages():
    return 'Hello, this is a message'

@app.route('/')
def server_start():
    return 'You need to specify path'



