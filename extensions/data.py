import hikari
import lightbulb
import random
import aiosqlite
import toolbox

plugin = lightbulb.Plugin('Data', 'Commands accessing the database.')

# Returns a random image of a bunny from the database
@plugin.command
@lightbulb.command('bunny', 'Gives you a random bunny!')
@lightbulb.implements(lightbulb.SlashCommand)
async def bunny(ctx):
    db = await aiosqlite.connect('main.db')
    nursor = await db.execute('SELECT COUNT(image_id) FROM images')
    num = await nursor.fetchall()
    n = random.randint(1, num[0][0])
    cursor = await db.execute('SELECT image, description FROM images WHERE image_id = ?', str(n))
    await db.commit()
    db.text_factory = str
    row = await cursor.fetchall()
    await db.close()
    embed = hikari.Embed(title="Random Bun!", description=row[0][1])
    embed.set_image(row[0][0])
    await ctx.respond(embed)

# Submit an image to the database
@plugin.command
@lightbulb.option('desc', 'Image description', type=str)
@lightbulb.option('img', 'Direct link to the image from imgur', type=str)
@lightbulb.command('submit', 'Submits a bunny image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def submit(ctx):
    if "SELECT" in ctx.options.img or "INSERT" in ctx.options.img or "DROP" in ctx.options.img or "CREATE" in ctx.options.img or "DELETE" in ctx.options.img:
        await ctx.respond("Invalid URL")
        return
    elif "SELECT" in ctx.options.desc or "INSERT" in ctx.options.desc or "DROP" in ctx.options.desc or "CREATE" in ctx.options.desc or "DELETE" in ctx.options.desc or ctx.options.desc is None:
        await ctx.respond("Invalid Description")
        return
    elif len(ctx.options.desc) > 35:
        await ctx.respond("Description too long.")
        return
    elif toolbox.is_url(ctx.options.img) is False:
        await ctx.respond("Not a URL")
        return
    elif ctx.options.img.endswith(('.png', '.jpg', '.jpeg')) is False:
        await ctx.respond("Not an image")
        return
    else:
        img = ctx.options.img
        desc = ctx.options.desc
        db = await aiosqlite.connect('main.db')
        await db.execute('INSERT INTO images (image, description) VALUES (?, ?)', (img, desc))
        await db.commit()
        await db.close()
        await ctx.respond("Submission added!")

def load(bot):
    bot.add_plugin(plugin)