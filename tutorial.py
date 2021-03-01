import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(f"logged as {client}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("dupa"):
        await message.channel.send("fuck off I'm sleeping")

client.run('')
