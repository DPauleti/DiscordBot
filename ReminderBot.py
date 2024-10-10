import os
import discord
import random
from dotenv import load_dotenv

load_dotenv() #Load .env file and extract bot token
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default() #Set bot intents
intents.members = True  #Allow bot to access server member information
intents.message_content = True #Allow the bot to view message contents

client = discord.Client(intents=intents)

@client.event
async def on_ready(): #When bot connects to discord
    guild = discord.utils.get(client.guilds, name=GUILD) #Get the name of the server specificied in the .env section

    print(
        f'{client.user} is connected to the following guild: \n' #Print the name of the server
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members]) #Get list of members connected to server
    print(f'Guild Members: \n - {members}') #Print list of members


@client.event
async def on_member_join(member): #When a new member joins the server
    await member.create_dm() 
    await member.dm_channel.send( #Send member a welcome DM
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    limbus_quotes = [
        "LIMBUS COMPANY!",
        "BEACH VOREYBURR!",
        "Danteh, go grind mirror dungeon Danteh",
        "Faust knows all outcomes",
        "The multitude tightens its hold",
    ]

    if "limbus" in message.content.lower():
        response = random.choice(limbus_quotes)
        await message.channel.send(response)

client.run(TOKEN)