import discord
from datetime import datetime

client = discord.Client()

time_dict = {}

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.content.startswith('!start'):
        time_dict[message.author.id] = datetime.now()
        await message.channel.send(f"{message.author.mention}, ты начал отсчет времени.")

    if message.content.startswith('!stop'):
        if message.author.id in time_dict:
            time_spent = datetime.now() - time_dict[message.author.id]
            total_seconds = int(time_spent.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            await message.channel.send(f"{message.author.mention}, ты провел на сервере {hours} ч., {minutes} мин., {seconds} сек.")
            del time_dict[message.author.id]
        else:
            await message.channel.send(f"{message.author.mention}, ты еще не начал отсчет времени.")
client.run('ur token')