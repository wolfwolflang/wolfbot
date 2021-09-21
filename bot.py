import discord
from discord import channel
from discord.ext import commands
from discord.utils import async_all

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> bot is online <<")

@bot.event
async def on_member_join(member):
    print(F'{member} join!')
    channel = bot.get_channel(853170882263646259)
    await channel.send(F'{member} 加入了狼之國')

@bot.event
async def on_member_remove(member):
    print(F'{member} leave!')
    channel = bot.get_channel(853170882263646259)
    await channel.send(F'{member} sad! 離開了狼之國')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)} 毫秒ms')

bot.run("ODg4MzY2OTQ1MTkwMTc4ODI2.YURqMA.FCO60O9L4BXh8hKyZPEBu_9OS_Q")

