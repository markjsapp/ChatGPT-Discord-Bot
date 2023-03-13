import discord
from discord import Intents
from discord.ext import commands
import requests
import json
import os
from dotenv import load_dotenv

# Set the webhook URL
webhook_url = os.getenv('WEBHOOK_KEY')

# create a new bot instance
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# define a command that sends a message when triggered
@bot.command(name='ask')
async def askChatGPT(ctx, question):
    await ctx.send(f"{question.author} asked ChatGPT: {question}")

    payload = {
    "question": question
    }

    # Make the HTTP request
    response = requests.post(webhook_url, json=payload)

    if response.status_code == 200:
        await ctx.send("Question was sent successfully! Waiting on response...")
    else:
        await ctx.send("Webhook POST request failed...")

# run the bot
bot.run(os.getenv('DISCORD_KEY'))