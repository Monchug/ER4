import discord
from discord.ext import commands
from discord.utils import get
from selenium import webdriver
from selenium.webdriver.common.by import By

client = commands.Bot("!")
Token = ""
username = ""
password = ""

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
@client.command(name="bsmg")
async def on_message(ctx):
    if client.user == ctx.message.author:
        return
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get("http://obs.sabis.sakarya.edu.tr/Ders/Grup/655940")
    driver.find_element(By.NAME,"Username").send_keys(username)
    driver.find_element(By.NAME,"Password").send_keys(password)
    driver.find_element(By.NAME,"button").click()

    duyuru = driver.find_element(By.CLASS_NAME,"timeline-items")
    print(duyuru.text)
    
    await ctx.message.channel.send(duyuru.text[0:2000])
    await ctx.message.channel.send(duyuru.text[2000:])
    driver.quit()
client.run(Token)
