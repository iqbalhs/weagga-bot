import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

startup_extensions = ["Music"]
bot = commands.Bot("xD")

@bot.event
async def on_ready():
    print("bot online")
    print("Name " + bot.user.name)
    print("ID " + bot.user.id)

class Main_Commands():
        def __init__(self, bot):
            self.bot = bot

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("nahh, it's just your internet that sucks")


@bot.command(pass_context=True)
async def hello(ctx):
    if ctx.message.author.id == '282789892843634688':
        await bot.say("uwu")
    else:
        await bot.say("you're not Nue, go away")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = "{} : {}" . format(type(e) . __name__, e)
            print("Failed to load extension {}\n{}" . format(extension, exc))

bot.run("token")