
import discord

INFO = open('c:/Users/jackl/OneDrive/Documents/Coding/INFO.txt','r').read()
INFO = INFO.split('/')
TOKEN = INFO[0]
GUILD = INFO[1]

client = discord.Client()





@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('BOT'))
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
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Bonjour {member.name}, bienvenue sur mon serveur!'
    )

client.run(TOKEN)