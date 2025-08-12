import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def opt(ctx, opt: str, left: int, right: int):
    if opt == "+":
        await ctx.send(left + right)
    elif opt == "x":
        await ctx.send(left * right)
    elif opt == "/":
        await ctx.send(left / right)
    elif opt == "//":
        await ctx.send(left // right)

@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def joined(ctx, member: discord.Member):

    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run("")
