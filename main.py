import random

BOT_PREFIX = (";", "/")
client = Bot(command_prefix=BOT_PREFIX)
client.remove_command("help")

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    await client.change_presence(game=discord.Game(name=';help'))

