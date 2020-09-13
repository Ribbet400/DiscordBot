# BOTTTTTTTTTTT
# CREATED BY RIBBET400
import discord
import random
from discord.ext import commands

INFO = open('c:/Users/jackl/OneDrive/Documents/Coding/INFO.txt','r').read()
INFO = INFO.split('/')
TOKEN = INFO[0]
GUILD = INFO[1]

client = discord.Client()

@client.event
async def on_ready(): # WHEN CONNECTED
    await client.change_presence(status=discord.Status.online, activity=discord.Game('4D chess'))
    print(f'{client.user.name} has connected to Discord!')
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message): # RESPONDS TO MESSAGES
    if message.author == client.user: # PREVENTS LOOP
        return

    Greetings = ['Bonjour','Hola','Hi','Salutations','Greetings','Hello']
    if message.content.lower() == 'hi' or message.content.lower() == 'hello':
        response = random.choice(Greetings)
        await message.channel.send(response)

    if message.content.lower() == 'rickroll':
        await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be')

    if message.content.lower() == 'github':
        await message.channel.send('https://github.com/Ribbet400')
        


@client.event
async def on_member_join(member): # WHEN MEMBERS JOIN
    await member.create_dm()
    await member.dm_channel.send(
        f'Bonjour {member.name}, bienvenue sur mon serveur! :thumbsup:'
    )

@client.event
async def on_member_remove(member): # WHEN MEMBERS LEAVE
    await member.create_dm()
    await member.dm_channel.send(
        f'Au revoir {member.name} :thumbsup:'
    )


client.run(TOKEN)