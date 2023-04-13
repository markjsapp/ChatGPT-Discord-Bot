from discord.ext import commands
from dotenv import load_dotenv
import discord
import openai
import threading
import time
import os

# keep track of how many times we've asked a question
question_count = 0

# for threading
last_response = {}

# create a new discord bot instance
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

openai.api_key = os.environ.get('OPEN_API_KEY')

# sends a message 
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

    # use threading to handle each user's question
    thread = threading.Thread(target=handle_question, args=(ctx.author.id, question, ctx.channel.id))
    thread.start()

# method that 
@bot.command(name='count')
async def countMethod(ctx):
    await ctx.send(f"{question_count}")

def handle_question(user_id, question, channel_id):
    global last_response
    try:
        # check if this user has asked a question before
        if user_id in last_response:
            # check if the previous response was less than 10 seconds ago
            if time.time() - last_response[user_id]['timestamp'] < 10:
                # send the cached response instead of making a new request
                response = last_response[user_id]['response']
                send_response(response, channel_id)
                return
        # make a new request
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": question }]
        )

        time.sleep(10)
        
        actual_response = response.choices[0].message.content

        # cache the response for this user
        last_response[user_id] = {'response': actual_response, 'timestamp': time.time()}
        send_response(actual_response, channel_id)
    except Exception as e:
        # handle errors
        print(f"Error handling question from user {user_id}: {e}")

def send_response(response, channel_id):
    # send the response to the channel
    bot.loop.create_task(bot.get_channel(channel_id).send(f"ChatGPT said: \n```{response}```"))

def main():
     # load environment variables
    load_dotenv()
    # run the bot
    bot.run(os.environ.get('DISCORD_KEY'))

if __name__ == '__main__':
    main()