# Bunny-Bot
A discord bot with simple fun commands, some moderation, and accessing a database through SQL.

Made as a first time programming project.

<img src="https://media.tenor.com/OoBQUN0NcuEAAAAd/loporrit-ff14.gif" style="width:250px;">
<i>Image found on Tenor, showing a loporrit from the game 'Final Fantasy XIV'</i>

<h1>Features</h1>

All the bot commands (with the exception of /help) are found in the Extensions folder in their designated file.

<h2>Fun</h2>
This extension gives several "fun" commands, that add some flavour to the server.

In the first version, the fun commands include: Welcome messages, Bunny hello, /ping, /greet

<h2>Data</h2>
Implemented to have the bot work with a database. SQLite is the database I chose to do that.
Through the /submit command, users can submit image url links and descriptions into a database,
which then SELECTs a random image and displays it in an embed along with its description through the /bunny command.

<h2>Moderation</h2>
Basic discord moderation commands, requiring the bot and the user calling the command, to have administrator level permissions.
Currently they are just basic /kick, /ban, and /purge <msg count, max 100> commands.

<h2>Error</h2>
Includes all the current error handlers for the commands, in case something goes wrong when calling a command.
Example, a role-less user tries calling for the /kick command, the bot gives a reply, that the user does not have the required role for the command.

<h2>Test</h2>
These are project testing commands, that I change and run as I am learning how to implement new commands or new features into existing commands, in an attempt to not break the existing ones.

<h1>Conclusion</h1>
This bot will continue being updated with new features, as well as bug fixes, as people suggest new things to me.
Feel free to give your input or if you have any suggestions on how to make things better!

<h3>Bot Creation</h3>
All requirements found in the requirements.txt file.
Bunny Bot was developed in Python, with the hikari and lightbulb libraries. The Bot connects to a database through aiosqlite.

<h3>Running the bot</h3>
Running the bot requires a .env file with the discord token of your bot account, and the server ID of the servers you want it in.
Then just type "python bot.py" into the command line.
