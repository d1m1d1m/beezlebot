import os
import discord
from discord.ext import commands

class BeezleBot(commands.Bot):
  def __init__(self, command_prefix, intents):
    super().__init__(command_prefix = command_prefix, intents = intents)

    self.mode = os.getenv('ENVIRONMENT_MODE')
    self.guild_id = os.getenv('GUILD_ID')

  async def setup_hook(self):
    extensions = [ "cogs.general" ]

    for ext in extensions:
      try:
        await self.load_extension(ext)
        print(f"🟢 Extension chargée : {ext}")
      except Exception as e:
        print(f"🔴 Erreur lors du chargement de {ext} : {e}")

  async def on_ready(self):
    print(f"✅ Connecté en tant que {self.user} (ID: {self.user.id})")
    await self.tree.sync(guild=discord.Object(id=self.guild_id))