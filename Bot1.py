# BOTTTTTTTTTTT
# CREATED BY RIBBET400
import discord
import random
from discord.ext import commands
import random
import json
#import requests

INFO = open('c:/Users/jackl/OneDrive/Documents/Coding/INFO.txt','r').read()
INFO = INFO.split('/')
TOKEN = INFO[0]
GUILD = INFO[1],INFO[2]

client = discord.Client()

@client.event
async def on_ready(): # WHEN CONNECTED
    await client.change_presence(status=discord.Status.online, activity=discord.Game('4D chess'))
    print(f'{client.user.name} has connected to Discord!')
    for guild in client.guilds:
        if guild.name in GUILD:
            print(
            f'\n{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
            )
            members = '\n - '.join([member.name for member in guild.members])
            print(f'Guild Members:\n - {members}')
    


@client.event
async def on_message(message): # RESPONDS TO MESSAGES
    if message.author == client.user: # PREVENTS LOOP
        return

    if 'hi' in message.content.lower() or 'hello' in message.content.lower():
        Greetings = ['Bonjour','Hola','Hi','Salutations','Greetings','Hello','Wagwan','Salve','Good afternoon','Hello child','Wassup','YO','Hey']
        response = random.choice(Greetings)
        await message.channel.send(response)

    if 'roadman' in message.content.lower():
        Roadman = ['Wagwan','safe 1 my G','init bruv','Dat grey ting be looking leg','Allow it fam','Ay blud','mandem','peng ting','wasteman']
        response = random.choice(Roadman)
        await message.channel.send(response)

    elif 'rickroll' in message.content.lower():
        await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be')

    elif message.content.lower() == 'github':
        await message.channel.send('https://github.com/Ribbet400')
        
    """elif message.content.lower() == 'frog': # INCREDIBLY INEFFICIENT AND CURRENTLY NOT WORKING
        try:
            res = requests.get('https://www.reddit.com/r/frogs/', headers={'User-Agent': 'Mozilla/5.0'})
            data = json.loads(res.text)['data']
            count = int(data['dist'])
            post = data['children'][random.randint(1, count)]['data']
            imageUrl = post['url_overridden_by_dest']
            title = post['title']
            image = discord.Embed(title=title)
            image.set_image(url=imageUrl)
            await message.channel.send(embed=image)
        except:
            await message.channel.send('no frog')"""
                        
    if message.content.lower().startswith("diss") or message.content.lower().startswith("Diss"):
        messageList = message.content.split()
        try:
            name = messageList[1]
        except IndexError:
            return
        if name.startswith('<@!'):
            print(name)
            if name == '<me' or name == 'bot':
                await message.channel.send('Get played')
                
            else:
                disses = ["the only letters of the alphabet you know are KFC.","out of 100,000 sperm, you were the fastest?","you'll never be the man your mother is.", "take that mask off, Halloween isn't until October"]
                response = random.choice(disses)
                answer = name+' '+response
                await message.channel.send(answer)




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