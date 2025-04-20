import discord
from discord.ext import commands
import os
intents=discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix='$',
    intents=intents
)

@bot.command()
async def responda(ctx, arg):
    await ctx.send(f"Você me mandou {arg}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Olá! Sou um bot gerenciador de tarefas da turma de ADS da Fatec Sorocaba 😊")


bot.run(os.getenv('TOKEN'))