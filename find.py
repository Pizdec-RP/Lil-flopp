# -*- coding: utf-8 -*-
import discord
import os, sys, ast, json, time, random, base64, subprocess, requests
from discord.ext import commands
from discord.utils import get
client = commands.Bot(command_prefix = '', selfbot = True, intents = discord.Intents.all())
token = sys.argv[1]
poisk = sys.argv[2]
webhook = sys.argv[3]

@client.event
async def on_ready():
    for guild in client.guilds:
        for member in guild.members:
            if int(member.id) == int(poisk):
                try:
                    channel = random.choice(guild.channels)
                    invite = channel.create_invite()
                    invite = invite.url
                except:
                    invite = 'не удалось создать инвайт'
                await webhook.send(content=f'```негр обнаружен на сервере: {guild.name}.приглос на сервер: {invite}. полный ник: {member}.```')
            else:
                pass
    
    await webhook.send(content='пожилое сканирование закончено')

client.run(token,bot=False)
