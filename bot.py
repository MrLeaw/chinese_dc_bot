import discord
from discord.ext import commands
import os
from cmds import register_commands
from dotenv import load_dotenv

load_dotenv()

BOTTOKEN = os.getenv('BOTTOKEN')

bot = commands.Bot()

register_commands(bot)

bot.run(BOTTOKEN)