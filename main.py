import discord
import os

from constants import DISCORD_BOT_TOKEN
from keep_alive import keep_alive


client = discord.Client()   # Create a Discord Client to send commands to Discord's servers.

@client.event               #We are defining an event for our client.
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        await message.channel.send(message.content[::-1])

keep_alive()
token = DISCORD_BOT_TOKEN
client.run(token)