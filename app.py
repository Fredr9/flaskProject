from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/chat-rooms')
def chatRooms():
    return 'Hallo Joakim!'

@app.route('/users', methods=['GET'])
def getUsers():
    return jsonify([user for user in users])

@app.route('/users', methods=['POST'])
def addUsers():
    content = request.data

    return jsonify([user for user in users])

@app.route('/messages')
def getMessages():
    return 'Hallo Joakim! Det var dumt ja!'

@app.route('/')
def hello_world():
    return 'Hallo Joakim! has'



