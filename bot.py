import lightbulb
import hikari
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"]
GUILDS = int(os.environ["DEFAULT_GUILDS"])

bot = lightbulb.BotApp(
    token=TOKEN, 
    default_enabled_guilds=GUILDS,
    intents=hikari.Intents.ALL,
    help_slash_command=True
    )

lightbulb.help_command.DefaultHelpCommand(bot)

bot.load_extensions_from('./extensions')
if __name__ == "__main__":
    bot.run(
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(name='eating lettuce', type=5)
    )