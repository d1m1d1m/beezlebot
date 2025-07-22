import os
import discord
from dotenv import load_dotenv
from core.custom_bot import CustomBot

# Load .env file
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

beezle_bot = CustomBot('!', intents)
beezle_bot.run(os.getenv('DISCORD_BOT_TOKEN'))