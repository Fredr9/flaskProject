# Oblig 2
This repository contains oblig 2 2410 for Alex(s336111), Jesper(s341861), Fredrik(s315714).

## General description about the solution
The solution is coded in python 3 using flask. The solution consist of a server, client and bot.

### Limitations
We have tried to add all the operations and restrictions that the task asked for but have struggled to add some
functions and the global restrictions. What we have managed to create is a server where we can add chatrooms and users,
we also have bots that can be added to the rooms.

We have tried to implement every aspect of task 1 and 2, task 1 we feel like we got the most of it, but task 2 we havent
got all of the aspects correctly, task 3 was unfortunately out of reach for us this time. Since we are three beginners
in python, we just started learning it. Hopefully we are gaining experience and learing a lot from this.

## Prerequisite for running the solution
In order to run the solution you need to have python, pip and flask. To install flask run the following in your terminal:

```bash
$ pip3 install flask
$ pip3 install flask-restful
```

## Running the solution
The server must be running before you can start the client or bot.

### Starting the server
To start the server type flask run in the terminal, or python3 app.py or just start the app.py in your compiler
You can use pycharm terminal or terminal to start the program.

Example: `python3 app.py`

### Starting the bot

If you run the bot.py program, you have to choose a name for your bot: yoy just type the name you want after bot.py e.g
bot.py Fredrik then Fredrik starts from this list: Fredrik, Joakim, Alex and Jesper.

For example:
`python3 bot.py Joakim`

The bot will enter a room if available or make a new one if there isnt any rooms. Then send a message to the server in that room / still trying to make this work.

#### Info about the bot
The bots doesn't quite behave the way we wanted them to. The bot can register and join an existing or create a new room, but we couldnt make them post multiple messages or fetch all the messages in the room.

If you run the bots multiple times, the bot will give messages depending on it is in the room or not from before.

### Running the client

Run the client by typting  `$ python3 client.py`. 

#### Supported commands
***adduser:*** for adding a new user.

***getusers:*** to get current users.

***addchatroom:*** to add a new chatroom.

***getchatrooms:*** to get current chatrooms

### Remove? 
You will have to run the bot seperatly, and if you go too: http://127.0.0.1:5000/api/chat-rooms You can search for "
text" and se the messages.
