#create a function that makes a list of commands
def register_commands2(bot):
    commands = []
    #import list from commandlist.txt
    with open("commandlist.txt", "r") as f:
        commands = f.read().splitlines()
        print(commands)

    @bot.slash_command(name="list")
    async def command_slash(ctx):
        await ctx.respond("\n".join(commands))