# -*- coding: utf-8 -*-
import discord, random, time, json, requests, asyncio, sqlite3, subprocess, sys, os, asyncio, datetime, aiohttp#, lxml

import io
#import dns
from discord.ext import commands
from discord.utils import get
#import youtube_dl
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.parse import urlparse
from urllib.parse import parse_qs
from time import sleep
#from PIL import Image, ImageFont, ImageDraw
#from pymongo import MongoClient
#from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
rand = random.choice

#----------------------------------------------
client = commands.Bot(command_prefix = ';', intents = discord.Intents.all())
cluster = None#MongoClient("mongodb+srv://jopking:14881488@cluster0.steie.mongodb.net/testdata?retryWrites=true&w=majority")
db = None#cluster.testdata
collection = None#db.testcoll
client.remove_command('help')
#------------------------db for whitelist---------------//
wlt = sqlite3.connect('/p/whitelisted.db')
wlcursor = wlt.cursor()
wlcursor.execute("""CREATE TABLE IF NOT EXISTS pizdak(id INT, whitel TEXT)""")
wlt.commit()

def wladd(gid, userid):
    text = str(wlcursor.execute("SELECT whitel FROM pizdak WHERE id = {}".format(gid)).fetchone()[0])
    listof = str(text+f' {userid}')
    wlcursor.execute("UPDATE pizdak SET whitel = ? WHERE id = ?", (str(listof),gid))
    wlt.commit()
    
def wldel(gid, userid):
    text = str(wlcursor.execute("SELECT whitel FROM pizdak WHERE id = {}".format(gid)).fetchone()[0])
    listof = text.replace(' '+str(userid),'')
    wlcursor.execute("UPDATE pizdak SET whitel = ? WHERE id = ?", (str(listof),gid))
    wlt.commit()
    
def wlget(gid):
    text = str(wlcursor.execute("SELECT whitel FROM pizdak WHERE id = {}".format(gid)).fetchone()[0])
    listof = text.split(' ')
    return listof
    
class Keymanager():
    def f():
        return random.choice('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    def generate():
        return #str(Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+Keymanager.f()+)

iibase = sqlite3.connect('/p/iibas.db')
iicursor = iibase.cursor()
iicursor.execute("""CREATE TABLE IF NOT EXISTS iint(id INT, channels TEXT)""")
iibase.commit()

def iiadd(gid, channelid):
    text = str(iicursor.execute("SELECT channels FROM iint WHERE id = {}".format(gid)).fetchone()[0])
    listof = str(text+f' {channelid}')
    iicursor.execute("UPDATE iint SET channels = ? WHERE id = ?", (str(listof),gid))
    iibase.commit()

def iidel(gid, channelid):
    text = str(iicursor.execute("SELECT channels FROM iint WHERE id = {}".format(gid)).fetchone()[0])
    listof = text.replace(' '+str(channelid),'')
    iicursor.execute("UPDATE iint SET channels = ? WHERE id = ?", (str(listof),gid))
    iibase.commit()
    
def iiget(gid):
    text = str(iicursor.execute("SELECT channels FROM iint WHERE id = {}".format(gid)).fetchone()[0])
    listof = text.split(' ')
    return listof
    

#----------------------------------------------db1 sex----------------------------------------------
owner=['942517025908064358','855504661426470962','803789551692546060','762586990909587476','812726900518027314','826439777230258207','855504661426470962','855504661426470962']


conect = sqlite3.connect('/p/data.db')
cu = conect.cursor()
cu.execute("""CREATE TABLE IF NOT EXISTS guilds(id INT, channel INT, description TEXT, antispam INT, anticrash INT, clicks INT)""")
conect.commit()


#----------------------------------------------db2 - servers----------------------------------------------
connect = sqlite3.connect('/p/sdata.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS guilds(id INT, atime INT, amsg INT, muterole INT)""")
connect.commit()
#----------------------------------------------db3 - хз залупа какаято----------------------------------------------

gconnect = sqlite3.connect('/p/gamedata.db')
gcursor = gconnect.cursor()
gcursor.execute("""CREATE TABLE IF NOT EXISTS game(id INT, money INT, boost INT)""")
gconnect.commit()

conn = sqlite3.connect('/p/pizdec.db')
curs = conn.cursor()


aiconnect = sqlite3.connect('/p/aimemory.db')
aicursor = aiconnect.cursor()
aicursor.execute("""CREATE TABLE IF NOT EXISTS memory(tag INT, pattern TEXT, response TEXT)""")
aiconnect.commit()

def aigetresponse(user_message):
    word = str(random.choice(user_message.split(' ')))
    patterns = aicursor.execute("SELECT pattern FROM memory").fetchall()
    alist = []
    for pattern in patterns:
        if word in pattern:
            alist.append(pattern)
    frase = random.choice(alist)
    blocklist = "[ ] ( ) | ? , . / \ ! @ # $ % ^ & * - _ = +".split(' ')
    for block in blocklist:
        try:
            frase.replace(f'{block}','')
        except:
            pass
    response = aicursor.execute("SELECT response FROM memory WHERE pattern = ?", (str(frase))).fetchone()[0]
    return response
    
def aiadd(message1,message2):
    print(f'added pattern {message1}, response {message2}')
    aicursor.execute("INSERT INTO memory VALUES (?,?,?)", (str(random.randint(99,99999999)),message1,message2))
    aiconnect.commit()

global ni44er
ni44er = True
global working
working = False

for guild in client.guilds:
    global srvs
    srvs = []
    srvs.append(guild.id)
    print(guild.id)
     
@client.event
async def on_ready():
    print('25')
    await client.change_presence(status = discord.Status.online, activity = discord.Game('попытка включения....'))
    jopka = 0
    for guild in client.guilds:
        if wlcursor.execute("SELECT id FROM pizdak where id = {}".format(guild.id)).fetchone() is None:
            
            wlcursor.execute("INSERT INTO pizdak VALUES (?,?)", (guild.id,'812950760399962123'))
            print(f"[debug] created whitelist for {guild.id}")
            
        else:
            pass
        
        if iicursor.execute("SELECT id FROM iint where id = {}".format(guild.id)).fetchone() is None:
            
            iicursor.execute("INSERT INTO iint VALUES (?,?)", (guild.id,'812950760399962123'))
            print(f"[debug] created ii for {guild.id}")
            
        else:
            pass
        
        if cu.execute("SELECT id FROM guilds where id = {}".format(guild.id)).fetchone() is None:
            t = 'измените описание командой ;setdesc (text)'
            cu.execute("INSERT INTO guilds VALUES (?,?,?,?,?,?)", (guild.id,0,t,0,0,1))
            print(f"[debug] added srv {guild.id}")
        else:
            pass
        if cursor.execute("SELECT id FROM guilds where id = {}".format(guild.id)).fetchone() is None:
            cursor.execute("INSERT INTO guilds VALUES (?,?,?,?)", (guild.id,5,8,0))
            print(f"[debug] added srv {guild.id}")
        else:
            pass
        wlt.commit()
        conect.commit()
        connect.commit()
        iibase.commit()
        mb = 0
        for member in guild.members:
            mb += 1
            if gcursor.execute("SELECT id FROM game where id = {}".format(member.id)).fetchone() is None:
                gcursor.execute("INSERT INTO game VALUES (?,?,?)", (member.id,0,1))
                print(f"[debug] added {mb} member {member.id}")
            else:
                pass
            gconnect.commit()
            jopka += 1
            #if collection.count_documents({"id": member.id}) == 0:
            #    try:
            #        collection.insert_one(post)
            #        print('added user')
            #    except:
            #        pass
            #else:
            #    pass
    
    print('50')
    #subprocess.Popen(['python3','/p/mainfile.py'])
    print("old token started")
    #DiscordComponents(client)
    
    ver = discord.__version__
    total = 0
    memb = 0
    for guild in client.guilds:
        total += 1
        for member in guild.members:
            memb += 1
    print('75')
    await client.change_presence(status = discord.Status.online, activity = discord.Game(f';help | {total} серверов | участников {memb} | версия API {ver}'))
    #subprocess.Popen(['python3','/p/main.py'])
    #await os.system('java -Xmx900M -jar /root/server.jar')
    print('100\nready')
@client.event
async def on_guild_join(guild):
    cna = client.get_channel(865111751515177031)
    embed = discord.Embed(title='бота добавили на новый сервер',description='вот немного информации о нем',color = discord.Color.green())
    nm = guild.name
    huytebe = 'название скрыто изза ссылки или упоминания в нем'
    if '@everyone' in str(nm) or '@here' in str(nm):
        nm = huytebe
    elif '@' in str(nm) or 'https' in str(nm):
        nm = huytebe
    elif '://' in str(nm) or 'discord/gg' in str(nm):
        nm = huytebe
    elif 'discord.com' in str(nm):
        nm = huytebe
    else:
        pass
    embed.add_field(name='название', value = f'{nm}', inline = True)
    embed.add_field(name=f"дата создания:", value=f"""{guild.created_at.strftime("%A, %B %d %Y")}""", inline = True)
    embed.add_field(name="владелец", value=f"{guild.owner}", inline = True)
    embed.add_field(name="кол-во участников", value=f"{guild.member_count}", inline = True)
    embed.add_field(name='id',value = f'{guild.id}', inline = True)
    await cna.send(embed=embed)

    for guild in client.guilds:
        if wlcursor.execute("SELECT id FROM pizdak where id = {}".format(guild.id)).fetchone() is None:
            t = 'измените описание командой ;setdesc (text)'
            wlcursor.execute("INSERT INTO pizdak VALUES (?,?)", (guild.id,str('812950760399962123')))
            print(f"[debug] created whitelist for {guild.id}")
            
        else:
            pass
        
        if iicursor.execute("SELECT id FROM iint where id = {}".format(guild.id)).fetchone() is None:
            
            iicursor.execute("INSERT INTO iint VALUES (?,?)", (guild.id,'812950760399962123'))
            print(f"[debug] created ii for {guild.id}")
            
        else:
            pass
        
        if cu.execute("SELECT id FROM guilds where id = {}".format(guild.id)).fetchone() is None:
            t = 'измените описание командой ;setdesc (text)'
            cu.execute("INSERT INTO guilds VALUES (?,?,?,?,?,?)", (guild.id,0,t,0,0,0))
            print(f"[debug] added srv {guild.id}")
        else:
            pass
        if cursor.execute("SELECT id FROM guilds where id = {}".format(guild.id)).fetchone() is None:
            cursor.execute("INSERT INTO guilds VALUES (?,?,?,?)", (guild.id,5,8,0))
            print(f"[debug] added srv {guild.id}")
        else:
            pass
        for member in guild.members:
            
            if gcursor.execute("SELECT id FROM game where id = {}".format(member.id)).fetchone() is None:
                gcursor.execute("INSERT INTO game VALUES (?,?,?)", (member.id,0,1))
                print(f"[debug] added member {member.id}")
            else:
                pass
        gconnect.commit()
    wlt.commit()
    conect.commit()
    connect.commit()
    iibase.commit()
    ver = discord.__version__
    total = 0
    memb = 0
    for guild in client.guilds:
        total += 1
        for member in guild.members:
            memb += 1
    await client.change_presence(status = discord.Status.online, activity = discord.Game(f';help | {total} серверов | участников {memb} | версия API {ver}'))
    
   
@client.event
async def on_guild_remove(guild):
    guilda = guild
    ver = discord.__version__
    total = 0
    memb = 0
    for guild in client.guilds:
        total += 1
        for member in guild.members:
            memb += 1
    await client.change_presence(status = discord.Status.online, activity = discord.Game(f';help | {total} серверов | участников {memb} | версия API {ver}'))
    
    cna = client.get_channel(865111751515177031)
    embed = discord.Embed(title='бот удален с сервера',color = discord.Color.red())
    nm = guilda.name
    huytebe = 'название скрыто изза ссылки или упоминания в нем'
    if '@everyone' in str(nm) or '@here' in str(nm):
        nm = huytebe
    elif '@' in str(nm) or 'https' in str(nm):
        nm = huytebe
    elif '://' in str(nm) or 'discord/gg' in str(nm):
        nm = huytebe
    elif 'discord.com' in str(nm):
        nm = huytebe
    else:
        pass
    embed.add_field(name='название', value = f'{nm}', inline = True)
    embed.add_field(name="владелец", value=f"{guilda.owner}", inline = True)
    embed.add_field(name='id',value = f'{guilda.id}', inline = True)
    await cna.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def anticrash(ctx,arg=None):
    if arg == None:
        await ctx.send("правильное использoвание команды ;anticrash (on/off)")
    elif arg == 'on':
        cu.execute("UPDATE guilds SET anticrash = ? WHERE id = ?", (1,ctx.guild.id))
        conect.commit()
        await ctx.message.add_reaction('✅')
        await ctx.send('защита включена')
    elif arg == 'off':
        cu.execute("UPDATE guilds SET anticrash = ? WHERE id = ?", (0,ctx.guild.id))
        conect.commit()
        await ctx.message.add_reaction('✅')
        await ctx.send('защита выключена')
    else:
        await ctx.send('неизвестный аргумент')
        
@client.command()
@commands.has_permissions(administrator=True)
async def antispam(ctx,arg=None):
    if arg == None:
        await ctx.send("правильное использoвание команды ;antispam (on/off)")
    elif arg == 'on':
        cu.execute("UPDATE guilds SET antispam = ? WHERE id = ?", (1,ctx.guild.id))
        conect.commit()
        await ctx.message.add_reaction('✅')
        await ctx.send('защита включена')
    elif arg == 'off':
        cu.execute("UPDATE guilds SET antispam = ? WHERE id = ?", (0,ctx.guild.id))
        conect.commit()
        await ctx.message.add_reaction('✅')
        await ctx.send('защита выключена')
    else:
        await ctx.send('неизвестный аргумент')
        
        
@client.command()
async def dbadd(ctx,member = None):
    if member == None:
        await ctx.send('укажите пользователя')
    else:
        try:
            cursor.execute(f'INSERT INTO users VALUES ({member.id},{member.id})')
            connection.commit()
            await ctx.send('информация обновлена')
        except:
            await ctx.send('автор бота дебил нихуя не настроил')

#@client.event
#async def on_invite_create(invite: discord.Invite):
#    server = invite.guild
#    channel = int(server.system_channel.id)
#    embed = discord.Embed(color=discord.Color.green(), description=f'**Создано приглашения**')
#    embed.add_field(name='Код инвайта: ', value=invite.code, inline=False)
#    embed.add_field(name='Максимально использаваний: ', value=invite.max_uses, inline=False)
#    embed.add_field(name='айди инвайта: ', value=invite.id, inline=False)
#    embed.add_field(name='автор инвайта: ', value=invite.inviter, inline=False)
#    await channel.send(embed=embed)

@client.command(aliases = ['mcach','ac','achivement'],pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def __ac(ctx, *, name:str = None):
    if name is None:
        embed = discord.Embed(title="Ошибка", description="Укажи название ачивки", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        a = random.randint(1, 40)
        name2 = name.replace(' ', '+')
        url = f'https://minecraftskinstealer.com/achievement/{a}/Achievement+Get%21/{name2}'
        emb = discord.Embed(description = f'**[Achievement!]({url})**',color = 0xe00055)
        emb.set_image(url = url)
        await ctx.send(embed=emb)

@client.command(aliases=['голосование', 'quickpoll','poll'],pass_context=True)
@commands.has_permissions(manage_messages=True)
async def __poll(ctx, *, question=None):
    if question is None:
        embed = discord.Embed(title="Ошибка", description="Укажите тему голосования", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Голосование", description=f"{question}\n🟩 - Да\n🟥 - Нет", color=discord.Color.green())
        bruh = await ctx.send(embed=embed)
        await bruh.add_reaction("🟩")
        await bruh.add_reaction("🟥")

@client.command(pass_context=True)
async def userinfo(ctx, member:discord.Member = None):
    if member is None:
        member = ctx.author
    else:
        pass
    comp = 0
    roles = [role for role in member.roles]
    embed = discord.Embed(title = f"информация о пользователе - {member}", color=0x5500ff)
    try:
        embed.set_thumbnail(url = member.avatar_url)
        comp += 1
    except:
        pass
    try:
        embed.add_field(name = "Айди", value = member.id )
        comp += 1
    except:
        pass
    try:
        embed.add_field(name = "Ник", value = member.display_name )
        comp += 1
    except:
        pass
#    embed.add_field(name = "Информация:", value = inn )
    try:
        embed.add_field(name = "Был зареган: ", value = member.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p") )
        comp += 1
    except:
        pass
    try:
        embed.add_field(name = "Зашел на сервер:", value = member.joined_at.strftime("%a, %#d, %B, %Y, %I:%M %p") )
        comp += 1
    except:
        pass
    try:
        embed.add_field(name = "Содержимое статуса:", value = member.activity )
        embed.add_field(name = "Активность:", value = member.status)
    except:
        pass
    try:
        embed.add_field(name = "Наивысшая роль:", value = member.top_role.mention )
        comp += 1
    except:
        pass
    if int(comp) <= 2:
        embed=discord.Embed(title="ошибка",description="немогу получить инфу о пользователе")
    else:
        pass
        
    await ctx.send( embed = embed )

@client.command()
async def ip( ctx, arg=None ):
    if arg == None:
        embed = discord.Embed(title="Ошибка", description="Укажи ip рядом с командой", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        try:
            response = requests.get( f'https://ipwhois.app/json/{ arg }' )
     
            user_ip = response.json()[ 'ip' ]
            user_continent = response.json()[ 'continent' ]
            user_city = response.json()[ 'city' ]
            user_code = response.json()[ 'country_code' ]
            user_flag = response.json()[ 'country_flag' ]
            user_stol = response.json()[ 'country_capital' ]
            user_codep = response.json()[ 'country_phone' ]
            user_region = response.json()[ 'region' ]
            user_country = response.json()[ 'country' ]
            user_time = response.json()[ 'timezone_gmt' ]
            user_val = response.json()[ 'currency' ]
            user_val_s = response.json()[ 'currency_code' ]
            user_org = response.json()[ 'org' ]
            user_timezone = response.json()[ 'timezone' ]
 
            global all_info
            all_info = f'\nIP : { user_ip }\nГород : { user_city }\nРегион : { user_region }\nСтолица страны : { user_stol }\nКод телефона : { user_codep }\nКод страны : { user_code }\nСтрана : { user_country }\nВалюта : { user_val }\nВалюта (короткая) : { user_val_s }\nПровайдер : { user_org }\nЗона : { user_timezone }'

            embed = discord.Embed(title = 'IP инфо', description = f'{ all_info }')
            await ctx.send(embed=embed)
        except:
            await ctx.send(embed=discord.Embed(title="ошибочка",description="возможно неверно введен ip"))

@client.command()
async def ping(ctx):
    ping = client.latency
    ping_emoji = "🟩🔳🔳🔳🔳"
    ping_list = [
        {"ping": 0.10000000000000000, "emoji": "🟧🟩🔳🔳🔳"},
        {"ping": 0.15000000000000000, "emoji": "🟥🟧🟩🔳🔳"},
        {"ping": 0.20000000000000000, "emoji": "🟥🟥🟧🟩🔳"},
        {"ping": 0.25000000000000000, "emoji": "🟥🟥🟥🟧🟩"},
        {"ping": 0.30000000000000000, "emoji": "🟥🟥🟥🟥🟧"},
        {"ping": 0.35000000000000000, "emoji": "🟥🟥🟥🟥🟥"}]
    for ping_one in ping_list:
        if ping > ping_one["ping"]:
            ping_emoji = ping_one["emoji"]
            break
    message = await ctx.send("чичас...")
    await message.edit(content = f" {ping_emoji} `{ping * 1000:.0f}ms`")
        

@client.command()
async def info(ctx, *, query: str = None):
    if query is None:
        embed = discord.Embed(title="Ошибка", description="укажите запрос", color=discord.Color.red())
        await ctx.send(embed=embed)
    elif len(query) > 50:
        embed = discord.Embed(title="Ошибка", description="неверный запрос", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        msg = await ctx.send("Чичиас...")
        sea = requests.get(
        ('https://ru.wikipedia.org//w/api.php?action=query'
         '&format=json&list=search&utf8=1&srsearch={}&srlimit=5&srprop='
        ).format(query)).json()['query']

        if sea['searchinfo']['totalhits'] == 0:
            await ctx.send(f'По запросу **"{query}"** ничего не найдено :confused:')
        else:
            for x in range(len(sea['search'])):
                article = sea['search'][x]['title']
                req = requests.get('https://ru.wikipedia.org//w/api.php?action=query'
                                   '&utf8=1&redirects&format=json&prop=info|images'
                                   '&inprop=url&titles={}'.format(article)).json()['query']['pages']
                if str(list(req)[0]) != "-1":
                    break
            article = req[list(req)[0]]['title']
            arturl = req[list(req)[0]]['fullurl']
            artdesc = requests.get('https://ru.wikipedia.org/api/rest_v1/page/summary/' + article).json()['extract']
            embed = discord.Embed(title = article, url = arturl, description = artdesc, color = 0x00ffff)
            embed.set_author(name = 'Google | Википедия', url = 'https://en.wikipedia.org/', icon_url = 'https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')

            await msg.delete()
            await ctx.send(embed = embed)

@client.command()
async def yt(ctx, *, query: str):
    if len(query) >= 101:
        embed = discord.Embed(title="Ошибка", description="слишком длинный запрос", color=discord.Color.red())
        await ctx.send(embed=embed)
    elif query is None:
        embed = discord.Embed(title="Ошибка", description="Укажи запрос", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        try:
            req = requests.get(
                ('https://www.googleapis.com/youtube/v3/search?part=id&maxResults=1'
                '&order=relevance&q={}&relevanceLanguage=en&safeSearch=moderate&type=video'
                '&videoDimension=2d&fields=items%2Fid%2FvideoId&key=')
                .format(query) + "AIzaSyC_viihkRiUg3N5bv0DRvOrmaNdUNJ852U")
            await ctx.send('https://www.youtube.com/watch?v={}'.format(req.json()['items'][0]['id']['videoId']))
        except:
            embed = discord.Embed(title="Ошибка", description=f"по запросу {query} ничего небыло найдено", color=discord.Color.red())
            await ctx.send(embed=embed)
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def idea(ctx, *, idea=None):
    if idea is None:
        embed = discord.Embed(title="Ошибка", description="Укажите идею `;idea <text>`", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        member = await client.fetch_user(user_id=855504661426470962)
        embed = discord.Embed(title="Новая Идея!", description=f"**Отправитель:\n**{ctx.author}\n**Айди:**\n{ctx.author.id}\n**Идея:**\n{idea}\nchannel: {ctx.channel.id}", color=discord.Color.green())
        await member.send(embed=embed)
        embed2 = discord.Embed(title="Успешно!", description=f"Идея была успешно отправлена создатаелю\n**Содержимое:**\n{idea}", color=discord.Color.green())
        await ctx.send(embed=embed2)

async def gamedef(ctx, text):
    member = ctx.author
    def check1(reaction, user):
        return user == member and reaction.emoji in '1️⃣2️⃣✅❌:'
    try:
        reaction, user = await client.wait_for('reaction_add', check = check1, timeout = 100)
    except asyncio.TimeoutError:
        return asyncio.TimeoutError
    


@client.command()
async def game(ctx, gameid=None):
    if gameid is None:
        await ctx.send('укажите айди игры (например ";game 1", всего игр 2)')
        return
    else:
        pass
    try:
        gameid = int(gameid)
        if gameid in [1,2]:
            pass
        else:
            return
    except:
        await ctx.send('неверно указан id игры')
        return
    member = (ctx.author)
    author = (ctx.author.id)
    Block = []
    if gameid == 1:
        if author in Block:
            embed = discord.Embed(title=f'{ctx.author} вам запрещено пользоваться этой командой', color=0xff0000)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
        else:  
            embed1 = discord.Embed(title = f'{ctx.author.name} начать игру ?',color = 0xac00ff)
            check_h = await ctx.send(embed = embed1)
            await check_h.add_reaction('✅')
            await check_h.add_reaction('❌')
        def check1(reaction, user):
            return user == member and reaction.emoji in '✅❌:'
        try:
            reaction, user = await client.wait_for('reaction_add', check = check1, timeout = 100)
        except asyncio.TimeoutError:
            embed3 = discord.Embed(title = f'{ctx.author.name} начать игру ?', description = 'Время вышло',color = 0xff0000)
            embed3.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await check_h.edit(embed = embed3)
            return
        if reaction.emoji == '❌':
            embed = discord.Embed(title = 'А жаль',color = 0xff0000)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed = embed)
        
        if reaction.emoji == '✅':
            embed = discord.Embed(title = f'Вы проснулись на космическом корабле, ничего не понимаете, ваши действия?\nНажмите 1 чтобы связаться с Землёй, 2 чтобы осмотреть корабль',color = 0x0000ff)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer1 = await ctx.send(embed = embed)
            await answer1.add_reaction('1️⃣')
            await answer1.add_reaction('2️⃣')      
        def check2(reaction, user):
            return user == member and reaction.emoji in '1️⃣2️⃣:'
        try:
            reaction, user = await client.wait_for('reaction_add', check = check2, timeout = 100)
        except asyncio.TimeoutError:
            embed3 = discord.Embed(title = f'Вы проснулись на космическом корабле, ничего не понимаете, ваши действия?\nНажмите 1 чтобы связаться с Землёй, 2 чтобы осмотреть корабль', description = 'Время вышло',color = 0xff0000)
            embed3.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await answer1.edit(embed = embed3)
            return
        if reaction.emoji == '1️⃣':     
            embed = discord.Embed(title = f'Земля не отвечает, в эфире помехи и чья-то ругань...\nНажмите 1 чтобы подать сигнал SOS, 2 чтобы нажать большую красную кнопку на пульте',color = 0xac00ff)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer = await ctx.send(embed = embed)
            await answer.add_reaction('1️⃣')
            await answer.add_reaction('2️⃣')        
        if reaction.emoji == '2️⃣':
            embed = discord.Embed(title = 'Все каюты на корабле пусты, вы один, и не умеете управлять кораблём\nНажмите ✅ чтобы попробовать включить автопилот, ❌ чтобы подать сигнал SOS',color = 0xac00ff)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer4 = await ctx.send(embed = embed)
            await answer4.add_reaction('✅')
            await answer4.add_reaction('❌')  
        def check3(reaction, user):
            return user == member and reaction.emoji in '1️⃣2️⃣✅❌:'
        try:
            reaction, user = await client.wait_for('reaction_add', check = check3, timeout = 100)
        except asyncio.TimeoutError:
            embed3 = discord.Embed(title = f'Земля не отвечает, в эфире помехи и чья-то ругань...\nНажмите 1 чтобы подать сигнал SOS, 2 чтобы нажать большую красную кнопку на пульте', description = 'Время вышло',color = 0xff0000)
            embed3.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await answer.edit(embed = embed3)
            return
        if reaction.emoji == '1️⃣':     
            embed = discord.Embed(title = f'После долгого ожидания, ваш сигнал был услышан, и за вами послали команду спасения.',color = 0x00ff00)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer = await ctx.send(embed = embed)       
        if reaction.emoji == '2️⃣':
            embed = discord.Embed(title = 'После нажатия кнопки на Землю была сброшена кварковая бомба, вы случайно уничтожили родную планету, и застрелились, поняв это.',color = 0xff0000)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer = await ctx.send(embed = embed) 
        if reaction.emoji == '✅':     
            embed = discord.Embed(title = f'После включения автопилота, вы стартовали в неизвестном направлении, и вскоре умерли от голода, не обнаружив на борту ничего съестного.',color = 0xff0000)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer = await ctx.send(embed = embed)      
        if reaction.emoji == '❌':
            embed = discord.Embed(title = 'После долгого ожидания, ваш сигнал был услышан, и за вами послали команду спасения.',color = 0x00ff00)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer = await ctx.send(embed = embed)
    #----------------------------------------------------------------
    elif gameid == 2:
    #----------------------------------------------------------------
        if author in Block:
            embed = discord.Embed(title=f'{ctx.author} вам запрещено пользоваться этой командой', color=0xff0000)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
        else:  
            embed1 = discord.Embed(title = f'{ctx.author.name} начать игру ?',color = 0xac00ff)
            check_h = await ctx.send(embed = embed1)
            await check_h.add_reaction('✅')
            await check_h.add_reaction('❌')
        def check1(reaction, user):
            return user == member and reaction.emoji in '✅❌:'
        try:
            reaction, user = await client.wait_for('reaction_add', check = check1, timeout = 100)
        except asyncio.TimeoutError:
            embed3 = discord.Embed(title = f'{ctx.author.name} начать игру ?', description = 'Время вышло',color = 0xff0000)
            embed3.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await check_h.edit(embed = embed3)
            return
        if reaction.emoji == '❌':
            embed = discord.Embed(title = 'А жаль',color = 0xff0000)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed = embed)
        
        if reaction.emoji == '✅':
            embed = discord.Embed(title = f'Вы нашли вещь хуже, чем «Тетрадь смерти». Долговая записка. Вы пишете, кто должен кому сколько денег и когда это должно быть выплачено. Иначе, они умирают от сердечного приступа.\n1 - выписать долг путину, 2 - испытать ее на своем лучшем друге',color = 0x0000ff)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer1 = await ctx.send(embed = embed)
            await answer1.add_reaction('1️⃣')
            await answer1.add_reaction('2️⃣')      
        def check2(reaction, user):
            return user == member and reaction.emoji in '1️⃣2️⃣:'
        try:
            reaction, user = await client.wait_for('reaction_add', check = check2, timeout = 100)
        except asyncio.TimeoutError:
            embed3 = discord.Embed(title = f'Timeout error', description = 'Время вышло',color = 0xff0000)
            embed3.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await answer1.edit(embed = embed3)
            return
        if reaction.emoji == '1️⃣':     
            embed11 =discord.Embed(title=f'вы выписали долг путину 148822854271337руб до завтра и благополучно легли спать. на следующий день вы проснулись от криков на улице. вы выглянули в окно. всюду была разруха: разбитые машины, горящие мусорки.вы ключили телевизор.')
            embed22 = discord.Embed(title = f'там вы услышали о том что вы разыскиваетесь за убийство бога. вы заметили под окнами мигалки\n1 - попытаться убежать через выход на крышу дома, 2 - отстреливаться батиным дробашом',color = 0xac00ff)
            embed22.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed = embed11)
            answer = await ctx.send(embed = embed22)
            await answer.add_reaction('1️⃣')
            await answer.add_reaction('2️⃣')        
        if reaction.emoji == '2️⃣':
            embed = discord.Embed(title = 'вы выписали долг другу и на следующий день он его выплатил вам. он не смог рассказать зачем он это сделал.\n✅ - выписывать долги всем подряд, ❌ - рассказать полиции о вашей находке',color = 0xac00ff)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer4 = await ctx.send(embed = embed)
            await answer4.add_reaction('✅')
            await answer4.add_reaction('❌')  
        def check3(reaction, user):
            return user == member and reaction.emoji in '1️⃣2️⃣✅❌:'
        try:
            reaction, user = await client.wait_for('reaction_add', check = check3, timeout = 100)
        except asyncio.TimeoutError:
            embed3 = discord.Embed(title = f'Timeout error', description = 'Время вышло',color = 0xff0000)
            embed3.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await answer.edit(embed = embed3)
            return
        if reaction.emoji == '1️⃣':     
            embed = discord.Embed(title = f'вы выбежали на крышу и побежали вдоль улицы. прыгая с одной крыши дома на другу. над собой вы вдруг услышали какието звуки. вы обернулись и последнее что вы увидели - направленная на вас пушка. после этого вы проснулись в своей кровати',color = 0x00ff00)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer = await ctx.send(embed = embed)       
        if reaction.emoji == '2️⃣':
            embed = discord.Embed(title = 'вы даже не умеете стрелять, поэтому при первой же попытке выстрелить вас откинуло назад сильной отдачей. вы уебались головой об стену и вырубились. после очнулись в своей кровати',color = 0xff0000)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer = await ctx.send(embed = embed) 
        if reaction.emoji == '✅':     
            embed = discord.Embed(title = f'вы усердно начали выписывать долги каждому встречному. к вам на счет начали поступать большие суммы. через пол часа к вам домой пришла налоговая инспекция, вас без разбирательств повязали и повезли на зону. там вас отпетушили и вы проснулись от боли в очке',color = 0xff0000)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer = await ctx.send(embed = embed)      
        if reaction.emoji == '❌':
            embed = discord.Embed(title = 'Полиция приняла вас за сумашедшего и увезла в дурку. от неожидонности вы проснулись',color = 0x00ff00)
            embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            answer = await ctx.send(embed = embed)
    else:
        await ctx.send('неверно указан id игры')
@client.command()
async def join(ctx):
    global voice
    channel=ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@client.command()
async def leave(ctx):
    channel=ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()

@client.command(aliases=['clear','cl','cln','clr'])
@commands.has_permissions(manage_messages=True)
async def __cl(ctx, amount = None):
    if amount is None:
        embed = discord.Embed(title="Ошибка", description="Укажи количество", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        amount = str(amount)
        amount = int(amount)
        if amount < 1:
            if amount == 0:
                await ctx.send("мм серьезно. ну ок, допустим я очистил 0 сообщений, чето поменялось?")
            else:
                await ctx.send("ээээ отрицательное число? я типо щас должен отправиться в будующее и вернуть оттуда сообщения или как ты себе это представляешь")
        else:
            if amount <= 10001:
                await ctx.channel.purge(limit = amount)
                msg = await ctx.send(f'очищено {amount} сообщ.')
                
            else:
                msg = await ctx.send('больше 10000 нельзя')
                await asyncio.sleep(4)
                await msg.delete()
@client.command(pass_context=True)
async def acl(ctx, amount = 1000):
    if str(ctx.message.author.id) in owner:
        await ctx.channel.purge(limit = amount)
        msg = await ctx.send(f'очистили {amount} сообщ.')
        await asyncio.sleep(4)
        await msg.delete()
    else:
        await ctx.send('нема прав')

@client.command(pass_context=True,aliases=['urlb','url'])
async def urlb__(ctx):
    await ctx.send(f'вот ссылка на добавление ботецкого https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot')

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def hack(ctx,*,text=None):
    if text is None:
        await ctx.send("и где цель?")
        hack.reset_cooldown(ctx)
    elif '@everyone' in text or '@here' in text:
        await ctx.send('попингуй')
        hack.reset_cooldown(ctx)
    else:
        
        count = random.randint(200,1500)
        msg = await ctx.send(f'пытаемся взломать {text}')
        await asyncio.sleep(2.5)
        await msg.edit(content = f'процесс взлома жопы {text} начат')
        await asyncio.sleep(2.5)
        await msg.edit(content = f'жопа взломана, достаем айпи адрес')
        await asyncio.sleep(2.5)
        await msg.edit(content = f'айпи адрес {text} получен (228.148.854.27:1337). получаем геоданные')
        await asyncio.sleep(2.5)
        await msg.edit(content= f'получены геоданные {text}. высылаем туда оффников')
        await asyncio.sleep(2.5)
        await msg.edit(content='оффники уже в пути, а теперь займемся его бравл аккаунтом')
        await asyncio.sleep(2.5)
        await msg.edit(content=f'найден аккаунт с почтой dibiloid123@gmail.com пароль: 1488228')
        await asyncio.sleep(2.5)
        await msg.edit(content='выкачиваем гемы и тырим скины...')
        await asyncio.sleep(2.5)
        await msg.edit(content='репортим на твой акк за наружешие discord ToS')
        await asyncio.sleep(2.5)
        await msg.edit(content=f'взлом окончен, ты продал инфу о {text} в даркнете и получил за это {count} рублей')
        #curs.execute("UPDATE userss SET cash = cash + {} WHERE id = {}".format(count,ctx.author.id))
        #conn.commit()

@client.command(pass_context=True)
async def getsyschannel(ctx):
    if str(ctx.message.author.id) in owner:
        server = ctx.message.guild
        chan = server.system_channel
        await ctx.send(f'системный канал: {chan}')
        chanid = server.system_channel.id
        await ctx.send(f'его айди: {chanid}')
    else:
        await ctx.send('```\nупсс... тебе такое недоступно\n```')
@client.command()
async def getsrvmembers(ctx):
    if str(ctx.message.author.id) in owner:
        for member in ctx.guild.members:
            await ctx.send(member)
    else:
        await ctx.send('упсс... тебе такое недоступно')
@client.command()
async def setchan(ctx,*, text):
    if str(ctx.message.author.id) in owner:
        global chan
        chan = int(text)
        await ctx.send(f'установлен канал {text}')
        await ctx.send(client.get_channel(chan))
    else:
        await ctx.send('упсс... тебе такое недоступно')
        
@client.command()
async def cchan(ctx,chan,name):
    chan = client.get_channel(chan)
    gid = chan.guild
    await gid.create_text_channel(name)
@client.command()
async def sch(ctx,*, text):
    if str(ctx.message.author.id) in owner:
        channel = client.get_channel(chan)
        global msgee
        try:
            url = file.url
            url = str(url)
            msgee = await channel.send(url)
        except:
            msgee = await channel.send(text)
    else:
        await ctx.send('упсс... тебе такое недоступно')
@client.command()
async def dl(ctx):
    if str(ctx.message.author.id) in owner:
        await msgee.delete()
        await ctx.send('вроди удалилось')
    else:
        await ctx.send('упсс... тебе такое недоступно')
@client.command()
async def react(ctx,*,reac):
    if str(ctx.message.author.id) in owner:
        await msgee.add_reaction(reac)
        await ctx.send('поставили')
    else:
        await ctx.send('упсс... тебе такое недоступно')
@client.command()
async def set_stat(ctx,*,text=None):
    if str(ctx.message.author.id) in owner:
        if text == None:
            await ctx.send('укажи статус')
        elif str(text) == '-d':
            ver = discord.__version__
            total = 0
            memb = 0
            for guild in client.guilds:
                total += 1
                for member in guild.members:
                    memb += 1
            await client.change_presence(status = discord.Status.online, activity = discord.Game(f';help | {total} серверов | участников {memb} | версия API {ver}'))
            await ctx.send('изменено на стандартный статус')
        else:
            try:
                await client.change_presence(status = discord.Status.online, activity = discord.Game(text))
                await ctx.send('выполнено')
            except:
                await ctx.send('тьху блять опять рейтлимиты')
    else:
        await ctx.send('упсс... тебе такое недоступно')

@client.command()
async def howbrawl(ctx):
    otv=['0.1','50','100','1488','0','25','75']
    tt = random.choice(otv)
    await ctx.send(f'ты бравлер на {tt} процентов')

@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def findgay(ctx, member:discord.Member=None):
    if member is None:
        ment = ctx.message.author
    else:
        ment = member
    embed = discord.Embed(title='система поиска пидорасов активирована')
    embed.set_footer(text='начинаем проверку на гея')
    msg4 = await ctx.send('запуск...')
    await msg4.edit(content='анализируем...\n🟩🟩🟩\n🟩🟩🟩\n🟩🟩🟩')
    await asyncio.sleep(0.4)
    await msg4.edit(content='анализируем...\n🟥🟩🟩\n🟩🟩🟩\n🟩🟩🟩')
    await asyncio.sleep(0.4)
    await msg4.edit(content='анализируем...\n🟩🟥🟩\n🟩🟩🟩\n🟩🟩🟩')
    await asyncio.sleep(0.4)
    await msg4.edit(content='анализируем...\n🟩🔳🟥\n🟩🟩🟩\n🟩🟩🟩')
    await asyncio.sleep(0.4)
    await msg4.edit(content='анализируем...\n🟩🔳🟩\n🟥🟩🟩\n🟩🟩🟩')
    await asyncio.sleep(0.4)
    await msg4.edit(content='анализируем...\n🟩🔳🟩\n🟩🟥🟩\n🟩🟩🟩')
    await asyncio.sleep(0.4)
    await msg4.edit(content='анализируем...\n🟩🔳🟩\n🟩🔳🟥\n🟩🟩🟩')
    await asyncio.sleep(0.4)
    await msg4.edit(content='анализируем...\n🟩🔳🟩\n🟩🔳🟩\n🟥🟩🟩')
    await asyncio.sleep(0.4)
    await msg4.edit(content='анализируем...\n🟩🔳🟩\n🟩🔳🟩\n🔳🟥🟩')
    await asyncio.sleep(0.4)
    await msg4.edit(content='анализируем...\n🟩🔳🟩\n🟩🔳🟩\n🔳🔳🟥')
    await asyncio.sleep(0.4)
    await msg4.edit(content='анализируем...\n🟩🔳🟩\n🟩🔳🟩\n🔳🔳🔳')
    ov = ['ты гей','ты не гей','ты заядлый гей и любишь поe8@ться в попку']
    ttk = random.choice(ov)
    await ctx.send(f'{ment}, твой результат: {ttk}')

#ffffffffffffffffffffffffffffffffffffffff
#ffffffffffffffffffffffffffffffffffffffff
@client.command()
async def images(ctx, *, query: str=None):
    session = aiohttp.ClientSession()
    url = 'https://google.com/search'
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR '}
    image_headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235"}
    reaction_emojis = ['1⃣', '2⃣', '3⃣', '4⃣']
    if query is None:
        return await ctx.send('You are supposed to enter a query after the command, smh', delete_after=5)

    params = {'q': quote_plus(query), 'source': 'lmns', 'tbm': 'isch'}
    async with session.get(url, params=params, headers=image_headers) as r:
        html = await r.text()

    soup = BeautifulSoup(html, 'lxml')
    images = []
    for item in soup.select('div.rg_meta')[:4]:
        images.append(json.loads(item.text)["ou"])

    em = discord.Embed(title="Link", url=images[0])
    em.set_author(name=f"I found {query}")
    em.set_image(url=images[0])

    image_result = await ctx.send(embed=em)

    for emoji in reaction_emojis:
        await image_result.add_reaction(emoji)

    while 1:
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in reaction_emojis\
                    and reaction.message == ctx.message
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await image_result.delete()
            break
        for emoji in reaction_emojis:
            await image_result.remove_reaction(emoji, ctx.author)
        selected_item = reaction_emojis.index(str(reaction.emoji))
        em.set_image(url=images[selected_item])
        em.url = images[selected_item]
        await image_result.edit(embed=em)



@client.command()
async def help(ctx):
    embed=discord.Embed(title="-------------- (  Доступные команды ) --------------", color=0xab7aff)
    embed.add_field(name="Общее", value=";userinfo (ник) - инфа о челе\n;ping - задержка в мс\n;ip (ip) - инфа о айпи адресе\n;info (запрос) - поиск в википедии\n;yt - поиск в ютубе\n;urlb - ссылка на добавление бота\n;sinfo - информация о сервере\n;idea - отправить идею для бота\n;embed - создать кастомный ембед", inline=False)
    embed.add_field(name="Фан команды", value=";шлепа - пикчи с шлёпой\n;ac (назв ачивки) - создать ачивку майнкрафта(только английские буквы)\n;hack (цель) - произвести взлом жопы\n;findgay - узнай, на сколько ты гей\n;game (1 или 2) - миниигра\n;penis - размер пениса", inline=True)
    embed.add_field(name="Команды для модерации и т.п.", value=";poll (текст голосования) - создать голосование\n;cl (кол-во) очистка сообщений\n;nuke - самоуничтожение канала\n;addrole (id) - выдает всем участникам сервера определенную роль\n;delrole (id) - удаляет всем участникам сервера определенную роль\n;chanrename (name) - меняет названия всех каналов(требуется право на изменение каналов)\n;chandelname (name) - удаляет все каналы с определенным названием\n;roledelname (name) - удаляет роли с заданым названием\n;usersedit (change/reset) (text) - устанавливает всем участникам заданый ник на сервере\n;wl (add/remove) (упоминание участника) - добавить участника в белый список", inline=True)
    embed.add_field(name="Автопартнерство", value=";bump - разослать обьявление\n;setdesc - описание сервера\n;partner-channel - установить партнерский канал", inline=True)
    embed.add_field(name='Автомодерация',value=';anticrash (on/off) - блокирует изменение каналов и ролей для учасников не находящихся в белом списке\n;antispam (on/off) - кикает спамеров\n;aspam (задержка) (макс. кол-во повторяющихся сообщ.) - настройка антиспама', inline=True)
    embed.add_field(name='Кликер', value=";clicker - запуск самого кликера\n;top - посмотреть топ серверов по количеству кликов\n;bal - посмотреть баланс\n;boostup - увеличить свой уровень буста", inline=True)
    embed.add_field(name='искуственный интелект', value=';ii - включает и выключает ии в данном канале\nии потребляет и генерирует информацию на основе сообщений которые видит бот. его сообщения отсылаются с помощью случайно выбраного вебхука. Предупреждаю, ответы ии могут содержать оскорбления.')
    embed.add_field(name='доп. инфа', value=f"сервер поддержки [->клик](https://discord.gg/Fj2Nq5sFUT)\nссылка на бота [->клик](https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot)", inline=True)
    await ctx.send(embed=embed)

@client.command(aliases=['m','mute'])
@commands.has_permissions(manage_roles=True)
async def __m(ctx):
    await ctx.send("блин, покакал")

@client.command(aliases=['um','unmute'])
async def __um(ctx):
    await ctx.send("я давно хотел вам сказать, я безумно хочю питсы")
    
    
@client.command()
@commands.has_permissions(administrator=True)
@commands.cooldown(1, 120, commands.BucketType.user)
async def nuke(ctx):
    member = (ctx.author)
    author = (ctx.author.id)
    Block = []
    if author in Block:
        embed = discord.Embed(title=f'{ctx.author} вам запрещено пользоваться этой командой', color=0xff0000)
        embed.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:  
        embed1 = discord.Embed(title = f'{ctx.author.name} взорвать канал? Это приведет к полной очистке сообщений',color = 0xac00ff)
        check_h = await ctx.send(embed = embed1)
        await check_h.add_reaction('✅')
        await check_h.add_reaction('❌')
    def check1(reaction, user):
        return user == member and reaction.emoji in '✅❌:'
    try:
        reaction, user = await client.wait_for('reaction_add', check = check1, timeout = 100)
    except asyncio.TimeoutError:
        embed3 = discord.Embed(title = f'{ctx.author.name} TimeoutError', description = 'Время вышло',color = 0xff0000)
        embed3.set_footer(text=f"Call:{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        await check_h.edit(embed = embed3)
        return
    if reaction.emoji == '✅':     
        await ctx.send('подрываем канал')
        await asyncio.sleep(1)
        channel_id = ctx.channel.id
        channel = client.get_channel(channel_id)
        new_channel = await ctx.guild.create_text_channel(name=channel.name, topic=channel.topic, overwrites=channel.overwrites, nsfw=channel.nsfw, category=channel.category, slowmode_delay=channel.slowmode_delay, position=channel.position)
        await channel.delete(reason=f'канал взорвал {ctx.author}')
        await new_channel.send(f"канал был взорван.\nhttps://imgur.com/LIyGeCR\n**called by: {ctx.author}**")    
    if reaction.emoji == '❌':
        embed = discord.Embed(title = 'ядерное развооружение...',color = 0xff0000)
        embed.set_footer(text=f"вызвано: {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(manage_roles=True)
@commands.cooldown(1, 30, commands.BucketType.guild)
async def addrole(ctx, mention=None):
    if mention is None:
        embed = discord.Embed(title="Ошибка", description="Укажи id роли", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        try:
            a = int(mention)
        except:
            await ctx.send('ты должен указать айди роли(не упомянание)')
            return
        await ctx.send("выполнение...")
        mention = str(mention)
        mention = int(mention)
        role = discord.utils.get(ctx.guild.roles, id=mention)
        totalrole = 0
        for user in ctx.guild.members:
            roles = [role for role in user.roles]
            if role in roles:
                pass
            else:
                try:
                    totalrole += 1
                    await user.add_roles(role)
                except:
                    pass
        ch = await ctx.send(f'добавлена роль {totalrole} участникам')

@client.command()
@commands.has_permissions(manage_roles=True)
@commands.cooldown(1, 30, commands.BucketType.guild)
async def delrole(ctx, mention=None):
    if mention is None:
        embed = discord.Embed(title="Ошибка", description="Укажи id роли", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        try:
            a = int(mention)
        except:
            await ctx.send('ты должен указать айди роли(не упомянание)')
            return
        await ctx.send("выполнение...")
        mention = str(mention)
        mention = int(mention)
        role = discord.utils.get(ctx.guild.roles, id=mention)
        totalrole = 0
        for user in ctx.guild.members:
            roles = [role for role in user.roles]
            if role in roles:
                try:
                    totalrole += 1
                    await user.remove_roles(role)
                except:
                    pass
            else:
                pass
        ch = await ctx.send(f'убрана роль {totalrole} участникам')
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
@client.command(aliases=['sinfo','serverinfo','si','serveri'])
async def sinfo__(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",colour = discord.Colour.green())
    embed.add_field(name=f"дата создания:", value=f"""{ctx.guild.created_at.strftime("%A, %B %d %Y")}""", inline=True)
    embed.add_field(name="владелец", value=f"{ctx.guild.owner}", inline=True)
    embed.add_field(name="кол-во участников", value=f"{ctx.guild.member_count}", inline=True)
    embed.add_field(name='регион', value = f'{ctx.guild.region}', inline=True)
    embed.add_field(name='id',value = f'{ctx.guild.id}', inline=True)
    anspam = int(cu.execute("SELECT antispam FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
    if anspam == '0':
        aspam = 'включено'
    else:
        aspam = 'выключено'
    ancrash = int(cu.execute("SELECT anticrash FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
    if ancrash == '0':
        acrash = 'выключено'
    else:
        acrash = 'включено'
    atime = int(cursor.execute("SELECT atime FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
    amsg = int(cursor.execute("SELECT amsg FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
    embed.add_field(name='выставленные настройки автомодерации на сервере',value=f'Антиспам: {aspam}\nАвтокик крашботов: {acrash}\n**Доп. настройки антиспама** - задержка: {atime}, максимальное кол-во повторяемых сообщений: {amsg}')
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    try:
        embed.set_footer(text=f'на счету сервера {ctx.guild.name} - {int(cu.execute("SELECT clicks FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])} кликов')
    except:
        pass
    await ctx.send(embed=embed)
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
@client.command()
@commands.has_permissions(manage_channels=True)
async def chanrename(ctx,*,text=None):
    if text is None:
        embed = discord.Embed(title="Ошибка", description="Укажи название", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        await ctx.send("выполнение...")
        totalchan = 0
        for channel in ctx.message.guild.channels:
            try:
                await channel.edit(name=text, reason=f'изменение внес {ctx.message.author}')
                totalchan += 1
            except:
                pass
        ch = await ctx.send(f'изменено {totalchan} каналов')
@client.command()
@commands.has_permissions(manage_channels=True)
async def chandelname(ctx,*,text=None):
    if text is None:
        embed = discord.Embed(title="Ошибка", description="Укажи название", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        await ctx.send("выполнение...")
        totalchan = 0
        for channel in ctx.message.guild.channels:
            if channel.name == text:
                try:
                    await channel.delete(reason=f'изменение внес {ctx.message.author}')
                    totalchan += 1
                except:
                    pass
            else:
                pass
        ch = await ctx.send(f'удалено {totalchan} каналов')
    
    
@client.command()
@commands.has_permissions(administrator=True)
async def usersedit(ctx,arg=None,*,text=None):
    if str(arg) == 'change':
        if text is None:
            embed = discord.Embed(title="Ошибка", description="предполагается наличие второго аргумента", color=discord.Color.red())
            await ctx.send(embed=embed)
            
        elif arg is None or text is None:
            embed = discord.Embed(title="Ошибка", description="Укажи аргументы к команде", color=discord.Color.red())
            await ctx.send(embed=embed)
        
        else:
            totl = 0
            await ctx.send('выполняю...')
            for member in ctx.guild.members:
                try:
                    await member.edit(nick=text)
                    totl += 1
                except:
                    pass
            await ctx.send(f'отредактировано {totl} аккаунтов')
    else:
        if arg is None:
            embed = discord.Embed(title="Ошибка", description="предполагается наличие аргумента", color=discord.Color.red())
            await ctx.send(embed=embed)
        elif str(arg) == 'reset':
            await ctx.send('выполняю...')
            totl = 0
            for member in ctx.guild.members:
                try:
                    await member.edit(nick=member.name)
                    totl += 1
                except:
                    pass
            await ctx.send(f'отредактировано {totl} аккаунтов')
        else:
            embed = discord.Embed(title="Ошибка", description="неопознаный аргумент", color=discord.Color.red())
            await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(manage_roles=True)
async def roledelname(ctx,*,text):
    if text is None:
        embed = discord.Embed(title="Ошибка", description="Укажи название", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        totalchan = 0
        for role in ctx.message.guild.roles:
            if role.name == text:
                try:
                    await role.delete(reason=f'изменение внес {ctx.message.author}')
                    totalchan += 1
                except:
                    pass
            else:
                pass
        await ctx.send(f'удалено {totalchan} ролей')
#@client.command()
#async def setallchanperms(ctx,role=None,typee=None,stat=None):
#    if role == None and typee == None and stat == None:
#        await ctx.send('укажите аргументы - ;setallchanperms (роль или участник для которого устанавливаются права) (тип права) (статус права True или False). пример: ;setallchanperms @myadmins send_messages True')
#    else:
#        totalchan = 0
#        ch = await ctx.send(f'изменено {totalchan} каналов')
#        for channel in ctx.message.guild.channels:
#            overwrite = discord.PermissionOverwrite()
#            if typee ==
#            await channel.set_permissions(role,overwrite=overwrite)


crbots = [
    '752375465934716979',
    '739759620301783150',
    '748836498488688671',
    '745592436876771479',
    '434421396232470552',
    '571355896337268745',
    '751842364116697158',
    '750344312226578543',
    '754582738073419806',
    '592103751297269773',
    '693561691891564544',
    '727274305691582465',
    '742098569787605023',
    '726070033402298479',
    '756251948268912811',
    '748570839573725255',
    '464061969322737685',
    '737686378912940074',
    '762248306230689813',
    '755022108525985892',
    '759392269874364436',
    '762264326957957140',
    '755701729101611060',
    '766979829022064642',
    '767323030787194891',
    '760908258469740584',
    '742096645377884181',
    '748451058854002750',
    '777541052486778922',
    '779463784238153750',
    '779589144401412126',
    '767003600961404938',
    '784765278868340789',
    '794534591070601235',
    '809109351415021578',
    '802149140960116738',
    '789379263417417809',
    '789379263417417809',
    '802148167511834666',
    '802149140960116738',
    '802148167511834666',
    '789379263417417809',
    '809109351415021578',
    '807687693713539081',
    '712336083689537678',
    '712336083689537678',
    '805446656606470194',
    '727274305691582465',
    '742096645377884181',
    '760908258469740584',
    '767323030787194891',
    '766979829022064642',
    '755022108525985892',
    '762248306230689813',
    '813056513845231646',
    '812281378988621834'
    ]
@client.event
async def on_member_join(member):
    defend = int(cu.execute("SELECT anticrash FROM guilds WHERE id = {}".format(member.guild.id)).fetchone()[0])
    
    if defend == 1:
        if member.id in crbots:
            try:
                await member.ban(reason='этот участник является крашботом или крашером')
            except:
                pass
        else:
            pass
    else:
        pass
    
    
            
    if gcursor.execute("SELECT id FROM game where id = {}".format(member.id)).fetchone() is None:
        gcursor.execute("INSERT INTO game VALUES (?,?,?)", (member.id,0,1))
        print(f"[debug] added member {member.id}")
    else:
        pass
    
    
    
    
    
@client.command()
async def report(ctx, *, idea=None):
    if idea is None:
        embed = discord.Embed(title="Ошибка", description="Укажите айди `;report <текст>`", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        member = await client.fetch_user(user_id=826439777230258207)
        embed = discord.Embed(title="репорт", description=f"**Отправитель:\n**{ctx.author}\n**Айди:**\n{ctx.author.id}\n**тема:**\n{idea}", color=discord.Color.green())
        await member.send(embed=embed)
        embed2 = discord.Embed(title="Успешно!", description=f"Репорт был отправлен создатаелю\n**Содержимое:**\n{idea}", color=discord.Color.green())
        await ctx.send(embed=embed2)

@client.command()
async def cname(ctx,*,text):
    if str(ctx.message.author.id) in owner:
        await ctx.guild.edit(name=text)
        await ctx.message.delete()
    else:
        await ctx.send('тебе такое нельзя')
#from simpledemotivators import demcreate
#@commands.command()
#async def dem(ctx, text1: str = None,*, text2: str = None):
#    files = []
#    for file in ctx.message.attachments:
#        fp = io.BytesIO()
#        await file.save(fp = 'kek.jpg')
#    dem = demcreate(f'{text1}', f'{text2}')
#    dem.makeImage('kek')
#    await ctx.send(file = discord.File(fp = 'demresult.jpg'))

@client.command()
async def usercard(ctx):
    img = Image.new('RGBA',(400,200),'#232529')
    url = str(ctx.author.avatar_url)[:-10]
    response = requests.get(url,stream=True)
    response = Image.open(io.BytesIO(response.content))
    response = response.convert('RGBA')
    response = response.resize((100, 100), Image.ANTIALIAS)
    img.paste(response, (15,15,115,115))
    idraw = ImageDraw.Draw(img)
    name = ctx.author.name
    tag = ctx.author.discriminator
    headline = ImageFont.truetype('arial.ttf',size = 20)
    undertext = ImageFont.truetype('arial.ttf',size=12)
    idraw.text((117,15), f'{name}#{tag}',font = headline)
    idraw.text((117,50), f'id: {ctx.author.id}',font = headline)
    idraw.text((15,120), f'registered at: {ctx.author.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p")}',font = undertext)
    idraw.text((15,155), f'enter server at: {ctx.author.joined_at.strftime("%a, %#d, %B, %Y, %I:%M %p")}',font = undertext)
    img.save('user_card.png')
    await ctx.send(file= discord.File(fp = 'user_card.png'))


@client.command()
async def runbot(ctx,ToKen=None):
    if ToKen==None:
        m = await ctx.send('ты не указал токен')
        sleep(3)
        await m.delete()
    else:
        try:
            crashbot.crash(ToKen)
            b = 'временно недоступно'
            await ctx.message.delete()
        except Exception:
            await ctx.send(Exception)
        sleep(1)
        await ctx.send(b)

@client.event
async def on_command_error(ctx,error):
    
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('у тебя недостаточно прав')
    elif isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.NoPrivateMessage):
        await ctx.send('в лс команда не работает')
    elif isinstance(error, discord.Forbidden):
        await ctx.send('ммм класс, как я должен эту команду выполнять если ты мне нужных прав не дал?')
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send('у бота не хватает прав')
    elif isinstance(error, commands.CommandOnCooldown):
        ss = ['https://tenor.com/view/clean-rat-shower-bruh-moment-bruh-gif-14980572','https://media.discordapp.net/attachments/632583673845252137/784641586281185280/d.gif','https://media.discordapp.net/attachments/787007272605057124/789777078131359774/tenor.gif','https://cdn.discordapp.com/attachments/765600797023010817/792422031240855582/bruh-2.mp4','https://tenor.com/view/no-spamming-discord-discord-mods-stop-spamming-spam-gif-19068664','https://cdn.discordapp.com/attachments/784816789153906698/794600196377804860/2_5420618708919780782-1.gif','https://tenor.com/view/kkk-hitler-rape-nazi-blm-gif-19060261','https://cdn.discordapp.com/attachments/784816789153906698/794609713533681684/Oh_nigga_you_gay_vine.mp4']
        await ctx.send(f'{ctx.author.mention}, Команда будет доступна снова через **{error.retry_after:,.0f}**сек.')
    else:
        await ctx.send(f"опа, приехали, ошибочка :```{error}```")


@client.command()
async def mch(ctx):
    await ctx.send(f'platform - {sys.platform} | pytdir - {sys.executable}')
def tch(tokenlist):
    os.remove('tokens.txt')
    f = open('.\\tokens.txt', 'w+')
    f.write(tokenlist)
#@client.command()
#async def tokencheck(ctx,*,tokenlist):
#    totalcheck = 0
#    embedd = discord.Embed(title='чекер токенов',description='ожидайте..')
#    tch(tokenlist)
#    tokens = open('.\\tokens.txt', 'r').read().splitlines()
#    for t in tokens:
 #       print(t)
#    embb = await ctx.send(embed=embedd)
#    tot = await ctx.send(f'проверено ```{totalcheck}``` токенов')
#    embed = discord.Embed(title='чекер токенов',description='результат')
#    for token in tokens:
#        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
#        apilink = 'https://discordapp.com/api/v6/users/@me'
#        request = requests.Session()
#        src = requests.get(apilink, headers=headers)
#        if "401: Unauthorized" in str(src.content):
#            embed.add_field(name = 'недействителен', value = token)
#            totalcheck += 1
#            await tot.edit(content=f'проверено ```{totalcheck}``` токенов')
#        else:
#            response = json.loads(src.content.decode())
#            if response["verified"]:
#                embed.add_field(name = 'верифицирован', value = token)
#                totalcheck += 1
#                await tot.edit(content=f'проверено ```{totalcheck}``` токенов')
#            else:
#                embed.add_field(name = 'не верифицирован', value = token)
#                totalcheck += 1
#                await tot.edit(content=f'проверено ```{totalcheck}``` токенов')
#    await embb.delete()
#    emb = await ctx.send(embed=embed)

@client.command()
async def color(ctx,member,color):
    member = discord.utils.get(ctx.message.guild.members, name = member)
    role = member.top_role
    pos = int(role.position)
    pos += 1
    await ctx.guild.create_role(name = color,position=pos,colour=color)
    await ctx.send(f'цвет {member} изменен на {color}')

@client.command()
async def tokencheck(ctx,*,token):
    headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    apilink = 'https://discordapp.com/api/v6/users/@me'
    request = requests.Session()
    embed = discord.Embed(title='чекер токенов')
    src = requests.get(apilink, headers=headers)
    if "401: Unauthorized" in str(src.content):
        embed.add_field(name = 'недействителен', value = token)
    else:
        response = json.loads(src.content.decode())
        if response["verified"]:
            embed.add_field(name = 'верифицирован', value = token)
        else:
            embed.add_field(name = 'не верифицирован', value = token)
    emb = await ctx.send(embed=embed)

@client.command()
async def monitoring(ctx,arg=None,sid=None,slink=None,*,sdescript=None):
    embed = discord.Embed(title='мониторинг')
    if arg == None:
        obj1 = 'мониторинг - это то место где люди могут обмениваться серверами, находить новые и добавлять свои. Рядом ты можешь увидеть список команд'
        obj2 = ';monitoring add (id серваера) (ссылка) (описа��ие)-добавить сервер\n;monitoring delete (id сервера)-удалить сервер из списка\n;monitoring list - список серверов'
        embed.add_field(name='информация',value=obj1)
        embed.add_field(name='команды',value=obj2)
        await ctx.send(embed=embed)
    elif arg == 'add':
        if sid==None or slink == None or sdescript==None:
            await ctx.send('недостаточно аргументов')
        else:
            cur.execute('INSERT INTO servers VALUES ({},{},{})'.format(sid,slink,sdescript))
            con.commit()
            await ctx.send('сервер успешно добавлен на мониторинг')
    elif arg == 'delete':
        if sid==None:
            await ctx.send('укажите id ��ервера в качестве 2го аргумента')
        else:
            cur.execute(f"DELETE FROM servers WHERE id = {sid}")
            con.commit()
    elif arg == 'list':
        embed = discord.Embed(title='мониторинг',description='лист серверов:\n')
        for guild in client.guilds:
            gid = guild.id
            try:
                c = cur.execute(f"SELECT * FROM servers WHERE id ={gid}").fetchone()
                embed.add_field(name = f'хуй', value = c)
            except:
                pass
        await ctx.send(embed=embed)
    else:
        await ctx.send('неизвестный аргумент')

@client.command()
async def penis(ctx, member:discord.Member=None):
    if member is None:
        member = ctx.author
    penis = '8'
    size = random.randint(1, 30)
    #pisun = collection.find_one({"id": ctx.author.id})['piska']
    #size = size + int(pisun)
    for i in range(size):
        penis = penis + '='
    penis = penis + 'D'
    embed = discord.Embed(description=f"🍆 Пенис {member.mention}'a\n{penis}", color=discord.Color.green())
    await ctx.send(embed=embed)

def zalupa(invite):
    tokens = open('.\\raidtokens.txt', 'r').read().splitlines()
    for token in tokens:
        apilink = "https://discordapp.com/api/v6/invite/" + str(invite)
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.post(apilink, headers=headers)
        print('suc')

def pizda():
    print('aye')
    time.sleep(2)
    tokens = open('.\\raidtokens.txt', 'r').read().splitlines()
    for token in tokens:
        subprocess.Popen(['python.exe','.\\bot.py', token])

#@client.command()
#async def auraid(ctx,*,token):
#    user = ctx.author
#    headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
#    apilink = 'https://discordapp.com/api/v6/users/@me'
#    request = requests.Session()
#    embed = discord.Embed(title='авторейд')
#    src = requests.get(apilink, headers=headers)
#    if "401: Unauthorized" in str(src.content):
#        embed.add_field(name = 'недействителен', value = token)
#        tov = False
#    else:
#        response = json.loads(src.content.decode())
#        if response["verified"]:
#            embed.add_field(name = 'верифицирован', value = token)
#            tov = True
#        else:
#            embed.add_field(name = 'не верифицирован', value = token)
#            tov = False
#    emb = await ctx.send(embed=embed)
#    if tov == True:
#        await ctx.send('```запуск ботов```')
#        pizda()
#        await ctx.send('укажите код инвайта(буквы идущие после discord.gg/) командой ;inv (invite code)')
#        def check(message,user):
#            return user == member and message.content.startswith == ';inv'
#        await client.wait_for('message', check = check, timeout = 50)
#        await ctx.send('```загоняю ботов на сервер```')

#@client.command()
#async def balance(ctx, member:discord.Member=None):
    #if member is None:
    #    member = ctx.author
    #else:
    #    pass
    #embed = discord.Embed(title = "баланс",description = f"""баланс {member.name} составляет {collection.find_one({"id": member.id})['cash']} руб.\n уровень {member.name} - {collection.find_one({"id": member.id})['nigga']}""")
    #await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def work(ctx,arg=None):
    if arg is None:
        await ctx.send(embed=discord.Embed(title = 'доступные работы:',description='**работы для 1 лвл**\n1)собирать бутылки\n2)сдаться в рабство\n3)работа проституткой\n4)рыться в помойке'))
    elif arg == '1':
        f = random.randint(450,4500)
        await ctx.send('ты начал собирать бутылки.')
        sleep(1)
        await ctx.send(f'{ctx.author.mention}, ты закончил сбор бутылок, получив {int(f)} руб. Тебе нужно 20с для отдыха')
        amount1 = int(collection.find_one({"id": ctx.author.id})['cash']) + int(f)
        collection.update_one({"id": ctx.author.id},{"$set": {"cash": amount1}})
    elif arg == '2':
        f = random.randint(450,4500)
        await ctx.send('ты сдался в рабство какому то таджику.')
        sleep(1)
        await ctx.send(f'{ctx.author.mention}, тебя отпустили из рабства, ты получил {int(f)} руб. Тебе нужно 20с для отдыха')
        amount1 = int(collection.find_one({"id": ctx.author.id})['cash']) + int(f)
        collection.update_one({"id": ctx.author.id},{"$set": {"cash": amount1}})
    elif arg == '3':
        f = random.randint(450,4500)
        await ctx.send(f'{ctx.author.mention} начата работа проституткой.')
        sleep(1)
        await ctx.send(f"Ты поймал на дороге какогото жирного дальнобойщика и он жестко вставил тебе гдето в лесу, щедро заплатив {int(f)} руб. Тебе нужно 20с для отдыха")
        amount1 = int(collection.find_one({"id": ctx.author.id})['cash']) + int(f)
        collection.update_one({"id": ctx.author.id},{"$set": {"cash": amount1}})
    elif arg == '4':
        await ctx.send('вы начали копаться в помойке')
        sleep(1)
        f = random.randint(450,4500)
        await ctx.send(f'Бродя по помойке, вы, {ctx.author.mention}, находите разорватый пакет. В этом пакете было много членов и разрезаных гнилых органов. Среди этой хуйни вы замечаете окровавленые {int(f)} рублей. Вы решили спиздить себе бабос и не звонить в мусарню. На вас наорали местные бомжи и вы решили что безопаснее всего будет не ходить туда 20 секунд')
        amount1 = int(collection.find_one({"id": ctx.author.id})['cash']) + int(f)
        collection.update_one({"id": ctx.author.id},{"$set": {"cash": amount1}})
    else:
        await ctx.send('неизвестный аргумент')
@client.command()
async def brawlgovno(ctx):
    money = collection.find_one({"id": ctx.author.id})['cash']
    if int(money) > 1500:
        await ctx.send('вы купили оружие для растрела бравлеров за 5000')
        amount1 = int(collection.find_one({"id": ctx.author.id})['cash']) - 1500
        collection.update_one({"id": ctx.author.id},{"$set": {"cash": amount1}})
    else:
        await ctx.send(f'{ctx.author.mention} у тебя нехватает денег на покупку. нужно 5000')
@client.command()
async def gayclub(ctx):
    money = collection.find_one({"id": ctx.author.id})['cash']
    if int(money) > 500:
        await ctx.send(f'{ctx.author.mention}, ты пошел в гейклуб, отдав за вход 500руб')
        amount1 = int(collection.find_one({"id": ctx.author.id})['cash']) - 500
        collection.update_one({"id": ctx.author.id},{"$set": {"cash": amount1}})
    else:
        await ctx.send(f'{ctx.author.mention}, ты пошел в гейклуб, но у тебя нехватило денег на вход и тебе пришлось пожертвовать очком. Помянем. нужно 500')
#@client.command()
#async def admbsdo(ctx):
#    money = collection.find_one({"id": ctx.author.id})['cash']
#    if int(money) > 1000000:
#        await ctx.send('нихуя ты баклажан, сообщай <@642409834561404928> об этом в лс с пруфами, будешь модером на бсдо')
#    else:
#        await ctx.send('ааааааааааахаххахахахахахахахах бля тебе в жизни столько не накопить. нужно ```1000000```')


#@client.command()
#async def casino(ctx,count=None):
#    if count is None:
#        await ctx.send('укажите сумму рядом')
#    else:
#        money = curs.execute("SELECT cash FROM userss WHERE id = {}".format(ctx.author.id)).fetchone()[0]
#        r = random.randint(1,4)
#        if r == None:
#            await ctx.send('ошибка какаято блять че за хуйня')
#        elif r == 1:
#            await ctx.send('ты просрал свою ставку')
@client.command()
async def piska(ctx):
    money = collection.find_one({"id": ctx.author.id})['cash']
    if int(money) > 20000:
        await ctx.send(f'{ctx.author.mention}, ты пожизненно увеличиил размер пениса на 1 см за 20000руб')
        amount1 = int(collection.find_one({"id": ctx.author.id})['cash']) - 20000
        collection.update_one({"id": ctx.author.id},{"$set": {"cash": amount1}})
        piskanew = int(collection.find_one({"id": ctx.author.id})['piska']) + 1
        collection.update_one({"id": ctx.author.id},{"$set": {"piska": piskanew}})
    else:
        await ctx.send(f'{ctx.author.mention}, ты бомж, нужно 20000руб')
#@client.event
#async def on_message(message):
#    def check(m):
#        return (m.author == message.author and m.content == message.content)
#    if not message.author.bot:
#        if len(list(filter(lambda m: check(m), client.cached_messages))) >= 4:
#            await message.channel.send(f'{message.author.mention}, ты че ахуел тут спамить негр https://tenor.com/view/no-spamming-discord-discord-mods-stop-spamming-spam-gif-19068664')
#        else:
#            m = None
#    else:
#        pass
@client.command()
async def pay(ctx,member:discord.Member, count):
    if int(count) >= 0:
        try:
            amount1 = int(collection.find_one({"id": ctx.author.id})['cash']) - int(count)
            amount2 = int(collection.find_one({"id": member.id})['cash']) + int(count)
            collection.update_one({"id": ctx.author.id},{"$set": {"cash": amount1}})
            collection.update_one({"id": member.id},{"$set": {"cash": amount2}})
            await ctx.message.add_reaction('✅')
        except:
            await ctx.message.add_reaction('❌')
    else:
        await ctx.send('всмысле отрицательное число? ты ебанат?')
def addcash(ctx,arg1,arg2):
    amount1 = int(collection.find_one({"id": arg1})['cash']) + int(arg2)
    collection.update_one({"id": arg1},{"$set": {"cash": amount1}})
@client.command()
async def vzlom(ctx,count):
    if str(ctx.message.author.id) in owner:
        amount1 = int(collection.find_one({"id": ctx.author.id})['cash']) + int(count)
        collection.update_one({"id": ctx.author.id},{"$set": {"cash": amount1}})
        await ctx.message.add_reaction('✅')
    else:
        await ctx.send("sosi")
@client.command()
async def buylvl(ctx,arg):
    try:
        amount1 = int(collection.find_one({"id": ctx.author.id})['cash']) - 200000
        collection.update_one({"id": ctx.author.id},{"$set": {"cash": amount1}})
        collection.update_one({"id": ctx.author.id},{"$set": {"nigga": 1}})
        await ctx.message.add_reaction('✅')
    except:
        await ctx.message.add_reaction('❌')

@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def work2(ctx,arg=None):
    if int(collection.find_one({"id": ctx.author.id})['nigga']) >= 1:
        if arg==None:
            await ctx.send('досутпно 2 работы:\n1) - таксист\n2) - тракторист\nзаработок: 1000-10000руб')
        elif arg == '1':
            f = random.randint(1000, 10000)
            text = ['тебе попался болтливый клиент. в итоге у тебя бомбануло и ты наорал на него. он обосрался и сьебался, но за проезд заплатил ','ты спокойно отвез чела до места назначния. получено ','какаято шлюха начала рожать посреди магазина и тебе на ебаном такси пришлось везти ее в детдом... ой в роддом, получено ','ебаные алкаши решили трахнуться прям в такси и тебе пришлось их высадить на пол пути. получено ']
            await ctx.send(f'{ctx.author.mention}, ты начал работу таксистом. {random.choice(text)}{f}руб. отдохни хотябы 20 сек')
            amount1 = int(collection.find_one({"id": ctx.author.id})['cash']) + int(f)
            collection.update_one({"id": ctx.author.id},{"$set": {"cash": amount1}})
        elif arg == '2':
            f = random.randint(1000, 10000)
            text = ['до тебя доебался рандомный бич и спиздил у тебя 500 руб пока ты работал. получено ','ты чуть не задавил какогото негра, гуляющего по полю. получено ','половину рабочего дня ты пробухал и чтобы искупить вину, пришлось пожертвовать очком. F. получено ']
            await ctx.send(f'начата работа трактористом. {random.choice(text)}{f}руб. отдохни хотябы 20 сек')
            amount1 = int(collection.find_one({"id": ctx.author.id})['cash']) + int(f)
            collection.update_one({"id": ctx.author.id},{"$set": {"cash": amount1}})
        else:
            await ctx.send('неизвестный аргумент')
    else:
        await ctx.send(f'{ctx.author.mention}, у тебя низкий уровень, тебе нужен хотябы 1ур. (;buylvl 1 - купить 1 лвл за 200000руб.)')


def sendmsg(token, text, channel, server, count):
    request = requests.Session()
    headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    chanjson = request.get(f"https://canary.discordapp.com/api/v6/guilds/{server}/channels",headers=headers, timeout=10)
    channellist = json.loads(chanjson.content)
    payload = {"content": text, "tts": False}
    for i in range(int(count)):
        for channel in channellist:
            request.post(f"https://canary.discordapp.com/api/v6/channels/{channel['id']}/messages", headers=headers, json=payload, timeout=10)



@client.command()
async def webhookspam(ctx,count,url,*,text):
    if int(count) >= 101:
        await ctx.send(f'сотка максимум, а ты дубина ввел {count} раз')
    else:
        await ctx.message.add_reaction('✅')
        for i in range(int(count)):
            payload = {"content":text}
            requests.post(url,data=payload)
#=================on_message======
def wordadd(word):
    if '@everyone' in word or '@here' in word:
        pass
    else:
        if "@" in word or 'http' in word:
            pass
        else:
            pass
            #huyna
#щикфищелфузеф
def obrabotkaepta(user_message,message1,message2):
    responsee = ''
    with open('/p/ii.json','r',encoding="utf-8") as aye:
        filecont = aye.read()
    try:
        with open('/p/ii.json','r',encoding="utf-8") as f:
            text = user_message.replace(',','')
            f = json.load(f)
            optsize = 0
            for intent in f["intents"]:
                for pattern in intent["patterns"]:
                    tempopt = 0
                    pattern = str(pattern)#need optimize
                    for word in text.split(' '):
                        if len(pattern.split(' ')) == 1:
                            if word == pattern:
                                tempopt += 1
                            else:
                                pass
                        else:
                            if word in pattern.split(' '):
                                tempopt += 1
                            else:
                                pass
                    if int(tempopt) > int(optsize):
                        optsize = int(tempopt)
                        responsee = random.choice(intent["responses"])
                        #if user_message not in intent["patterns"]:
                        #    intent["patterns"].append(user_message)
                        #else:
                        #    pass
                    elif int(tempopt) == int(optsize):
                        s = random.randint(1,2)
                        if s == 1:
                            optsize = int(tempopt)
                            responsee = random.choice(intent["responses"])
                        else:
                            pass
                    else:
                        pass
            def mmr(f,message1,message2):
                with open('/p/ii.json','w') as e:
                    payload = {
                        "patterns": [f"{message1}"],
                        "responses": [f"{message2}"]
                    }
                    f['intents'].append(payload)
                    json.dump(f, e, indent=4,ensure_ascii=False)
            if int(optsize) == 0:
                mmr(f,message1,message2)
            elif int(optsize) in [1,2] and len(user_message.split(' ')) > 1:
                mmr(f,message1,message2)
            else:
                pass
    except Exception as exc:
        with open('/p/ii.json','w') as e:
            e.write(filecont)
        print('-------------------------error--------------------------')
        print(exc)
    #with open('universal.json','r') as g:
    #    for word in responsee.split(' '):
    #        for gobject in g["ptn"]:
    #            for gword in gobject:
    #                try:
    #                    
    #                except:
    #                    pass
    return responsee
    
def iimemoryadd(message1,message2):
    with open('/p/ii.json','r') as f:
        js = json.load(f)
    with open('/p/ii.json','w+') as d:
        patterns = []
        responses = []
        patterns.append(str(message1)) 
        responses.append(str(message2))
        payload = {
            "tag":f'{random.randint(1000,99999)}{random.randint(1000,99999)}{random.randint(1000,99999)}{random.randint(1000,99999)}{random.randint(1000,99999)}{random.randint(1000,99999)}{random.randint(1000,99999)}{random.randint(1000,99999)}',
            "patterns": patterns,
            "responses": responses,
            "context_set": "unknown"
        }
        print(payload)
        js['intents'].append(payload)
        json.dump(js, d, indent=4)

@client.event
async def on_message(message):
    await client.process_commands(message)
    pizdeccc = ['discord.gg','discord.com','@everyone','@here','@','http','https','://']
    messages = await message.channel.history(limit=2).flatten()
    trust = True
    for messagee in messages:
        for f in pizdeccc:
            if f in messagee.content.lower() or messagee.content == '':
                trust = False
                break
    st = '! @ # $ % ^ & * ( ) _ - + = . / , ? pls Pls'.split(' ')
    for messagee in messages:
        for f in st:
            if messagee.content.startswith(f'{f}'):
                trust = False
                break
    if trust is True:
        #chance = random.randint(1,40)
        #if int(chance) == 3:
        #    messages = await message.channel.history(limit=2).flatten()
        message1 = messages[1].content.lower()
        message2 = messages[0].content.lower()
        #    iimemoryadd(message1, message2)
        #else:
        #    pass
        if str(message.channel.id) in iiget(message.guild.id):
            if message.author.bot:
                pass
            else:
                rsp = obrabotkaepta(message.content.lower(),message1,message2)#aigetresponse(message.content.lower())
                if rsp == None or str(rsp) == '':
                    pass
                else:
                    try:
                        webhooks = await message.channel.webhooks()
                        webhook = random.choice(webhooks)
                        await webhook.send(rsp)
                    except:
                        pass
        else:
            pass
    else:
        pass
    aut = message.author
    #mute = int(cursor.execute("SELECT muterole FROM guilds WHERE id = {}".format(message.guild.id)).fetchone()[0])
    #for role in aut.roles:
    #    rid = role.id
    #    if int(rid) == int(mute):
    #        await message.delete()
    #    else:
    #        pass
    #print(f'#[{message.guild.name}]# - [{message.author}] : {message.content}')
    
    if client.user.mentioned_in(message):
        if '@everyone' in message.content or '@here' in message.content:
            pass
        else:
            await message.add_reaction("✅")
    else:
        pass
    if message.author.bot or message.author.permissions_in(message.channel).administrator == True:
        pass
    else:
        defend = int(cu.execute("SELECT antispam FROM guilds WHERE id = {}".format(message.guild.id)).fetchone()[0])
        if defend == 0:
            pass
        elif defend == 1:
            
            atime = int(cursor.execute("SELECT atime FROM guilds WHERE id = {}".format(message.guild.id)).fetchone()[0])
            
            amsg = int(cursor.execute("SELECT amsg FROM guilds WHERE id = {}".format(message.guild.id)).fetchone()[0])
            
            amsglow = int(amsg) - 1
            def check (msg):
            
                return (msg.author == message.author and (datetime.datetime.utcnow() - msg.created_at).seconds < int(atime)) and msg.content == message.content
            
            if len(list(filter(lambda m: check(m), client.cached_messages))) >= int(amsglow) and len(list(filter(lambda m: check(m), client.cached_messages))) < int(amsg):
            
                await message.channel.send(f"{message.author.mention} не спамь!")
            elif len(list(filter(lambda m: check(m), client.cached_messages))) >= int(amsg):
                embed = discord.Embed(title = f"**вы были кикнуты с сервера**", description = f"причина : спам", color = 0xff0000)
                await message.author.send(embed = embed)
                try:
                    await message.author.kick()
                    await message.channel.send(f"{message.author.mention} был кикнут за спам !")
                except:
                    pass
        else:
            pass
    
    
    
    
    
#============================on_message=========
@client.command()
async def chname(ctx, *, name: str):
    if str(ctx.message.author.id) in owner:
        await client.user.edit(username=name)
        await ctx.message.add_reaction('✅')
    else:
        await ctx.message.add_reaction('❌')
        
        
        
@client.command(aliases=['pb','pixelbattle'])
async def __pixelbattle(ctx, color, xa, ya):
    if int(xa) >= 40 or int(ya) >= 40:
        await ctx.send('указаны слишком большие координаты, доступны от 0 до 39 по x и y оси')
    else:
        xa = int(xa) * 10
        ya = int(ya) * 10
        img = Image.open("pixelbattle.png")
        draw = ImageDraw.Draw(img)
        xb = int(xa) + 10
        yb = int(ya) + 10
        draw.rectangle((int(xa), int(ya), int(xb), int(yb)),fill=color)

        img.save('pixelbattle.png')
        await ctx.send(file= discord.File(fp = 'pixelbattle.png'), delete_after=10)
@client.command()
async def cleanfd(ctx):
    if str(ctx.message.author.id) in owner:
        img = Image.new('RGB',(400,400),'#ffffff')
        img.save('pixelbattle.png')
    else:
        await ctx.message.add_reaction('❌')
@client.command(aliases=['sf','showfield','field'])
async def __field(ctx):
    await ctx.send(file= discord.File(fp = 'pixelbattle.png'))

@client.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def pbimg(ctx,xa,ya):
    xa = int(xa) * 10
    ya = int(ya) * 10
    xb = xa + 80
    yb = ya + 80
    img = Image.open("pixelbattle.png")

    if not ctx.message.attachments:
        url = str(ctx.author.avatar_url)[:-10]
        response = requests.get(url,stream=True)
        response = Image.open(io.BytesIO(response.content))
        response = response.convert('RGBA')
        response = response.resize((100, 100), Image.ANTIALIAS)
        img.paste(response, (xa,ya,xb,yb))
        idraw = ImageDraw.Draw(img)
        img.save('pixelbattle.png')
    else:
        for file in ctx.message.attachments:
            url = file.url
            url = str(url)
            response = requests.get(url,stream=True)
            response = Image.open(io.BytesIO(response.content))
            response = response.convert('RGBA')
            response = response.resize((100, 100), Image.ANTIALIAS)
            img.paste(response, (xa,ya,xb,yb))
            idraw = ImageDraw.Draw(img)
            img.save('pixelbattle.png')
    await ctx.send(file= discord.File(fp = 'pixelbattle.png'))

@client.command()
async def rsl(ctx, id, *, text=None):
    if ctx.message.author.id in owner:
        for guild in client.guilds:
            if guild.id == int(id):
                pass
            else:
                pass
    else:
        await ctx.send("huy sosi")
        
@client.command(aliases=['шлепа','шлёпа','floppa'])
async def ayetatari__(ctx):
    aaaaaa =[
        'https://memepedia.ru/wp-content/uploads/2020/10/screenshot_11-3.png',
        'https://memepedia.ru/wp-content/uploads/2020/10/screenshot_10-3.png',
        'https://memepedia.ru/wp-content/uploads/2020/10/big-floppa-meme.png',
        'https://memepedia.ru/wp-content/uploads/2020/10/bolshoj-shlepa-5-360x270.jpg',
        'https://memepedia.ru/wp-content/uploads/2020/10/bolshoj-shlepa-3.jpg',
        'https://i.ytimg.com/vi/zDhxA8rZY4k/maxresdefault.jpg',
        'https://i.ytimg.com/vi/LlMXNr_LF08/hqdefault.jpg',
        'https://i.ytimg.com/vi/qwLT6np8DJM/maxresdefault.jpg',
        'https://startgames.org/wp-content/uploads/2020/12/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9-%D1%88%D0%BB%D0%B5%D0%BF%D0%B0-%D0%A4%D0%BB%D0%BE%D0%BF%D0%BF%D0%B0-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D0%BE%D1%82-4-640x459.jpg',
        'https://static.wikia.nocookie.net/floppa/images/9/96/Floppa.jpg/revision/latest?cb=20200815053935',
        'https://i.ytimg.com/vi/g_47HOqNVVg/maxresdefault.jpg',
        'https://static.wikia.nocookie.net/floppa/images/d/d1/MADDRIP2.jpg/revision/latest/top-crop/width/360/height/450?cb=20201222000559',
        'https://i.redd.it/x0h0w7ozg8461.jpg',
        'https://static.wikia.nocookie.net/floppa/images/f/f2/WideFloppa.jpg/revision/latest?cb=20201105152154',
        'https://avatars.mds.yandex.net/get-znatoki/1545559/2a00000176b7536300e9638b4ba7762a4e92/w480',
        'https://memepedia.ru/wp-content/uploads/2020/10/big-floppa-4-360x270.jpg',
        'https://vk.com/photo-201452090_457241067',
        'https://cdn.discordapp.com/attachments/812364227738075186/812941247940919316/9T9uqdsLr5E.jpg',
        'https://cdn.discordapp.com/attachments/812364227738075186/812941247702237194/Qa7DDCeb1FQ.jpg',
        'https://cdn.discordapp.com/attachments/812364227738075186/812941247294472212/zR1vAofmJX0.jpg',
        'https://cdn.discordapp.com/attachments/812364227738075186/812941246871502858/EkOehB_BLtM.jpg',
        'https://cdn.discordapp.com/attachments/812364227738075186/812941246619713557/SWW7Q7qXCEs.jpg',
        'https://cdn.discordapp.com/attachments/812364227738075186/812941949346381854/EcFJyxYoaig.jpg',
        'https://cdn.discordapp.com/attachments/812364227738075186/812941949106782229/tX0jKij_v9c.jpg',
        'https://cdn.discordapp.com/attachments/812364227738075186/812941948838477884/ut368jN44jA.jpg',
        'https://cdn.discordapp.com/attachments/812364227738075186/812941948615786536/E8L3TaD8bvM.jpg',
        'https://r5.mt.ru/r3/photo472B/20467497080-0/jpg/bp.webp',
        'https://cs13.pikabu.ru/post_img/big/2020/12/26/11/1609011892174478536.jpg',
        'https://startgames.org/wp-content/webp-express/webp-images/doc-root/wp-content/uploads/2020/12/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9-%D1%88%D0%BB%D0%B5%D0%BF%D0%B0-%D0%A4%D0%BB%D0%BE%D0%BF%D0%BF%D0%B0-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D0%BE%D1%82-11-640x603.jpg.webp',
        'https://2ch.hk/b/src/234653109/16070912386072.jpg',
        'http://sun9-44.userapi.com/s/v1/ig2/7emxmSE2nNnwZTQEOe80GDoXFdCbL4SguUUhB5rKChSHpRmVV9tEhewqYLs4yjKpYvBPDVG3g1BQ8hyU1UcAbvHH.jpg?size=200x0&quality=96&crop=56,6,200,200&ava=1',
        'https://preview.redd.it/pw2f4rf5isi61.jpg?auto=webp&s=30291613449b7a80fce2036e2aae726496b11936'
        'https://cdn.discordapp.com/attachments/845721818375520327/846970596902699038/20210525124147.jpg',
        'https://cdn.discordapp.com/attachments/845721818375520327/846970780838658048/20210517080359.jpg',
        'https://cdn.discordapp.com/attachments/845721818375520327/846971442704678912/20210426172755.jpg',
        'https://cdn.discordapp.com/attachments/845721818375520327/846971613236035585/16215844557820.jpg',
        'https://cdn.discordapp.com/attachments/845721818375520327/846972858999373824/20210420184828.jpg',
        'https://cdn.discordapp.com/attachments/845721818375520327/846975334783123466/9b6pnTgyhx8.jpg',
        'https://cdn.discordapp.com/attachments/845721818375520327/846975344548380702/pGvRUIxFP7U.png',
        'https://cdn.discordapp.com/attachments/845721818375520327/846975352474697748/FDFhqrcqyig.png',
        'https://cdn.discordapp.com/attachments/845721818375520327/846975365070979102/MitRODViPA.jpg',
        'https://cdn.discordapp.com/attachments/845721818375520327/846975374675673099/HwM4SYjmscs.jpg', 
        'https://cdn.discordapp.com/attachments/845721818375520327/846975386084704276/LwilZXBnSuc.jpg',
        'https://cdn.discordapp.com/attachments/845721818375520327/846975395353329715/x-3l1cWpe9k.jpg',
        'https://cdn.discordapp.com/attachments/845721818375520327/846975422783946762/IMG20210311125825.jpg'
        ]
    url = random.choice(aaaaaa)
    embed=discord.Embed(title='большой шлепа',description='русский кот')
    embed.set_image(url=str(url))
    await ctx.send(embed=embed)



@client.command()
@commands.cooldown(1, 18000, commands.BucketType.guild)
async def bump(ctx):
    e = 0
    succ = 0
    tryed = 0
    for i in ctx.guild.members:
        e += 1
    channelid = cu.execute("SELECT channel FROM guilds WHERE id = {}".format(ctx.guild.id))
    text = cu.execute("SELECT description FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0]
    if channelid == 0 or text == 'измените описание командой ;setdesc (text)':
        await ctx.send("сначала укажите описание сервера и канал для партнерства")
        bump.reset_cooldown(ctx)
    else:
        await ctx.send("рассылка началась")
        if len(await ctx.guild.invites()) == 0:
            invite = await ctx.channel.create_invite()
        else:
            invite = None
            for invitee in await ctx.guild.invites():
                if invitee.max_age == 0 and invitee.max_uses == 0:
                    invite = invitee
            if invite is None:
                invite = await ctx.channel.create_invite()
            else:
                pass
        embed=discord.Embed(title = ctx.guild.name, description = f"{text}\n🔖 | [ссылка]({invite})\n👑 | Овнер : {ctx.guild.owner}\n🕶️ | участников: {e}")
        for guildd in client.guilds:
            tryed += 1
            try:
                channeld = cu.execute("SELECT channel FROM guilds WHERE id = {}".format(guildd.id)).fetchone()[0]
                cnl = client.get_channel(channeld)
                await cnl.send(embed=embed)
                succ += 1
            except:
                pass
        await ctx.send(f"ваше обьявление доставлено на {succ} из {tryed} серверов")
@client.command()
@commands.has_permissions(administrator=True)
async def setdesc(ctx,*,text=None):
    if text == None:
        await ctx.send("⚠️ укажите описание")
    elif '@everyone' in text or '@here' in text:
        await ctx.send("❌ нельзя использовать пинг в описании")
    elif 'discord.gg/' in text or 'discord.com/invite/' in text:
        await ctx.send('❌ приглашения в описании запрещены')
    elif 'https://' in text or 'http://' in text:
        await ctx.send('❌ ссылки в описании запрещены')
    else:
        cu.execute("UPDATE guilds SET description = ? WHERE id = ?", (str(text),ctx.guild.id))
        conect.commit()
        await ctx.send(embed=discord.Embed(title='✔️ Готово',description=f'**новое описание успешно установлено**\n{text}'))

@client.command(aliases=["partner-channel","pc"])    
@commands.has_permissions(administrator=True)
async def partnerchannel(ctx,id=None):
    if id == None:
        await ctx.send("укажите id канала")
    else:
        try:
            chan = client.get_channel(int(id))
            if chan == None:
                await ctx.send(embed=discord.Embed(title='❌ Ошибка',description = 'неверно указан id канала'))
            else:
                cu.execute("UPDATE guilds SET channel = {} WHERE id = {}".format(id,ctx.guild.id))
                conect.commit()
                await ctx.send(embed=discord.Embed(title='✔️ Готово',description = f'успешно установлен канал {chan}'))
        except:
            await ctx.send(embed=discord.Embed(title='❌ Ошибка',description = 'неверно указан id канала'))
            
@client.command()
@commands.has_permissions(administrator=True)
async def aspam(ctx, atime=None, amsg=None):
    if atime is None or amsg is None:
        await ctx.send(embed=discord.Embed(title='❌ Ошибка',description = 'указаны не все аргументы\nпример команды: ;aspam 5 4 - где 5 это интервал между сообщениями, а 4 это максимальное количество повторяющихся сообщений'))
    else:
        if int(amsg) < 3:
            await ctx.send(embed=discord.Embed(title='❌ Ошибка',description = 'кол-во сообщений неможет быть меньше 3'))
        elif int(amsg) > 20:
            await ctx.send(embed=discord.Embed(title='❌ Ошибка',description = 'кол-во сообщений не должно превышать 20'))
        elif int(atime) < 2:
            await ctx.send(embed=discord.Embed(title='❌ Ошибка',description = 'задержка не может быть меньше 2 сек'))
        elif int(atime) > 60:
            await ctx.send(embed=discord.Embed(title='❌ Ошибка',description = 'задержка не может быть больше 60 сек'))
        else:
            cursor.execute("UPDATE guilds SET atime = {} WHERE id = {}".format(int(atime),ctx.guild.id))
            cursor.execute("UPDATE guilds SET amsg = {} WHERE id = {}".format(int(amsg),ctx.guild.id))
            connect.commit()
            await ctx.send(embed=discord.Embed(title='✔️ Готово',description = f'обновлены настройки антиспама:\nмакс. кол-во повторяющихся сообщ. - {amsg}\nзадержка - {atime}'))
            
            
@client.command()
async def raid(ctx,arg1=None,arg2=None,*,arg3=None):
    tokens = open('.\\tokens.txt','r').read().splitlines()
    description = '```>...```'
    embed = discord.Embed(title='рейд очка',description = description)
    m = await ctx.send(embed=embed)
    if str(arg1) == 'inv':
        description = description + str(f'\n```>[жопный инвайтер] invite code = {str(arg2)}\n>...```')
        await m.delete()
        m = await ctx.send(embed=discord.Embed(title='рейд очка',description=description))
        tc = 0
        for token in tokens:
            try:
                tc += 1
                apilink = "https://discordapp.com/api/v6/invite/" + str(arg2)
                headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
                requests.post(apilink, headers=headers)
            except:
                description = description + f'```[жопный инвайтер] токен {token} не может зайти```'
        await m.delete()
        description = description + f'\n```>[жопный инвайтер] успешно - {tc}```'
        await ctx.send(embed=discord.Embed(title='рейд очка', description=description))
    elif str(arg1) == 'add':
        f = open('.\\tokens.txt', 'w+')
        f.write(str(arg2)).splitlines()
        f.close
    
@client.command()
async def servs(ctx):
    for guild in client.guilds:
        await ctx.send(f"{guild.name} id:{guild.id} уч:{guild.member_count}")
       
async def createmute(ctx):
    role = await ctx.guild.create_role(name = 'мут')
    cursor.execute("UPDATE guilds SET muterole = {} WHERE id = {}".format(int(role.id),ctx.guild.id))
    
        
#@client.command
#async def mute(ctx, member:discord.Member=None, reason):
#    if int(cursor.execute("SELECT muterole FROM guilds WHERE id = {}".format(message.guild.id)).fetchone()[0]) == 0:
#        createmute(ctx)
 #       embed = discord.Embed(title="Предупреждение", description="Роль для мута не была указана, поэтому я создам ее сам", color=discord.Color.red())
 #       xd = await ctx.send(embed=discord.Embed)
   #     muteroleid = cursor.execute("SELECT muterole FROM guilds WHERE id = {}".format(message.guild.id)).fetchone()[0]
    #    muterole = role = discord.utils.get(ctx.guild.roles, id = int(muteroleid))
        
@client.command()
async def leaveguild(ctx, count):
    ttt = 0
    m = await ctx.send(f'ливнул с {ttt} серверов')
    for guild in client.guilds:
        memb = 0
        for member in guild.members:
            memb += 1
        if int(memb) == int(count):
            await guild.leave()
            ttt += 1
            
            await m.edit(content = f'ливнул с {ttt} серверов {memb}')
        else:
            pass
    await ctx.send('vse')
    
@client.command()
async def webhooktest(ctx, t):
    webhook = ctx.channel.create_webhook(name='pizdorvanka')
    await webhook.send(content=t)
        
        
def tch(tokenlist):
    os.remove('/p/tokens.txt')
    f = open('/p/tokens.txt', 'w+')
    try:
        tokenlist = str(tokenlist).replace(" ","\n")
    except:
        pass
    f.write(tokenlist)
        
@client.command()
async def findnegr(ctx,*,idd):
    idd = ctx.message.content[9:]
    tokens = idd.split(' ')
    print(tokens)
    tokens.remove(tokens[0])
    if len(tokens) > 1:
        embed = discord.Embed(title='поиск негров')
        for iddd in tokens:
            #try:
            iddd = iddd.replace(' ','')
            print(iddd)
            member = await client.fetch_user(iddd)
            
            inf = 'обнаружен на серверах:\n'
            for guild in client.guilds:
                for user in guild.members:
                    if int(member.id) == int(user.id):
                        inf = inf + f'{guild.name}\n'
                    else:
                        pass
            embed.add_field(name=f'{member.name}#{member.discriminator}',value=str(inf),inline=False)
            #except:
            #    embed.add_field(name=f'{iddd}',value='сукина шлюха закрыла лс либо неправильный ид',inline=False)
        await ctx.send(embed=embed)
    else:
        for iddd in tokens:
            iddd = iddd.replace(' ','')
            member = await client.fetch_user(int(iddd))
            embed = discord.Embed(title='поиск негров')
            embed.set_thumbnail(url = member.avatar_url)
            embed.add_field(name = "Айди", value = member.id )
            embed.add_field(name = "Ник", value = member.display_name )
    #    embed.add_field(name = "Информация:", value = inn )
            embed.add_field(name = "Был зареган: ", value = member.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p") )
            inf = ''
            for guild in client.guilds:
                for user in guild.members:
                    if int(member.id) == int(user.id):
                        inf = inf + f'{guild.name}\n'
                    else:
                        pass
            embed.add_field(name = "обнаружен на серверах",value = f'{inf}',inline=False)
        await ctx.send(embed=embed)
        
@client.command()
async def fnadd(ctx,token):
    f = open('/p/ftokens.txt','w+')
    f.writelines(f'{str(token)}\n')
    f.close
    await ctx.send('токен добавлен нахуй',delete_after=10)
    
    
@client.command()
async def clicker(ctx):
    message = await ctx.send(embed=discord.Embed(title='**Кликер**',description='за каждое нажатие на реакцию под этим сообщением тебе будет зачисляться деньги, умноженые на твой уровнень буста.',color=discord.Color.gold(),footer='после 10 секунд неактивности, зачисления происходить не будут'))
    try:
        await message.add_reaction("💵")
    except:
        await ctx.send(embed=discord.Embed(title='❌ Ошибка',description = 'для того чтобы бот мог ставить реакции,выдайте ему нужные права'))
    member0 = ctx.message.author
    def check228(reaction, user):
        return reaction.emoji in '✖️💵' and user == user
        
        
    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', check = check228, timeout = 10)
                    
        except asyncio.TimeoutError:
            embed1 = discord.Embed(title = f'**Кликер**', description = 'Время вышло',color = 0xff0000)
            await message.edit(embed=embed1)
            return
            break
            
        if reaction.emoji == '💵':
            
            
            #do shit about giving money
            
            money = int(gcursor.execute("SELECT money FROM game WHERE id = {}".format(user.id)).fetchone()[0])
            boost = int(gcursor.execute("SELECT boost FROM game WHERE id = {}".format(user.id)).fetchone()[0])
                     
            summ = 1 * int(boost)
            totalmoney = int(money) + int(summ)
            gcursor.execute("UPDATE game SET money = ? WHERE id = ?", (int(totalmoney),user.id))
            gconnect.commit()
            gclicks = summ + int(cu.execute("SELECT clicks FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
            cu.execute("UPDATE guilds SET clicks = ? WHERE id = ?", (int(gclicks),ctx.guild.id))
            conect.commit()
            if user.id == client.user.id:
                pass
            else:
                await reaction.remove(user)
        else:
            pass
        
        
@client.command(aliases=["bal","balance"])
async def bal___(ctx, member:discord.Member=None):
    if member is None:
        member = ctx.author
    else:
        pass
    embed = discord.Embed(title = "баланс",description = f'баланс {member.name} составляет {int(gcursor.execute("SELECT money FROM game WHERE id = {}".format(member.id)).fetchone()[0])} 💵\nбуст {member.name} - {int(gcursor.execute("SELECT boost FROM game WHERE id = {}".format(member.id)).fetchone()[0])}')
    try:
        embed.set_footer(text=f'на счету сервера {ctx.guild.name} - {int(cu.execute("SELECT clicks FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])} кликов')
    except:
        pass
    await ctx.send(embed=embed)
    
    
def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Выбор наименьшего значения
            if arr[j] < arr[minimum]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        arr[minimum], arr[i] = arr[i], arr[minimum]
            
    return arr
    
    
def sort(arr):

    if len(arr) <= 1:
    
        return arr
        
    pivot = arr[len(arr) // 2]
    
    left = [x for x in arr if x < pivot]
    
    middle = [x for x in arr if x == pivot]
    
    right = [x for x in arr if x > pivot]
    
    return sort(left) + middle + sort(right)
    
@commands.cooldown(1, 5, commands.BucketType.user)
@client.command()
async def top(ctx):
    embed = discord.Embed(title='топ 9 серверов по кликам', description="если ваш сервер не отображается в топе значит его уровень в списке меньше 9")
    #conect.* cu.*
    guilds1 = {}
    for guild in client.guilds:
        clicks = int(cu.execute("SELECT clicks FROM guilds WHERE id = {}".format(guild.id)).fetchone()[0])
        if int(clicks) <= 1:
            pass
        else:
            guilds1[clicks] = int(guild.id)
    print(guilds1)
    #получаем больший элемент
    unsorted = []
    
    for k, v in guilds1.items():
        k = str(k)
        k = int(k)
        unsorted.append(k)
    
    #sortedg = selection_sort(unsorted)
    #sortedg=sortedg[::-1]
    complited = 0
    piska = 10
    while int(complited) == 0:
        try:
            j = 0
            #for i in sortedg:
            for i in range(int(piska)):
                j += 1
                #num = int(i)
                num = max(unsorted)
                score = int(j)
                if int(score) >= 10:
                    break
                else:
                    pass
                try:
                    gid = guilds1[str(num)]
                except:
                    gid = guilds1[int(num)]
                #guild = client.get_guild(int(gid))
                #inv = await guild.invites()
                #inv = random.choice(inv)
                #inv = str('https://discord.gg/'+inv)
                embed.add_field(name=f'{score}. **{client.get_guild(int(gid)).name}**',value=f'{num} кликов',inline=True)
                #sortedg.remove(num)
                unsorted.remove(num)
            await ctx.send(embed=embed)
            complited = 1
            break
        except:
            piska -= 1
            complited = 0
        print(piska)
        print(complited)
        print(unsorted)
        print('--------')
@client.command()
async def boostup(ctx):
    member = ctx.message.author
    boostnow = int(gcursor.execute("SELECT boost FROM game WHERE id = {}".format(ctx.message.author.id)).fetchone()[0])
    boosttobuy = int(boostnow) + 1
    count = int(boosttobuy) * 100
    
    embed1 = discord.Embed(title = f'{ctx.author.name} ты действительно хочешь купить буст {boosttobuy} уровня за {count} кликов?',color = 0xac00ff)
    check_h = await ctx.send(embed = embed1)
    await check_h.add_reaction('✅')
    await check_h.add_reaction('❌')
    def check1(reaction, user):
        return user == member and reaction.emoji in '✅❌:'
    try:
        reaction, user = await client.wait_for('reaction_add', check = check1, timeout = 100)
    except asyncio.TimeoutError:
        embed3 = discord.Embed(title = f'{ctx.author.name} TimeoutError', description = 'Время ожидания ответа вышло',color = 0xff0000)
        embed3.set_footer(text=f"{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        await check_h.edit(embed = embed3)
        return
    if reaction.emoji == '✅':     
        usermoney = int(gcursor.execute("SELECT money FROM game WHERE id = {}".format(ctx.message.author.id)).fetchone()[0])
        if int(usermoney) < int(count):
            embed3 = discord.Embed(title = f'{ctx.author.name}', description = f'Недостаточно средств. Нужно еще {int(count) - int(usermoney)}',color = 0xff0000)
            embed3.set_footer(text=f"{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await check_h.edit(embed = embed3)
        else:
            embed3 = discord.Embed(title = f'{ctx.author.name}', description = f'Успешно приобретен {boosttobuy} уровень буста за {count} кликов',color = 0x00ff00)
            embed3.set_footer(text=f"{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await check_h.edit(embed = embed3)
            totalmoney = int(usermoney) - int(count)
            gcursor.execute("UPDATE game SET money = ? WHERE id = ?", (int(totalmoney),ctx.message.author.id))
            gcursor.execute("UPDATE game SET boost = ? WHERE id = ?", (int(boosttobuy),ctx.message.author.id))
            
            
    if reaction.emoji == '❌':
        embed = discord.Embed(title = 'отменено',color = 0xff0000)
        embed.set_footer(text=f"{ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed = embed)
        
        
@client.event
async def on_guild_channel_create(channel):
    defend = int(cu.execute("SELECT anticrash FROM guilds WHERE id = {}".format(channel.guild.id)).fetchone()[0])
    if int(defend) == 1:
        whitelist = wlget(channel.guild.id)
        async for i in channel.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=2),action=discord.AuditLogAction.channel_create):
            
            if str(i.user.id) in whitelist or str(i.user.id) == str(client.user.id):
                break
            else:
                await i.target.delete(reason=f"{i.user.name} не в белом списке")
    else:
        pass
    
    
@client.event
async def on_guild_channel_delete(channel):
    defend = int(cu.execute("SELECT anticrash FROM guilds WHERE id = {}".format(channel.guild.id)).fetchone()[0])
    if int(defend) == 1:
        whitelisted = wlget(channel.guild.id)
        async for i in channel.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=2),action=discord.AuditLogAction.channel_delete):
            if str(i.user.id) in whitelisted or str(i.user.id) == str(client.user.id):
                break
            else:
                await channel.clone()
    else:
        pass
@client.event
async def on_guild_role_create(role):
    defend = int(cu.execute("SELECT anticrash FROM guilds WHERE id = {}".format(role.guild.id)).fetchone()[0])
    if int(defend) == 1:
        whitelisted = wlget(role.guild.id)
        async for i in role.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=2),action=discord.AuditLogAction.role_create):
            if str(i.user.id) in whitelisted or str(i.user.id) == str(client.user.id):
                break
            else:
                await i.target.delete()
    else:
        pass
        
@client.event
async def on_guild_role_delete(role):
    defend = int(cu.execute("SELECT anticrash FROM guilds WHERE id = {}".format(role.guild.id)).fetchone()[0])
    if int(defend) == 1:
        whitelisted = wlget(role.guild.id)
        async for i in role.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes=2),action=discord.AuditLogAction.role_delete):
            if str(i.user.id) in whitelisted or str(i.user.id) == str(client.user.id):
                pass
            else:
                await i.target.clone()
    else:
        pass

@client.command()
@commands.has_permissions(administrator=True)
async def wl(ctx,arg=None,user:discord.Member=None):
    if arg is None or user is None:
        #error message
        await ctx.send("укажите все требуемые аргументы")
    else:
        try:
            pppppp = user.top_role.position
        except:
            pppppp = None
        if pppppp is None:
            await ctx.send("неверно указан аргумент")
        else:
            try:
                uid = user.id
            except:
                pass
            usermaxrole = int(ctx.author.top_role.position)
            botuser = get(ctx.guild.members, id=int(client.user.id))
            
            botmaxrole = int(botuser.top_role.position)
            if ctx.author.permissions_in(ctx.channel).administrator == True:
                if str(arg) == 'add':
                    whitelist = wlget(ctx.guild.id)
                    if str(user.id) not in whitelist:
                        wladd(ctx.guild.id,user.id)
                        await ctx.send("участник успешно добавлен в белый писок")
                    else:
                        await ctx.send("участник уже в белом списке")
                            
                elif str(arg) == 'remove':
                    whitelist = wlget(ctx.guild.id)
                    try:
                        if str(user.id) in whitelist:
                            wldel(ctx.guild.id,user.id)
                            await ctx.send(f"участник убран из белого списка")
                    except:
                        await ctx.send("такого участника нет в белом списке")
                else:
                    await ctx.send("неверный аргумент")
            else:
                await ctx.send("вы должны быть администратором")
            
            
@client.command()
async def clientstop(ctx):
    if str(ctx.author.id) in owner:
        await client.change_presence(status = discord.Status.online, activity = discord.Game(f'бот выключен'))
        exit(0)
    else:
        await ctx.send('сосай')
    
    
@client.command()
async def clientrestart(ctx):
    if str(ctx.author.id) in owner:
        cna = client.get_channel(865111751515177031)
        path = '/p/mainfile1.py'
        msgt = await cna.send(embed = discord.Embed(title="бот перезагружен",description=f"исходный размер основного файла {os.path.getsize(path)}байт.\nкод завершения процесса 0"))
        subprocess.Popen(['python3','/p/mainfile1.py'])
        await client.change_presence(status = discord.Status.online, activity = discord.Game(f'бот перезагружается, команды могут неработать'))
        exit(0)
    else:
        await ctx.send('fucking slave, тебе такая команда недоступна')
@client.command()
async def dashboard(ctx):
    def form_embed(ctx):
        guild = ctx.guild
        embed=discord.Embed(title=f'**DASHBOARD** для {guild.name}')
        
        anspam = int(cu.execute("SELECT antispam FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
        if anspam == '0':
            aspam = 'включено'
        else:
            aspam = 'выключено'
        ancrash = int(cu.execute("SELECT anticrash FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
        if ancrash == '0':
            acrash = 'выключено'
        else:
            acrash = 'включено'
        atime = int(cursor.execute("SELECT atime FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
        amsg = int(cursor.execute("SELECT amsg FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        clicks = cu.execute("SELECT clicks FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0]
        
        embed.add_field(name=f'антиспам[📄]',value=aspam,inline=False)
        embed.add_field(name=f'доп. настройки антиспама[🔧]',value=f'{amsg} сообщ. за {atime} секунд',inline=False)
        embed.add_field(name=f'антикраш[☢️]',value=acrash,inline=False)
        
        channelo = cu.execute("SELECT channel FROM guilds WHERE id = {}".format(guild.id)).fetchone()[0]
        if int(channelo) == 0:
            chan = 'канал не установлен'
        else:
            try:
                chan = client.get_channel(int(channelo))
            except:
                chan = "канал удален или произошла ошибка"
        embed.add_field(name=f'канал для автопартнерки🔊',value=chan,inline=False)
        text = cu.execute("SELECT description FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0]
        if str(text) == 'измените описание командой ;setdesc (text)':
            aupt = 'текст не задан'
        else:
            aupt = 'нажмите 📃 чтобы просмотреть текст или 📝 чтобы изменить его'
        embed.add_field(name=f'текст автопартнерки',value=aupt,inline=False)
        
        embed.add_field(name=f'клики сервера',value=f'{clicks} кликов',inline=False)
        embed.add_field(name=f'пустое поле',value=f'тут что то будет..',inline=False)
        return embed
    
    mesg = await ctx.send(embed=form_embed(ctx),components=[
        #Button(style=ButtonStyle.green, label='антиспам')
        #Button(style=ButtonStyle.green, label='доп. настройки антиспама')
        #Button(style=ButtonStyle.green, label='')
        #Button(style=ButtonStyle.green, label='')
        #Button(style=ButtonStyle.green, label='')
        #Button(style=ButtonStyle.green, label='')
        ])
    response = await client.wait_for('button_click')
    if response.channel == ctx.channel and response.user == ctx.author:
        if response.component.label == 'антиспам':
            #some events
            anspam = int(cu.execute("SELECT antispam FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
            if str(anspam) == '0':
                aspam = 1
            else:
                aspam = 0
            
            cu.execute("UPDATE guilds SET antispam = {} WHERE id = {}".format(int(aspam),ctx.guild.id))
            conect.commit()
            await mesg.edit(embed=form_embed(ctx))
            #await response.respond(content="")#едит содержания кнопки
        elif response.component.label == 'доп. настройки антиспама':
            pass
        elif response.component.label == 'антикраш':
            ancrash = int(cu.execute("SELECT anticrash FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
            if str(ancrash) == '0':
                acrash = 1
            else:
                acrash = 0
            
            cu.execute("UPDATE guilds SET anticrash = {} WHERE id = {}".format(int(acrash),ctx.guild.id))
            conect.commit()
        
        elif response.component.label == 'вайтлист':
            pass
        elif response.component.label == '':
            pass
        elif response.component.label == '':
            pass
        
    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', check = check1, timeout = 50)
        except asyncio.TimeoutError:
            embed3 = discord.Embed(title = f'{ctx.author.name} TimeoutError', description = 'Время ожидания ответа вышло',color = 0xff0000)
            await mesg.edit(embed = embed3)
            break
        if reaction.emoji == '📄':
            anspam = int(cu.execute("SELECT antispam FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
            if anspam == '0':
                aspam = 1
            else:
                aspam = 0
            
            cu.execute("UPDATE guilds SET antispam = {} WHERE id = {}".format(int(aspam),ctx.guild.id))
            conect.commit()
            await mesg.edit(embed=form_embed(ctx))
        elif reaction.emoji == '☢️':
            ancrash = int(cu.execute("SELECT anticrash FROM guilds WHERE id = {}".format(ctx.guild.id)).fetchone()[0])
            if ancrash == '0':
                acrash = 1
            else:
                acrash = 0
            
            cu.execute("UPDATE guilds SET anticrash = {} WHERE id = {}".format(int(acrash),ctx.guild.id))
            conect.commit()
            await mesg.edit(embed=form_embed(ctx))
        elif reaction.emoji == '🔧':
            pass
        elif reaction.emoji == '🔊':
            await ctx.send("упомяните нужный канал: ")
            channel = ctx.channel
            def check(m):
                return m.channel == channel and m.author == ctx.message.author
    
            msg = await client.wait_for('message', check=check,timeout=200)
            ch = client.textChannel(msg.content)
            cu.execute("UPDATE guilds SET channel = {} WHERE id = {}".format(ch.id,ctx.guild.id))
            conect.commit()
            
        elif reaction.emoji == '📃':
            await ctx.send(f"текст для автопартнерства:\n{cu.execute('SELECT description FROM guilds WHERE id = {}'.format(ctx.guild.id)).fetchone()[0]}")
        elif reaction.emoji == '📝':
            await ctx.send("еще не сделал")
        else:
            await ctx.send("invalid ebaiy")
            
@client.command()
async def osrun(ctx,*,command):
    os.system(command)
    await ctx.message.add_reaction("✔️")
    
@client.command()
async def embed(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    m1 = await ctx.send('Укажите заголовок:')
    title = await client.wait_for('message', check=check,timeout=200)

    m2 = await ctx.send('Укажите описание:')
    desc = await client.wait_for('message', check=check,timeout=200)
    
    
    embed = discord.Embed(title=title.content, description=desc.content, color=0xff6700)
    
    m4 = await ctx.send('Укажите количество дополнительных полей(0 если не надо):')
    
    count = await client.wait_for('message', check=check,timeout=200)
    count = count.content
    if int(count) == 0:
        pass
    else:
        for i in range(int(count)):
            m5 = await ctx.send('название поля:')
            name = await client.wait_for('message', check=check,timeout=200)
            m6 = await ctx.send('описание поля:')
            descript = await client.wait_for('message', check=check,timeout=200)
            embed.add_field(name=str(name.content),value=str(descript.content),inline=True)
            try:
                await m5.delete()
            except:
                pass
            try:
                await m6.delete()
            except:
                pass
            try:
                await name.delete()
            except:
                pass
            try:
                await descript.delete()
            except:
                pass
    m54 = await ctx.send("укажите ссылку на картинку ембеда(напишите None если не нужна):")
    url = await client.wait_for('message', check=check,timeout=200)
    url = url.content
    if str(url) == 'None' or str(url) == 'none':
        pass
    else:
        embed.set_image(url=str(url))
    m = await ctx.send("генерирую ембед")
    await ctx.send(embed=embed)
    try:
        await m.delete()
    except:
        pass
    try:
        await m1.delete()
    except:
        pass
    try:
        await title.delete()
    except:
        pass
    try:
        await m2.delete()
    except:
        pass
    try:
        await desc.delete()
    except:
        pass
    try:
        await count.delete()
    except:
        pass
    
    


@client.command()
@commands.has_permissions(administrator=True)
async def ii(ctx):
    if str(ctx.channel.id) not in iiget(ctx.guild.id):
        
        try:
            guild = ctx.guild
            webhooks = await ctx.channel.webhooks()
            ll = []
                
            channel = ctx.channel
            rg = len(webhooks)
            if rg < 1:
                hh = 1 - int(rg)
                for i in range(int(hh)):
                    oguild = client.get_guild(int(856247439307964427))
                    for emoji in oguild.emojis:
                        ll.append(emoji.id)
                    idd = random.choice(ll)
                    url = f"https://cdn.discordapp.com/emojis/{int(idd)}.{'gif' if emoji.animated else 'png'}"
                    avatar = requests.get(url).content
                    await channel.create_webhook(name='AI',avatar=avatar)
            else:
                pass
            webhooks = await ctx.message.channel.webhooks()
            iiadd(ctx.guild.id, ctx.channel.id)
            await ctx.message.add_reaction("🤖")
        except:
            await ctx.message.add_reaction("⚠️")
            await ctx.send('возникла проблема при активации ии. возможно, что у бота нет прав на создание вебхуков')
            
    else:
        iidel(ctx.guild.id, ctx.channel.id)
        await ctx.message.add_reaction("🗑️")
        await ctx.send('ии выключен')
        
        
@client.command()
async def fakeperm_ii(ctx):
    if str(ctx.message.author.id) in owner or "Pizdec" in ctx.author.name:
        if str(ctx.channel.id) not in iiget(ctx.guild.id):
            
            try:
                guild = ctx.guild
                webhooks = await ctx.channel.webhooks()
                ll = []
                    
                channel = ctx.channel
                rg = len(webhooks)
                if rg < 1:
                    hh = 1 - int(rg)
                    for i in range(int(hh)):
                        #oguild = ctx.guild
                        #for emoji in oguild.emojis:
                        #    ll.append(emoji.id)
                        #idd = random.choice(ll)
                        #url = 'https://cdn.discordapp.com/emojis/{}.{}'.format(int(idd),"gif" if emoji.animated else "png");
                        #avatar = requests.get(url).content
                        names = random.choice(['van','billy','slave','fucking slaves','pussy','dick','fat cock','бомж валерий','жма'])
                        await channel.create_webhook(name=f'{names}')
                else:
                    pass
                webhooks = await ctx.message.channel.webhooks()
                iiadd(ctx.guild.id, ctx.channel.id)
                await ctx.message.add_reaction("🤖")
                await ctx.send('предупреждаю заранее, бот обучается на основе того что видит на разных серверах, поэтому в его ответах могут содержаться оскорбления. Не воспринимай их всерьез, договорились?')
            except Exception as e:
                print(e)
                await ctx.message.add_reaction("⚠️")
                await ctx.send('возникла проблема при активации ии. возможно, что у бота недостаточно прав')
                
        else:
            iidel(ctx.guild.id, ctx.channel.id)
            await ctx.message.add_reaction("🗑️")
            await ctx.send('ии выключен')
    else:
        await ctx.send("а вот ты так не можешь")

@client.command()
async def key(ctx):
    if ctx.author == ctx.guild.owner:
        with open('universal.json','r') as f:
            f = json.load(f)
            for server in f["servers"]:
                if str(server["id"]) == str(ctx.guild.id):
                    key = str(server["key"])
            await ctx.author.send(f"ваш ключ сервера: ```\n{key}\n```. передавайте только тем кому доверяете. чтобы регенерировать ключ введите ;keyregen")
    else:
        await ctx.send('ключ может узнать только овнер сервера')

@client.command()
async def keyregen(ctx):
    if ctx.author == ctx.guild.owner:
        with open('universal.json','r') as f:
            f = json.load(f)

    else:
        await ctx.send('доступно только овнеру сервера')
#client.run('ODIzMDg0MjgzMjk5MzY0OTQ0.YFbq-Q.RYpx0OTNApvtwRQqFd4NbXqqXrw')#тесты
#client.run('хуй соси')#основа
client.run("хуй соси")#nb
