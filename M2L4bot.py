import discord, os, requests
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


@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))

    # ¡Y así es como se puede sustituir el nombre del fichero desde una variable!
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run("")
