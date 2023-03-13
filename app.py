import discord
from discord import Intents
from discord.ext import commands
import requests
import json
import os
from dotenv import load_dotenv

# Set the webhook URL
webhook_url = 'https://hook.us1.make.com/lw7k8jkk1deqer77zcq9s6kvf1r7941c'

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
bot.run('MTA4NDYwODQxNDkyMTAwMzA5OA.GIOZss.4sNp99bpTorPwyVx4PVIuBJC30a5Q2-Q6hxnI0')