import discord, re

client = discord.Client()
tokenFile = open("token.txt", "r")
token = tokenFile.read().rstrip()

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    questionPresent = re.search(".* *([Hh][Oo]+[Ww]+)|([Ww][Hh]*[Aa]+[Tt]*) *.*",msg)

    if questionPresent:
        await message.channel.send('Watashi, ki ni narimasu!')
    
client.run(token)