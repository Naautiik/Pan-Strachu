import discord
from discord.ext import tasks
from flask import Flask
from threading import Thread
from datetime import date
from passy import TOKEN
from time import sleep
# from server import keep_alive

def calculate_matura():
    today = date.today()
    matura = date(2021, 5, 4)
    diff = str((matura - today))
    diff = diff.split(" ")[0]
    return diff

client = discord.Client()

@client.event
async def on_ready():
    print(f"logged as {client}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith("!strach"):
        mess = "Do matur pozostało ci " + calculate_matura() + " dni! Serdecznie zachęcam do przyklejenia tyłka do stołka!"
        await message.channel.send(mess)
    if message.content.startswith("jestem "):
        if len(message.content) >= 7:
            mess = "Cześć " + message.content[6:].strip() + ", jestem Pan Strachu"
        await message.channel.send(mess)
    if message.content.lower() == "stelar to gej":
        await message.channel.send("Zgadzam się całym swym strasznym serduszkiem")

app = Flask('')

@app.route('/')
def home():
    return "Alive."

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@client.event
async def on_ready():
    change_status.start()
    print("ready!")

@tasks.loop(seconds=120)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = "płaczu maturzystów"))
    sleep(60)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = "błagań maturzystów"))

keep_alive()
client.run(TOKEN)

