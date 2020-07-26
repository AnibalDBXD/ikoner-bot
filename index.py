import discord
from discord.ext import commands
from riotwatcher import *
import urllib.request, json
from urllib import parse,request
import re



bot = commands.Bot(command_prefix='=', description="Bot Oficial de Ikoners!")

#Load JSON for api riot
with urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/10.14.1/data/es_AR/champion.json") as url:
    champions_data = json.loads(url.read().decode())
    
watcher = LolWatcher('***********-********-****')
my_region = 'la1'

#Comandos

#Test command
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#change state to write stream
@bot.command()
async def streaming(ctx, streamer_name):
    url_streamer="https://www.twitch.tv/"+streamer_name
    await bot.change_presence(activity=discord.Streaming(name=streamer_name, url=url_streamer))
    await ctx.send("Streamer a mostrar es: " + streamer_name)

#Reset streaming to league of legend
@bot.command()
async def reset(ctx):
    await bot.change_presence(activity=discord.Game(name="League of Legends"))

#Show stats Champ
@bot.command()
async def champ(ctx, champ):
      try:
        #Convert to String the parameter of comando
        nombre = str(champ)
        #selected champ = The List of all dates of selected champ 
        selected_champ = champions_data['data'][nombre]
        
        champ_embed = discord.Embed(title=selected_champ['name'], description=selected_champ['title'],
        colour=discord.Colour.gold())

        champ_embed.add_field(name="Lore", value=selected_champ['blurb'])
        
        champ_embed.set_author(name="Ikoner", url="https://www.youtube.com/channel/UCN2cPKmtHpQ0m44ILhpNTZg",icon_url="http://ddragon.leagueoflegends.com/cdn/10.14.1/img/champion/"+selected_champ['name']+".png")
      #build the Stats
        champ_embed.add_field(name="Stats", value=
        "HP: "                      + str(selected_champ['stats']['hp'])          + "\n" +
        "Velocidad de Movimiento: " + str(selected_champ['stats']['movespeed'])   + "\n" +
        "Armadura: "                + str(selected_champ['stats']['armor'])       + "\n" +
        "Rango: "                   + str(selected_champ['stats']['attackrange']) + "\n" +
        "Regeneracion de vida: "    + str(selected_champ['stats']['hpregen'])     + "\n" +
        "AD: "                      + str(selected_champ['stats']['attackdamage'])+ "\n" +
        "Velocidad de ataque: "     + str(selected_champ['stats']['attackspeed']) + "\n",inline=False)
        
        await ctx.send(embed=champ_embed)
      except KeyError:
        await ctx.send('Ese Campeon no existe :O')


#Help command
@bot.command()
async def comandos(ctx):
    help_embed=discord.Embed(title="Comandos",description="Todos los comandos disponibles",colour=discord.Colour.dark_gold())
    help_embed.set_author(name="Ikoner",url="https://www.youtube.com/channel/UCN2cPKmtHpQ0m44ILhpNTZg",icon_url="https://cdn.discordapp.com/attachments/727351589311873144/728718306604744805/unknown.png")
    help_embed.add_field(name="=ping", value="pong", inline=True)
    help_embed.add_field(name="=champ", value="Devuelve una descripcion y stats del campeon escrito", inline=True)

    await ctx.send(embed=help_embed)


#Events

#Show "Estoy Listo" when the bot 
@bot.event
async def on_ready():

    await bot.change_presence(activity=discord.Game(name="League of Legends"))

    print("Estoy listo")

#Bot token
bot.run('NzI4NzIxODcxMTcxNzQ3ODQx.Xw1NhQ.O4xd2UKsvnNWo5sbJ62MlowaO0g')
