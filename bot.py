import discord 
from dotenv import load_dotenv 
import os
from math import *
import random

# create intents
intents = discord.Intents.default()
intents.message_content = True

# read bot token from .env file
load_dotenv("TOKEN")
token = os.environ.get("TOKEN")

# create bot client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user.name} logged in")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("ᓚᘏᗢ"):
        cleanMsg = message.content[3:]
        await message.channel.send("hi...unfortunately :( *echo of" + (cleanMsg) + "*")
    if message.content.startswith("math(っ °Д °;)っ"): 
        cleanMsg = message.content[14:]
        await message.channel.send("hi...unfortunately :( *math is sad but here u go :( ' " + str(eval(cleanMsg)) + " ' *")
    elif message.content.startswith("magik（⊙ｏ⊙）"):
        magic_list = ["it is certain","it is decidely so","without a doubt","yes,definitely","you may rely on it","as i see it, yes","most likely","outlook is good","yes","signs point to yes","reply hazy, try again","ask again later","better not tell you now","cannot predict this now","concentrate and ask again","don't count on it","my reply is no","my sources say no","outlook is not so good","very doubtful"]
        cleanMsg = message.content[10:]
        await message.channel.send(str(random.choice(magic_list)))

# log in
client.run(token)