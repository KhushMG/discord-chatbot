import discord
import os
from dotenv import load_dotenv
import openai
import random
# imports

load_dotenv()


TOKEN = os.getenv("DISCORD_TOKEN")
API_KEY = os.getenv("OPENAI_KEY")

openai.api_key = os.getenv("OPENAI_KEY")
openai.Model.list()

client = discord.Client(intents=discord.Intents.all())

def get_chat_response(message):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": 
             '''You are a passive-aggressive but helpful assistant
             who is familiar with manga/anime but doesn't feel the need
             to bring it up when not necessary
             .'''
             },
            {"role": "user", "content": message},
        ],
    )

    try:
        bot_response = response['choices'][0]['message']['content']
    except KeyError as e:
        print("Error accessing response:", e)
        bot_response = "Error generating response"

    return bot_response


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif (
        "happy birthday" in message.content.lower()
        or "happy bday" in message.content.lower()
    ):
        user_input = message.content[6:]  # Remove '!chat ' from the message
        user_input = "happy birthday phrase"
        bot_response = get_chat_response(user_input)
        await message.channel.send(bot_response)
    elif "balls" in message.content.lower():
        # user_input = message.content[6:]  # Remove '!chat ' from the message
        # user_input = "make a random sentence which includes balls"
        # bot_response = get_chat_response(user_input)
        await message.channel.send(random.choice(['i\'m balls', 'Oy! Balls!', 'Balls!!!','I LOVE BALLS!!',
                                                  'HUGE BALLS!']))    
    elif "bro" in message.content.lower():
        user_input = message.content[6:]  # Remove '!chat ' from the message
        user_input = "frat bro phrase"
        bot_response = get_chat_response(user_input)
        await message.channel.send(bot_response)
    elif message.content.startswith("!chat"):
        user_input = message.content[6:]  # Remove '!chat ' from the message
        bot_response = get_chat_response(user_input)
        await message.channel.send(bot_response)

client.run(TOKEN)