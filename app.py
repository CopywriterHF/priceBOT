from discord.ext import commands
import requests

description = '''A Discord Bitcoin Price Bot example.'''
bot = commands.Bot(command_prefix='/', description=description)

BOT_USER_TOKEN = "YOUR_BOT_USER_TOKEN"

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def btc(currency : str):
    """fetches bitcoin price."""
    url = 'https://blockchain.info/ticker'
    resp = requests.get(url)
    btc = resp.json()[currency]
    await bot.say(btc['symbol'] + ' ' + str(btc['last']))

bot.run(BOT_USER_TOKEN)
