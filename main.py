# author: Max Carter
# date:   25/11/18
# Sends the top posts from /r/ProgrammerHumor to a discord channel.

#import modules
from discord import *
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import praw

#setting up reddit account
reddit = praw.Reddit(client_id = "",
                     client_secret = "",
                     username = "",
                     password = "",
                     user_agent = "")

#setting up subreddit
subreddit = reddit.subreddit("ProgrammerHumor")

posted_memes = []

#setting up the bot on discord
bot = commands.Bot(command_prefix = "!")

#when the bot starts
@bot.event
async def on_ready():
    print("bot ready")

#when a meme is requested
@bot.command(pass_context=True)
async def meme(message):
    posts = subreddit.hot(limit=100)
    for submission in posts:
        if not submission.stickied and not submission in posted_memes:
            await bot.say(submission.url)
            await bot.say(submission.title)
            posted_memes.append(submission)
            return
    
    
#running bot on discord
bot.run("")
