import discord
from discord.ext import commands
from discord.utils import get
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

client = commands.Bot("!")
Token = "OTIyODYwODE2MDc0NjkwNTcw.YcHnHA.2s3sSgzJgjjDOX9CeiT9XYG9YmE"
username = "b201200007"
password = "s5f5M7az"

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

    while True:

        driver.get('https://obs.sabis.sakarya.edu.tr/Ders/Grup/655940')
        duyuru = driver.find_element(By.CLASS_NAME,'timeline-content')
        time.sleep(5)
        driver.get('https://obs.sabis.sakarya.edu.tr/Ders/Grup/655940')
        duyuru2 = driver.find_element(By.CLASS_NAME,'timeline-content')
        if duyuru != duyuru2:
            await ctx.message.channel.send("@everyone")
            await ctx.message.channel.send(duyuru2.text)

@client.command(name="a")
async def on_message(ctx):
    if client.user == ctx.message.author:
        return
    await ctx.message.channel.send("@everyone")
    
client.run(Token)
