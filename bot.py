import random
import requests
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=".hn ", intents=intents, help_command=None)

@client.event
async def on_ready():
    print('bot ready')
    
@client.command()
async def help(ctx):
    help = discord.Embed(title="Help commands", description=".hn best for beststories\n.hn top for topstories\n.hn new for newstories")
    await ctx.send(embed=help)

@client.command()
async def best(ctx):
    r = requests.get("https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty")
    res = r.json()
    itemnum = random.randint(0,200)
    item = str(res[itemnum])
    await ctx.send("https://news.ycombinator.com/item?id="+item)

@client.command()
async def top(ctx):
    r = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
    res = r.json()
    itemnum = random.randint(0,500)
    item = str(res[itemnum])
    await ctx.send("https://news.ycombinator.com/item?id="+item)

@client.command()
async def new(ctx):
    r = requests.get("https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty")
    res = r.json()
    itemnum = random.randint(0,500)
    item = str(res[itemnum])
    await ctx.send("https://news.ycombinator.com/item?id="+item)

client.run(TOKEN)
