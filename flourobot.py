# Work with Python 3.6
import random
import asyncio
import aiohttp
import json
#from discord import Game
from discord.ext.commands import Bot
from googlesearch import search
from googletrans import Translator

BOT_PREFIX = ("/")
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


#@client.event
#async def on_ready():
#    await client.change_presence(game=Game(name="i miss orange juice"))
#    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

@client.command()
async def guess(number):
    lunathecat1212112 = (random.randint(0, 10))
    if number == lunathecat1212112:
        await client.say("Amazing! You guessed it! Have a gold star. :star:")
    if number != lunathecat1212112:
        await client.say("Wrong!")
        return(lunathecat1212112)

@client.command()
async def g(tearm):
    for url in search(tearm, stop=5):
        await client.say(url)

@client.command()
async def about():
    await client.say('''
/t "language" "message" | Language is the language to translate into (use the abbreviations in this list: https://en.wikipedia.org/wiki/ISO_639-1) and message is the message to translate. Include the quotes.
/8ball | Roll the 8 ball.
/square x | Square the number x
/bitcoin | Display current bitcoin value in USD
/guess x | Try to guess a number from 0 to 100. Put your guess in the x spot.
/g tearm | Google something. Put your search tearm in the "tearm" spot.
/about | Sends this message.

Code:
Basic structure: DevDungeon
All other programming: @flouroantimonic_acid#7707
Join our discord server! https://discord.gg/BaENmRW
''')

@client.command()
async def woah():
    await client.say('''
( ͡° ͜ʖ ͡° )
    ( (   ͡° ͜ʖ ͡° )
   (   (   ͡° ͜ʖ ͡° )
  (   ͡° (   ͡° ͜ʖ ͡ ° )
 (   ͡° ͜ʖ (   ͡° ͜ʖ ͡° )
(   ͡° ͜ʖ ͡° (   ͡° ͜ʖ ͡° )
(   ͡° ͜ʖ ͡° ) (   ͡° ͜ʖ ͡° )
(   ͡° ͜ʖ ͡° )  (   ͡° ͜ʖ ͡° )
(   ͡° ͜ʖ ͡° ) (   ͡° ͜ʖ ͡° )
 (   ͡° ͜ʖ ͡° ) ͡° ͜ʖ ͡° )
  (   ͡° ͜ʖ ͡° ) ͜ʖ ͡° )
   (   ͡° ͜ʖ ͡° ) ͡° )
    (   ͡° ͜ʖ ͡° )° )
     (   ͡° ͜ʖ ͡° ))
      (   ͡° ͜ʖ ͡°)
    ( (   ͡° ͜ʖ ͡° )
   (   (   ͡° ͜ʖ ͡° )
  (   ͡° (   ͡° ͜ʖ ͡° )
 (   ͡° ͜ʖ (   ͡° ͜ʖ ͡° )
(   ͡° ͜ʖ ͡° (   ͡° ͜ʖ ͡° )
(   ͡° ͜ʖ ͡° ) (   ͡° ͜ʖ ͡° )
(   ͡° ͜ʖ ͡° )  (   ͡° ͜ʖ ͡° )
(   ͡° ͜ʖ ͡° ) (   ͡° ͜ʖ ͡° )
 (   ͡° ͜ʖ ͡° ) ͡° ͜ʖ ͡° )
  (   ͡° ͜ʖ ͡° ) ͜ʖ ͡° )
   (   ͡° ͜ʖ ͡° ) ͡° )
    (   ͡° ͜ʖ ͡° )° )
     (   ͡° ͜ʖ ͡° )
    ( (   ͡° ͜ʖ ͡° )
   (   (   ͡° ͜ʖ ͡° )
  (   ͡° (   ͡° ͜ʖ ͡° )
 (   ͡° ͜ʖ (   ͡° ͜ʖ ͡° )
(   ͡° ͜ʖ ͡° (   ͡° ͜ʖ ͡° )
(   ͡° ͜ʖ ° ) (   ° ʖ ° )
(   ° ʖ ° )  (   ° ʖ ° )
(   ° ʖ ° ) (   ° ʖ ° )
 (   ° ʖ ° ) ° ʖ ° )
  (   ° ʖ ° ) ʖ ° )
   (   ° ʖ ° ) ° )
    (   ° ʖ ° )° )
      ( ° ʖ ° )
    ( (   ° ʖ ° )
   (   (   ° ʖ ° )
  (   ° (   ° ʖ  ° )
 (   ° ʖ (   ° ʖ ° )
(   ° ʖ ° (   ° ʖ ° )
(   ° ʖ ° ) (   ° ʖ ° )
(   ° ʖ ° )  (   ° ʖ ° )
(   ° ʖ ° ) (   ° ʖ ° )
 (   ° ʖ ° ) ° ʖ ° )
  (   ° ʖ ° ) ʖ ° )
   (   ° ʖ ° ) ° )
    (   ° ʖ ° )° )
     (   ° ʖ ° ))
      (   ° ʖ °)
    ( (   ° ʖ ° )
   (   (   ° ʖ ° )
  (   ° (   ° ʖ ° )
 (   ° ʖ (   ° ʖ ° )
(   ° ʖ ° (   ° ʖ ° )
(   ° ʖ ° ) (   ° ʖ ° )
(   ° ʖ ° )  (   ° ʖ ° )
(   ° ʖ ° ) (   ° ʖ ° )
 (   ° ʖ ° ) ° ʖ ° )
  (   ° ʖ ° ) ʖ ° )
   (   ° ʖ ° ) ° )
    (   ° ʖ ° )° )
     (   ° ʖ ° )
    ( (   ° ʖ ° )
   (   (   ° ʖ ° )
  (   ° (   ° ʖ ° )
 (   ° ʖ (   ° ʖ ° )
(   ° ʖ ° (   ° ʖ ° )
(   ° ʖ ° ) (   ° ʖ ° )
(   ° ʖ ° )  (   ° ʖ ° )
(   ° ʖ ° ) (   ° ʖ ° )
 (   ° ʖ ° ) ° ʖ ° )
  (   ° ʖ ° ) ʖ ° )
   (   ° ʖ ° ) ° )
    (   ° ʖ ° )° )
''')

@client.command()
async def t(message):
    translation = Translator().translate(message, dest='en')
    await client.say(translation.text)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        print("--------------------------------")
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
