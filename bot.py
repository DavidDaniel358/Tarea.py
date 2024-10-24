import os
import random
import discord
from bot_logic import gen_pass
from discord.ext import commands
from bot_logic import flip_coin
from bot_logic import get_duck_image_url
from bot_logic import get_fox_image_url

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "$", intents=intents )

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()    
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()    
async def bye(ctx):
    await ctx.send("😔")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))  

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def flip(ctx):     
    await ctx.send(flip_coin())

@bot.command()
async def man(ctx):
    with open('Image/meme1.jpg', 'rb') as f:
        #vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable
        picture = discord.File(f)
    await ctx.send(file=picture)        

@bot.command()
async def meme_random(ctx):
    memo_alet = random.choice(os.listdir('Image'))
    with open(f'Image/{memo_alet}', 'rb') as f:
        #vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
         
@bot.command('fox')
async def fox(ctx):
    '''Una vez que llamamos al comando fox, 
    el programa llama a la función get_fox_image_url'''
    image_lur = get_fox_image_url()
    await ctx.send(image_lur)         
bot.run("TOKEN")
