import os
import discord
from discord.ext import commands

from core.extensions_manager import ExtensionsManager
from core.database_manager import DatabaseManager

class CustomBot(commands.Bot):
  def __init__(self, command_prefix, intents):
    super().__init__(command_prefix = command_prefix, intents = intents)

    self.extensions_manager = ExtensionsManager(self)
    self.database_manager   = DatabaseManager(self)

  async def setup_hook(self):
    await self.database_manager.connect()

    print("[EXT] - Manager opérationnel")
    await self.extensions_manager.load("default")
    await self.extensions_manager.load("developer")

  async def on_ready(self):
    print(f"✅ Connecté en tant que {self.user}")
    await self.tree.sync(guild=discord.Object(id=os.getenv('GUILD_ID')))

  async def close(self):
    await self.database_manager.close()
    await super().close()