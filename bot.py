import discord
from discord.ext import commands, tasks
import os
import csv
import random
from cmds import register_commands
from command_list import register_commands2
from dotenv import load_dotenv

load_dotenv()

BOTTOKEN = os.getenv('BOTTOKEN')

bot = commands.Bot()

register_commands(bot)
register_commands2(bot)

@tasks.loop(minutes=3)
async def loop():
    csv_file = open('vocab.csv', 'r')
    csv_reader = csv.reader(csv_file, delimiter=',')
    # pick a random line, excluding the header
    line = random.choice(list(csv_reader)[1:])
    first = f"你怎麼發音**{line[0]}**？\n||{line[1]}||"
    channel = bot.get_channel(1026731489959882765)
    await channel.send(first)

@bot.event
async def on_ready():
    print("走吧")
    loop.start()

bot.run(BOTTOKEN)