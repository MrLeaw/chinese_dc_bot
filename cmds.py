def register_commands(bot):
    @bot.slash_command(name="ping")
    async def first_slash(ctx):
        await ctx.respond("pong")