import discord
from datetime import date
from passy import TOKEN

def calculate_matura():
    today = date.today()
    matura = date(2021, 5, 4)
    diff = str((matura - today))
    diff = diff.split(" ")[0]
    return diff

print(TOKEN)

client = discord.Client()

@client.event
async def on_ready():
    print(f"logged as {client}")

@client.event
async def on_message(message):
    print(client.user)
    if message.author == client.user:
        return
    if message.content.startswith("!strach"):
        mess = "Do matur pozostało ci " + calculate_matura() + " dni! Serdecznie zachęcam do przyklejenia tyłka do stołka!"
        await message.channel.send(mess)

print(calculate_matura())
client.run(TOKEN)

