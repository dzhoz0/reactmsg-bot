import discord
import os
from dotenv import load_dotenv
import random
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

# Initial file

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'Message from {message.author.id}: {message.content}')
    rnd = random.randint(0, 5)
    if rnd != 0:
        return

    # print(type(message.author.id))
    if message.author.id == 695503661748453387:
        await message.add_reaction('🌙')
    if message.author.id == 558299808947765250:
        print("zesty?")
        await message.add_reaction('🍔')
    if message.author.id == 856005046965633034:
        await message.add_reaction('🫐')

# Get token from .env and run client
load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
