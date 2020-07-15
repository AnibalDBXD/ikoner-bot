import discord
from discord.ext import commands
from RiotWatcher import src
from riotwatcher import LolWatcher
import urllib.request, json
from urllib import parse,request
import re

#Variables
bot = commands.Bot(command_prefix='=', description="Bot Oficial de Ikoners!")

#Cargar el JSON de todos lso champs
with urllib.request.urlopen("http://ddragon.leagueoflegends.com/cdn/10.14.1/data/es_AR/champion.json") as url:
    champions_data = json.loads(url.read().decode())
    
watcher = LolWatcher('RGAPI-963052f9-5a06-40bf-9865-126418fb5139')
my_region = 'la1'

#Comandos
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#Cambia el estado al streamer seleccionado
@bot.command()
async def streaming(ctx, streamer_name):
    url_streamer="https://www.twitch.tv/"+streamer_name
    await bot.change_presence(activity=discord.Streaming(name=streamer_name, url=url_streamer))
    await ctx.send("Streamer a mostrar es: " + streamer_name)

#Resetea el estado de streaming
@bot.command()
async def reset(ctx):
    await bot.change_presence(activity=discord.Game(name="League of Legends"))

#Muestra Stats del champ
@bot.command()
async def champ(ctx, champ):
      try:
        #Transformo a String el parametro del comando
        nombre = str(champ)
        #Guardo en la variable la Lista de todos los datos del Campeon selecionado
        selected_champ = champions_data['data'][nombre]
        
        champ_embed = discord.Embed(title=selected_champ['name'], description=selected_champ['title'],
        colour=discord.Colour.gold())

        champ_embed.add_field(name="Lore", value=selected_champ['blurb'])
        
        champ_embed.set_author(name="Ikoner", url="https://www.youtube.com/channel/UCN2cPKmtHpQ0m44ILhpNTZg",icon_url="http://ddragon.leagueoflegends.com/cdn/10.14.1/img/champion/"+selected_champ['name']+".png")
      #Construyo las Stats
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


#Comando help
@bot.command()
async def comandos(ctx):
    help_embed=discord.Embed(title="Comandos",description="Todos los comandos disponibles",colour=discord.Colour.dark_gold())
    help_embed.set_author(name="Ikoner",url="https://www.youtube.com/channel/UCN2cPKmtHpQ0m44ILhpNTZg",icon_url="https://cdn.discordapp.com/attachments/727351589311873144/728718306604744805/unknown.png")
    help_embed.add_field(name="=ping", value="pong", inline=True)
    help_embed.add_field(name="=champ", value="Devuelve una descripcion y stats del campeon escrito", inline=True)

    await ctx.send(embed=help_embed)


#Eventos
@bot.event
async def on_ready():

    await bot.change_presence(activity=discord.Game(name="League of Legends"))

    print("Estoy listo")


bot.run('NzI4NzIxODcxMTcxNzQ3ODQx.Xw1NhQ.O4xd2UKsvnNWo5sbJ62MlowaO0g')
