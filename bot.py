import discord
from discord.ext import commands
import os
from commands import Commands
from dotenv import load_dotenv
load_dotenv()

BOTTOKEN = os.getenv('BOTTOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')



intents = discord.Intents.default()

client = MyClient(intents=intents)
client.run(BOTTOKEN)