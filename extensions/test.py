import lightbulb
import hikari
import aiosqlite
import toolbox

plugin = lightbulb.Plugin('Test', 'Various commands to perform bot tests.')

# Embed command for testing various things
@plugin.command
@lightbulb.command('embed', 'Sends an embed in the channel')
@lightbulb.implements(lightbulb.SlashCommand)
async def embed_command(ctx: hikari.GuildEvent):
    guild = ctx.get_guild()
    embed = hikari.Embed(title="Title Example", description="Example of a description in the embed")
    embed.add_field(name="Hellos!", value=f"If you have any questions, please feel free to ask!", inline=True)
    embed.add_field(name="Information", value=f"The owner of the server is <@{guild.owner_id}>, with {guild.member_count} members!")
    embed.set_thumbnail("https://media.tenor.com/5RcczXcjF_MAAAAC/loporrit-ff14.gif")
    # embed.set_image("https://i.imgur.com/NectDaG.png")
    embed.set_footer(f"Bunny Bot is made exclusively for {guild.name}!")
    embed.colour="#ff99ff"
    await ctx.respond(embed)

# Testing the data command for accessing database
@plugin.command
@lightbulb.command('data', 'Testing database select and image response!')
@lightbulb.implements(lightbulb.SlashCommand)
async def data(ctx):
    db = await aiosqlite.connect('main.db')
    cursor = await db.execute('SELECT image FROM images WHERE image_id = ?', '2')
    await db.commit()
    db.text_factory = str
    row = await cursor.fetchall()
    await db.close()
    await ctx.respond(row[0][0])

# Testing for an image url and other stuffs
@plugin.command
@lightbulb.option('link', 'Link to test')
@lightbulb.command('url', 'Tests for a image url')
@lightbulb.implements(lightbulb.SlashCommand)
async def url(ctx):
    if toolbox.is_url(ctx.options.link) is False:
        await ctx.respond("Not a url")
        return
    elif ctx.options.link.endswith(('.png', '.jpg', '.jpeg')) is False:
        await ctx.respond("Not an image")
        return
    elif len(ctx.options.link) > 60:
        await ctx.respond("Too long")
        return
    else:
        await ctx.respond("Real url to an image!")

# Basic addition bot that I limited to nsfw channels for the sake of testing add_checks
@plugin.command
@lightbulb.add_checks(lightbulb.nsfw_channel_only)
@lightbulb.option('num2', 'Second number', type=int)
@lightbulb.option('num1', 'First number', type=int)
@lightbulb.command('add', 'Adds 2 numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

def load(bot):
    bot.add_plugin(plugin)