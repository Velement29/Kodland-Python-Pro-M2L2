import os
import discord
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

print(os.listdir())
print(os.listdir('M2L1/image'))

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot llamado {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'Adios amigo!')

@bot.command('manualidad')
async def manualidad(ctx):
    text = ""
    video = ""
    manualselec = random.randint(1, 3)

    if manualselec == 1:
        text = "¡Aqui tienes una manualidad con material reciclable!\nEsta manualidad es un avión de papel reciclable que sirve como alcancía\nNecesitarias los siguitenes materiales:\n2 Papel Foamy de colores diferentes\nUna botella de agua vacia"
        video = "https://www.youtube.com/watch?v=T5kQiJxCkg4"
        await ctx.send(text)
        await ctx.send(video)
        with open(os.path.join('M2L2\images', 'avion.png'), 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif manualselec == 2:
        text = "¡Aqui tienes una manualidad con material reciclable!\nEsta manualidad es un porta-retrato giratorio\nNecesitarias los siguitenes materiales:\nPapel Foamy escarchado\nCartón\nPapel de plastico\nEngrapadora\nTapas de plastico de botellas\nTubitos de papel higienico\nUn Cautín\nGoma\nUn exacto"
        video = "https://www.youtube.com/watch?v=noKdhREAPz4"
        await ctx.send(text)
        await ctx.send(video)
        with open(os.path.join('M2L2\images', 'portaretrato.png'), 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif manualselec == 3:
        text = "¡Aqui tienes una manualidad con material reciclable!\nEsta manualidad es un mini coche de carreras\nNecesitarias los siguitenes materiales:\nTemperas\nPinceles\nChinchetas\nPegatinas\nTijeras\nRollos de papel higienico\nCartón"
        video = "https://www.youtube.com/watch?v=hlGPRicekGQ"
        await ctx.send(text)
        await ctx.send(video)
        with open(os.path.join('M2L2\images', 'coche.png'), 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)


bot.run("")