import discord
import os
import requests
import json
from uptime import keep_alive
import random

client = discord.Client()

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n- " + json_data[0]['a']
    return (quote)

def get_html():
    things = ['CSS', 'lmth', 'Data Scientist', 'YouKnowWho', 'That guy!']
    word = random.choice(things)
    return word

def commands():
    return 'hello\narnold\nhtml'

commandlist = ["hello", "arnold", "html", "commands"]

@client.event
async def on_ready():
    print(f"Up and running.\n {client.user}")
    game = discord.Activity(name="Motivation", type=5)
    await client.change_presence(activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send(
            "Hello! I am a bot here to send you motivational quotes.")

    if message.content.startswith("$"):
        if len(message.content) == 1:
            await message.channel.send("Yes! That is my prefix.")
        elif message.content[1:] not in commandlist:
            await message.channel.send(
                "No such command exists.\nFor a list of comnands type '$commands'")

    if message.content.startswith("$arnold"):
        await message.channel.send(get_quote())

    if message.content.startswith("$html"):
        await message.channel.send(get_html())

    if message.content.startswith("$commands"):
        await message.channel.send(commands())

keep_alive()
client.run(os.getenv('TOKEN'))
