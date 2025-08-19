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
async def opt(ctx, opt: str, *numbers: float):
    if not numbers:
        return await ctx.send("Debes escribir al menos un número.")

    if opt == "+":
        result = sum(numbers)

    elif opt == "x":
        result = 1
        for n in numbers:
            result *= n

    elif opt == "/":
        result = numbers[0]
        for n in numbers[1:]:
            result /= n

    elif opt == "//":
        result = numbers[0]
        for n in numbers[1:]:
            result //= n

    else:
        return await ctx.send("Operación no válida. Usa +, x, / o //")

    await ctx.send(result)

@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def joined(ctx, member: discord.Member):

    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run("")
