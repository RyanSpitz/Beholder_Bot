# This example requires the 'message_content' intent.
import discord
import json

# Reads input for bot token from config file
with open('config.json', 'r') as file:
    config = json.load(file)
# print(config["token"])


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(config["token"])