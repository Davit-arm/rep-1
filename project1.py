import discord
import random, string
from discord.ext import commands
import os
import requests
from password import generate_password

print(os.listdir('images'))



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
#hi
@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
#help
@bot.command()
async def help1(ctx):
    await ctx.send('''hello - privet
                      heh(how much heh you want) - for bot to laugh
                      normal_can- what can be thrown in normal cans
                      recycle_bin - what can be thrown in recycle bins
                      help1 - all commands will be here!
                    dont forget to use the prefix($) before typing in the command!''')
#eco

@bot.command()
async def normal_can(ctx):
    await ctx.send(f'''# Что можно выбрасывать в обычную урну
# 1.Органические отходы

## -Остатки пищи (если нет компостной системы).
## -Бумажные полотенца, салфетки (если они загрязнены).
## -Чайные пакетики и кофейная гуща (без упаковки).
                   
# 2.Загрязнённая упаковка:

## -Бумага c жирными пятнами например: коробки от пиццы.
## -Пластиковая упаковка, загрязнённая пищей (если её нельзя очистить).
                   
# 3.Мелкий бытовой мусор:

## -Одноразовые подгузники.
## -Гигиенические изделия.
## -Сигаретные окурки.
## -Лампочки накаливания но не (энергосберегающие или светодиодные).
                   
# 4.Мелкий пластик:

## -Пакеты от чипсов, конфет и другая упаковка, не пригодная для переработки.''')
    

@bot.command()
async def recycle_bin(ctx):
    await ctx.send(f'''Что стоит отправить на переработку:
# 1.Бумага и картон:

## -Чистая бумага (газеты, журналы, офисная бумага).
## -Чистые картонные коробки (разделить и сложить).
## -Книги (без пластиковых обложек).
                   
# 2.Пластик:

## -Пластиковые бутылки и упаковка c маркировкой переработки (например, PET 1, HDPE 2, LDPE 4 и т.д.).
## -Чистые пластиковые контейнеры (например, от йогурта, пищевых продуктов).
## -Пакеты и плёнка (если принимаются на переработку, уточняйте y локальных служб).
                   
# 3.Стекло:

## -Стеклянные бутылки и банки (обязательно чистые).
## -Стеклянная тара (без крышек и колпачков).
                   
# 4.Металл:

## -Алюминиевые банки и жестяные банки (очищенные от остатков еды).
## -Металлические крышки от стеклянных банок.
                   
# 5.Тетрапаки (упаковка для сока, молока):
                   
## -Эту упаковку можно перерабатывать, но она требует специального подхода, поэтому нужно узнать, принимают ли её на переработку в вашем регионе.

# 6.Электроника и батарейки:

## -В специализированные пункты нужно сдавать батарейки, аккумуляторы, электронику (старые телефоны, компьютеры).

# 7.Одежда и текстиль:
## -В пункты приёма текстиля можно сдать одежду, обувь, постельное бельё.
                   

# Что ни в коем случае нельзя выбрасывать в обычный мусор:
## -Батарейки и аккумуляторы (выделяют токсичные вещества).
## -Лекарства (сдавать в аптеки, которые принимают старые медикаменты).
## -Энергосберегающие лампы и светодиодные лампочки (они содержат ртуть).
## -имикаты, лакокрасочные материалы, ртутные термометры.''')
    
#generate
@bot.command()
async def generate(ctx, length: int = 8):
    await ctx.send(f"Generated password: {generate_password(length)}")

#photos
@bot.command()
async def mem(ctx):
    with open('images/meme.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def randommem(ctx):
    image = random.choice(os.listdir('images'))
    with open(f'images/{image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)





bot.run('mytoken')
