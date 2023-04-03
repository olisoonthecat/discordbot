import discord 
from dotenv import load_dotenv 
import os
from math import *
import random
from discord.ext import commands

# create intents
intents = discord.Intents.default()
intents.message_content = True

# read bot token from .env file
load_dotenv("TOKEN")
token = os.environ.get("TOKEN")

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.command(help = "testing obv u dum dum ○|￣|_ =3")
async def test(ctx):
    await ctx.send("i want money gimme money ᕦ(ò_óˇ)ᕤ")

@bot.command(help = "echoes ur message (∪.∪ )...zzz")
async def echo(ctx, *, arg):
    await ctx.send("echo = ||" + arg + "|| *yw* ༼ つ ◕_◕ ༽つ")

@bot.command(help = "solves ur stupid math problems cus u a dum dum ┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻")
async def math(ctx, *, arg):
    await ctx.send("math is sucky but here " + str(eval(arg)) + " :sob:")

bot.run(token)