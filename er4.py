import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot("!")

Token = ""

@client.event
async def on_ready():  
    print(f"{client.user} botu Discorda bağlandı!\n")

@client.command(name="clear")
async def clear(ctx, number=50):
    await ctx.channel.purge(limit=number)
    
@client.command(name="emoji")
async def on_message(ctx):
    if client.user  == ctx.message.author:
        return

    #if ctx.message.attachments[0].url.endswith('PNG') or ctx.message.attachments[0].url.endswith('JPG') or ctx.message.attachments[0].url.endswith('JPEG'):
    await ctx.message.add_reaction("🇦")
    await ctx.message.add_reaction("🇧")
    await ctx.message.add_reaction("🇨")
    await ctx.message.add_reaction("🇩")
    await ctx.message.add_reaction("🇪")

client.run(Token)