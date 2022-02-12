from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import argparse
import asyncio

parser = argparse.ArgumentParser(description="Discord Bot for Sakarya University BBF Discord Server")
parser.add_argument("-t","--token",required=True,help="Your Discord Bot Token")
parser.add_argument("-u","--username",required=True,help="Your Sabis username")
parser.add_argument("-p","--password",required=True,help="Your sabis password")
args = vars(parser.parse_args())
client = commands.Bot("!")
Token = args["token"]
username = args["username"]
password = args["password"]
liste = []

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
        
@client.command(name="duyuru")
async def on_message(ctx):
    if client.user == ctx.message.author:
        return
        
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://obs.sabis.sakarya.edu.tr/')
    driver.find_element(By.NAME,'Username').send_keys(username)
    driver.find_element(By.NAME,'Password').send_keys(password)
    driver.find_element(By.NAME,'button').click()
    time.sleep(5)
    while True:
        duyuru = driver.find_element(By.CLASS_NAME, 'timeline-item')
        liste.append(duyuru.text)
        driver.refresh()
        await asyncio.sleep(5)
        duyuru2 = driver.find_element(By.CLASS_NAME, 'timeline-item')
        liste.append(duyuru2.text)
        await asyncio.sleep(5)
        if liste[0] == liste[1]:
            await ctx.message.channel.send("@everyone")
            await ctx.message.channel.send(liste[1])
        liste.clear()
        driver.refresh()
        time.sleep(5)        

client.run(Token)
