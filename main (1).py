# Так можно прочитать весь файл
#f = open('text.txt', 'r', encoding='utf-8')
#text = f.read()
#print(text)
#f.close()

# А так перезапишем файл полностью
#f = open('text.txt', 'w', encoding='utf-8')
#text = 'Новый текст'
#f.write(text)
#f.close()

# А вот сокращенная версия
#with open('text.txt', 'r', encoding='utf-8') as f:
    #print(f.read())

#with open('text.txt', 'w', encoding='utf-8') as f:
    #f.write('new text')




import discord
from discord.ext import commands
import os
import random


bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)



@bot.command('mem')
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command('penguin')
async def penguin(ctx):
    img_name = random.choice(os.listdir('img'))
    with open(f'img/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

bot.run('MTEzNTIwMDUwMDUxODc1MjM5OA.GX_4yd.EXDJ3VGW_6ePUaHhx3eNWKK28f69t2z72s6ow4')