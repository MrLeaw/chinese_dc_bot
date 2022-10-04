def register_commands(bot):
    @bot.slash_command(name="ping")
    async def first_slash(ctx):
        await ctx.respond("pong")

    @bot.slash_command(name="echo")
    async def second_slash(ctx, message: str):
        await ctx.respond(message)
