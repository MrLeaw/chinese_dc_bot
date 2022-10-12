import discord

#create a function that makes a list of commands
def register_commands2(bot):
    commands = []
    #import list from commandlist.txt
    with open("commandlist.txt", "r") as f:
        commands = f.read().splitlines()
        print(commands)

    @bot.slash_command(name="list")
    async def command_slash(ctx):
        await ctx.respond(",".join(commands))


#create a slash command called help that shows how to use the commands
#the command should be called /help + "command name"
#the command should show the command name, description, and usage
    @bot.slash_command(name="help")
    async def help_slash(ctx, command: str):
        #check if command is in commandlist.txt
        if command in commands:
            #if it is, open the file from commandusages folder and read the file
            with open("commandusages/"+ command + ".txt", "r") as f:
                await ctx.respond(f.read())
        else:
            await ctx.respond("Command not found")
        
    @bot.command()
    async def help2(ctx):
        embed = discord.Embed(
            title="Command Lists",
            description="How to use these commands",
            color=discord.Colour.blurple()
        )
        embed.set_author(name="Chinese Bot")

        await ctx.respond(embed=embed)