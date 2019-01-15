import random
import asyncio
from discord.ext.commands import Bot 

BOT_PREFIX = (";", "/")
client = Bot(command_prefix=BOT_PREFIX)
client.remove_command("help")

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    await client.change_presence(game=discord.Game(name=';help'))

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers in which the bot is running:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)
			
token = os.environ.get("DISCORD_BOT_SECRET")
client.loop.create_task(list_servers())
client.run(token)
