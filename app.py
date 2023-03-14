from dotenv import load_dotenv
from discord.ext import commands
import discord
import openai
import time

# keep track of how many times we've asked a question
question_count = 0

# create a new discord bot instance
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

openai.api_key = "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"

# define a command that sends a message when triggered
@bot.command(name='ask')
async def askChatGPT(ctx):
    # count stuff
    global question_count
    question_count += 1
    # parse for the user's question 
    userMessage = ctx.message.content
    # strip away the !ask text
    question = userMessage[5:]
    # print the question asked to the channel 
    await ctx.send(f"{ctx.author} asked ChatGPT: \n```{question}```")

    # create a request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": question }]
    )

    # timeout may vary due to huge responses
    time.sleep(10)

    response = response.choices[0].message.content
    await ctx.send(f"ChatGPT said: \n```{response}```")

@bot.command(name='count')
async def countMethod(ctx):
    await ctx.send(f"{count}")

def main():
     # load environment variables
    load_dotenv()
    # run the bot
    bot.run('MTA4NDYwODQxNDkyMTAwMzA5OA.G0UywQ.t52Ws8jfXHM1EMwDYPYz7o0gJa9Dz98SSh4F_A')

if __name__ == '__main__':
    main()