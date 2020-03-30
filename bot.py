import discord, re, random, json

client = discord.Client()

runFile = open("info.json", "r")
runInfo = json.loads(runFile.read().rstrip())

token = runInfo["token"]
supportedOsuBots = runInfo["bots"]

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif (message.author.id in supportedOsuBots) and (random.randint(0,10) <= 2):
        await message.channel.send('*We don’t know if trying our best will help, but we do know, that if we don’t try our best, it won’t help for sure!*')
        return

    msg = message.content
    questionPresent = re.search(r"\b(([Hh][Oo]+[Ww]+)|([Ww][Hh]*[Aa]+[Tt]+)|([Ww][Hh]+[Yy]+))\b",msg)
    uwu = re.search(r"\b([Uu]+[Ww]+[Uu]+)\b",msg)
    angry = re.search(r"\b([Rr][Ii]+[Pp]+ *([Ff][Cc]+)?|[Ff]+[Uu]+[Cc]*[Kk]* *([Mm]+[Ee]+)?|[Ff][Rr][Uu][Ss][Tt][Rr][Aa][Tt][Ii]+[Nn]+[Gg]+)\b",msg)
    dontGetIt = re.search(r"\b(([Dd][Oo][Nn]'?[Tt] +(([Gg][Ee][Tt] +[Ii]+[Tt]+)|([Uu][Nn][Dd][Ee][Rr][Ss][Tt][Aa]+[Nn]+[Dd]+)))|([Nn][Oo] +[Ss][Ee][Nn][Ss][Ee]))\b",msg)
    cold = re.search(r"\b([Cc]+[Oo]+[Ll]+[Dd]+)|([Ss]+[Aa]+[Mm]+[Uu]+[Ii]+)\b",msg)

    if angry or dontGetIt or cold:
        if angry:
            await message.channel.send('*If you can never get angry at anything, that probably means you have nothing that you like, either.*')
        elif dontGetIt:
            await message.channel.send('*I find myself hard to understand sometimes.*')
        elif cold:
            await message.channel.send('*Iie, mou haru desu.* :relaxed:')
    elif questionPresent:
        await message.channel.send('*Watashi, ki ni narimasu!* :astonished:')
    elif uwu:
        await message.channel.send(':flushed:')

client.run(token)
