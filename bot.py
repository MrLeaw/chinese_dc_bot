import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

BOTTOKEN = os.getenv('BOTTOKEN')

bot = commands.Bot()
@bot.slash_command(name="ping")
async def first_slash(ctx): 
    await ctx.respond("pong")

bot.run(BOTTOKEN)