@bot.command()
async def randommem(ctx):
      animal = random.choice(os.listdir('images'))
    with open(f'animals/{animal}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
