import hikari
import lightbulb
import datetime

plugin = lightbulb.Plugin('Moderation', 'Moderation commands requiring ADMIN permissions.')

# Prevents executing commands targeting the command caller
def not_on_self(func):
    async def wrapper(ctx):
        if ctx.options.user == ctx.author:
            await ctx.respond(f"You can't {func.name} yourself!")
            return
        await func(ctx)
    return wrapper

# Command for Kicking a user
@plugin.command
@lightbulb.add_checks(lightbulb.has_role_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option('user', 'User being kicked', type=hikari.User)
@lightbulb.command('kick', 'Kicks the user')
@lightbulb.implements(lightbulb.SlashCommand)
@not_on_self
async def kick(ctx):
    if not ctx.guild_id:
        await ctx.respond("This command can only be used in a server.")
        return   
    await ctx.bot.rest.kick_user(ctx.guild_id, ctx.options.user.id)
    await ctx.respond(f'<@{ctx.options.user.id}> was kicked from the server.')

# Command for banning a user
@plugin.command
@lightbulb.add_checks(lightbulb.has_role_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option('user', 'User being banned', type=hikari.User)
@lightbulb.command('ban', 'Bans the user')
@lightbulb.implements(lightbulb.SlashCommand)
@not_on_self
async def ban(ctx):
    if not ctx.guild_id:
        await ctx.respond("This command can only be used in a server.")
        return   
    await ctx.bot.rest.ban_user(ctx.guild_id, ctx.options.user.id)
    await ctx.respond(f'<@{ctx.options.user.id}> was banned from the server.')

# Purge command mostly taken from the hikari-lightbulb github page
@plugin.command
@lightbulb.add_checks(lightbulb.has_role_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("count", "Amount of messages to purge.", type=int, max_value=100, min_value=1)
@lightbulb.command("purge", "Purge a number of messages from a channel", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def purge(ctx: lightbulb.SlashContext, count: int) -> None:
    if not ctx.guild_id:
        await ctx.respond("This command can only be used in a server.")
        return
    messages = (
        await ctx.app.rest.fetch_messages(ctx.channel_id)
        .take_until(lambda m: datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=14) > m.created_at)
        .limit(count)
    )
    if messages:
        await ctx.app.rest.delete_messages(ctx.channel_id, messages)
        await ctx.respond(f"Purged {len(messages)} messages.")
    else:
        await ctx.respond("Could not find any messages younger than 14 days!")

def load(bot):
    bot.add_plugin(plugin)