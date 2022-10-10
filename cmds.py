import database

def register_commands(bot):
    @bot.slash_command(name="ping")
    async def first_slash(ctx):
        await ctx.send("pong")

    @bot.slash_command(name="echo")
    async def second_slash(ctx, message: str):
        await ctx.respond(message)

    @bot.slash_command(name="subscribe")
    async def third_slash(ctx):
        if not database.user_exists(ctx.author.id):
            # read the file
            database.add_user(ctx.author.id)
            await ctx.respond("Subscribed!")
        else:
            await ctx.respond("You're already subscribed!")

    @bot.slash_command(name="unsubscribe")
    async def unsubscribe(ctx):
        if database.user_exists(ctx.author.id):
            database.delete_user(ctx.author.id)
            await ctx.respond("Unsubscribed!")
        else:
            await ctx.respond("You're not subscribed!")
            
    print("Commands registered")