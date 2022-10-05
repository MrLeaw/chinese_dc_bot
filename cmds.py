users = []

def register_commands(bot):
    global users
    users = []
    @bot.slash_command(name="ping")
    async def first_slash(ctx):
        await ctx.send("pong")

    @bot.slash_command(name="echo")
    async def second_slash(ctx, message: str):
        await ctx.respond(message)

    @bot.slash_command(name="subscribe")
    async def third_slash(ctx):
        with open('users.txt', 'r') as f:
            c = f.read()
            if c.strip() == "":
                users = []
            else:
                users = [int(s) for s in c.split(';')]
        if not ctx.author.id in users:
            # read the file
            users.append(ctx.author.id)
            with open('users.txt', 'w') as f:
                f.write(";".join([str(i) for i in users]))
            await ctx.respond("Subscribed!")
        else:
            await ctx.respond("You're already subscribed!")

    @bot.slash_command(name="unsubscribe")
    async def unsubscribe(ctx):
        with open('users.txt', 'r') as f:
            c = f.read()
            if c.strip() == "":
                users = []
            else:
                users = [int(s) for s in c.split(';')]
        if ctx.author.id in users:
            # read the file
            users.remove(ctx.author.id)
            # save to file
            with open('users.txt', 'w') as f:
                f.write(";".join([str(i) for i in users]))
            await ctx.respond("Unsubscribed!")
        else:
            await ctx.respond("You're not subscribed!")
            
    print("Commands registered")