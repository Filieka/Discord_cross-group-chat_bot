import discord
from discord.ext import commands,tasks 
import json
import os
import keep_alive
from itertools import cycle

with open('setting.json', 'r', encoding='utf8') as jFile:
    jdata = json.load(jFile)

intents = discord.Intents.all()

#機器人的前綴是 = 
bot = commands.Bot(command_prefix='!!', intents = intents)

status = cycle([
  "!!help"
])

@tasks.loop(seconds=1)
async def status_swap():
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.event
async def on_ready():
    print(">> Bot is online <<")   
    for guild in bot.guilds:

        print('Active in {}\n Member Count : {}'.format(guild.name,guild.member_count))

    status_swap.start() 

@bot.command(aliases=["as","a_s","AS","A_S"])
async def add_server(ctx, channel_id):        
    with open('s.json', 'r', encoding='utf8') as jfile:
        jdata = json.load(jfile)
    
    
    with open('s.json', 'w', encoding='utf8') as jfile:
        jdata["ids"].append(f"{channel_id}")
        jfile.seek(0)

        json.dump(jdata, jfile, indent = 8)
    #    json.dump({'id': f"{channel_id}"}, jfile, indents=4)
    await ctx.send("成功喔")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'UnLoaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'ReLoaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    #keep_alive.keep_alive()    
    bot.run(jdata['TOKEN'])