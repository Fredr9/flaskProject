# flaskProject


Oblig2 data 2410 for
Alex s336111
Jesper s341861 
Fredrik s315714




To start the server type flask run in the terminal, or python3 app.py or just start the app.py in your compiler

If you run the bot.py program, you have to choose a name for your bot: yoy just type the name you want after bot.py e.g bot.py Fredrik then Fredrik starts from this list: Fredrik, Joakim, Alex and Jesper
e.g 
python3 bot.py Joakim


The bot will enter a room if available or make a new one if there isnt any rooms.

then send a message to the server in that room / still trying to make this work

If you run the client program: Start by running python3 client.py in your terminal You choose this by input from user(You) The choices you have are:

adduser: for adding a new user getusers: to get current users addchatroom: to add a new chatroom getchatrooms: to get current chatrooms

We have tried to add all the operations and restrictions that the task asked for but have struggled to add some functions and the global restrictions. what we have managed to create is a server where we can add chatrooms and users, we also have bots that can be added to the rooms.

We have tried to implement every aspect of task 1 and 2, task 1 we feel like we got the most of it, but task 2 we havent got all of the aspects correctly, task 3 was unfortunately out of reach for us this time. 
Since we are three beginners in python, we just started learning it. 
Hopefully we are gaining experience and learing a lot from this. 

the bots doesnt quite behave the way we wanted them to.
The bot can register and join a existing or create a new room, but we couldnt make them post multiple messages or fetch all the messages in the room.

If you run the bots multiple times, the bot will give messages depending on it is in the room or not from before. 

You will have to run the bot seperatly, and if you go too: http://127.0.0.1:5000/api/chat-rooms
You can search for "text" and se the messages.
