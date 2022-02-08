import discord
from discord.ext import commands
from discord.utils import get
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

client = commands.Bot("!")
Token = ""
username = ""
password = ""
bsmg = []
a = []
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
    #driver.find_element(By.NAME,'Username').send_keys(username)
    #driver.find_element(By.NAME,'Password').send_keys(password)
    #driver.find_element(By.NAME,'button').click()
    driver.get('https://dcbotdeneme.blogspot.com/2022/02/deneme.html')
    while True:

        duyuru = driver.find_element(By.CLASS_NAME, 'post-outer')
        bsmg.append(duyuru.text)
        driver.refresh()
        time.sleep(10)
        driver.refresh()
        duyuru2 = driver.find_element(By.CLASS_NAME, 'post-outer')
        bsmg.append(duyuru2.text)
        if bsmg[0] != bsmg[1]:
            await ctx.message.channel.send(bsmg[1])
        bsmg.clear()
        driver.refresh()
        time.sleep(10)

@client.command(name="a")
async def on_message(ctx):
    if client.user == ctx.message.author:
        return
        
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    #driver.find_element(By.NAME,'Username').send_keys(username)
    #driver.find_element(By.NAME,'Password').send_keys(password)
    #driver.find_element(By.NAME,'button').click()
    driver.get('https://dcbotdeneme.blogspot.com/2022/02/deneme2.html')
    while True:

        duyuru = driver.find_element(By.CLASS_NAME, 'post-outer')
        a.append(duyuru.text)
        driver.refresh()
        time.sleep(10)
        driver.refresh()
        duyuru2 = driver.find_element(By.CLASS_NAME, 'post-outer')
        a.append(duyuru2.text)
        if a[0] != a[1]:
            await ctx.message.channel.send(a[1])
        a.clear()
        driver.refresh()
        time.sleep(10)

client.run(Token)
