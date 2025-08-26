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

    await ctx.send(f'**{member.name}** joined {discord.utils.format_dt(member.joined_at)}')


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

def get_cat_facts():
    url = 'https://meowfacts.herokuapp.com/'
    res = requests.get(url)
    
    if res.status_code == 200: #Comprobamos si cuando hicimos la petición HTTP (requests.get(url)), el servidor devolvio un código de estado correcto.
        data = res.json()
        # Accedemos al primer dato dentro de "data" (que es una lista)
        return data['data'][0]

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command('catfact')
async def cat(ctx):
    cat_fact = get_cat_facts()
    await ctx.send(cat_fact)

temp_des = {
    "papel": "2 a 5 meses",
    "cáscara de plátano": "2 a 10 días",
    "chicle": "5 años",
    "lata de aluminio": "200 a 500 años",
    "bolsa de plástico": "150 años",
    "botella de plástico": "450 años",
    "cigarro": "1 a 10 años",
    "vidrio": "4000 años o nunca",
    "cartón": "2 a 5 meses",
    "ropa de algodón": "1 a 5 meses",
    "ropa de poliéster": "más de 200 años",
    "pañal desechable": "500 años",
    "madera": "1 a 3 años"
}

@bot.command()
async def tiempo(ctx, *, material: str):
    material = material.lower()
    if material in temp_des:
        await ctx.send(f" El/la **{material}** tarda **{temp_des[material]}** en descomponerse.")
    else:
        await ctx.send("⚠️ Lo siento, no tengo información sobre ese material. Intenta con otro.")

lugares_naturales = [
    "parques nacionales",
    "playas",
    "bosques",
    "selvas",
    "montañas",
    "volcanes",
    "cascadas",
    "ríos",
    "lagos",
    "lagunas",
]

@bot.command()
async def lugar(ctx):
    lugar_random = random.choice(lugares_naturales)
    await ctx.send(f"Te recomiendo visitar: **{lugar_random}**")

botes = [
    "Bote amarillo: Para envases ligeros como plásticos (PET), latas y Tetra Pak",
    "Bote verde: Para vidrio, como botellas y frascos.",
    "Bote naranja: Para residuos orgánicos, como restos de comida y poda.",
    "Bote gris: Para residuos no reciclables o resto de residuos generales que no entran en otras categorías.",
    "Bote azul: Para papel y cartón.",
    "Bote rojo: Para residuos peligrosos, como pilas, medicamentos caducados o productos químicos."
]

@bot.command()
async def bote(ctx):
    mensaje = random.choice(botes)
    await ctx.send(f" {mensaje}")
    
bot.run("")
