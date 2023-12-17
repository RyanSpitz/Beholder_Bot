# This example requires the 'message_content' intent.
import discord
import json
import spell

dnde = "https://api.open5e.com/v1/spells/?format=json"

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
    # If the bot sent the message ignore the message
    if message.author == client.user:
        return
    # If the message is our command symbol
    if message.content.startswith('$'):

        if message.content[1:] == 'hello':
            await message.channel.send('Hello!')

        elif message.content.startswith('$spell'):

            # Takes all input after '$spell ' then puts a dash in anyspaces
            spellName = message.content[7:].replace(' ', '-')
            # print(spellName)

            # Catch a bad request
            spell_data = spell.fetch_spell_data(spellName)
            if spell_data == None:
                await message.channel.send(message.content[7:] + " is not a valid spell name.")

            else:    
                spell_emded = spell.create_spell_Embed(spell_data)

                # Sends the embed to the channel that requested
                await message.channel.send(embed=spell_emded)

client.run(config["token"])