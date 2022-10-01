import hikari
import lightbulb

plugin = lightbulb.Plugin('Fun', 'A collection of random fun commands.')

# Welcome message for new members
@plugin.listener(hikari.MemberCreateEvent)
async def on_member_join(event: hikari.MemberCreateEvent):
    guild = event.get_guild()
    embed = hikari.Embed(title="User has joined the server.", description=f"Welcome to {guild.name}, <@{event.member.id}>!")
    embed.set_thumbnail("https://media.tenor.com/OoBQUN0NcuEAAAAd/loporrit-ff14.gif")
    embed.add_field(name="Hellos!", value=f"If you have any questions, please feel free to ask.", inline=True)
    embed.add_field(name="Information", value=f"Server Owner: <@{guild.owner_id}>, having {guild.member_count} members!")
    embed.set_footer(f"Bunny Bot is made exclusively for Milkingway Millennia♡!")
    embed.colour="#ff99ff"
    channel = guild.system_channel_id
    await event.app.rest.create_message(channel, embed=embed)

# Hellos, I'm a bunny!
@plugin.listener(hikari.GuildMessageCreateEvent)
async def hellos(event: hikari.GuildMessageCreateEvent) -> None:
    if event.author.is_bot:
        return
    else:
        # if 'hellos' in event.content or 'Hellos' in event.content:
        if event.content and "hellos" in event.content.lower():
            await event.app.rest.create_message(event.channel_id, "Hellos!")
        else:
            return

# Checks for bot response
@plugin.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx): 
    await ctx.respond('Pong! ૮₍ ˃ ᵕ ˂ ₎ა')

# Says hello to target user
@plugin.command
@lightbulb.option("user", "User to greet", hikari.User)
@lightbulb.command("hello", "Greets the specified user")
@lightbulb.implements(lightbulb.SlashCommand)
async def greet(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Hellos {ctx.options.user.mention}!")

def load(bot):
    bot.add_plugin(plugin)