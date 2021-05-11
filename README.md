#Oblig 2

This repository contains oblig 2 2410 for Alex(s336111), Jesper(s341861), Fredrik(s315714).


##General description about the solution

The solution is coded in python 3 (3.8.5) using flask. 
The solution consist of a server, client and bot.

##Limitations
We have tried to add all the operations and restrictions that the task asked for but have struggled to add some functions 
and the global restrictions. 
What we have managed to create is a server where we can add chatrooms and users,
we also have bots that can be added to the rooms.

We have tried to implement every aspect of task 1 and 2, task 1 we feel like we got the most of it,
but task 2 we haven't got all of the aspects correctly, task 3 was unfortunately out of reach for us this time.


##Prerequisite for running the solution

In order to run the solution you need to have python, pip and flask. To install flask run the 
following in your terminal:

``bash
$ pip3 install flask
$ pip3 install flask-restful
``

To identify the bots and chatrooms we used a ID generator called UUID this you need to import:
https://docs.python.org/3.8/library/uuid.html



##Running the solution

The server must be running before you can start the client or bot.

##Starting the server

To start the server type flask run in the terminal, or python3 app.py or just start the app.py in your compiler 
You can use pycharm terminal or terminal to start the program.

If you want to use it in debug mode:
Example: `python3 app.py`

Without debug mode:

Example: `flask run`


##Starting the bot

If you run the bot.py program, you have to choose a name for your bot: you just type the name you want after bot.py e.g bot.py 
Fredrik then Fredrik starts from this list: Fredrik, Joakim, Alex and Jesper.

For example: `python3 bot.py Joakim`

The bot will enter a room if available or make a new one if there isn't any rooms,
with an input so you can choose the name. 
Then send a message to the server in that room.
Info about the bot


The bots doesn't quite behave the way we wanted them to. The bot can register and join an existing or create a new room, 
but we havent found a way to get them to stay connected or reconnect. So a bot sends messages,
and fetch the messages that is currently in the room.

If you run the same bot multiple times it will give an error, abort function is used here. 


###Running the client

Run the client by typing `$ python3 client.py`.
####Supported commands

***adduser***: for adding a new user.

***getusers***: to get current users.

***deleteuser***: to delete a selected user, you need to provide the user id.

***addchatroom***: to add a new chatroom.

***getchatrooms***: to get current chatrooms

***deletechatroom***: to delete a selected chatroom, you need to provide the chatroom id.

