# create a command that returns pong when the user said ping
from discord.ext import commands
bot = commands.Bot(command_prefix='=')

@bot.command()
async def ping(ctx):
    # check if the message is ping
    # check if the user is a bot
    #if not, reply with pong
    if ctx.message.content == 'ping':
        if not ctx.author.bot:
            await ctx.send('pong')