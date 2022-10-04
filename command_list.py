#import list from commandlist.txt
with open("commandlist.txt", "r") as f:

#create a function that makes a list of commands
    def register_commands(bot):
        for line in f:
            command = line.strip()
            @bot.slash_command(name="list")
            async def command_slash(ctx):
                await ctx.respond(command)