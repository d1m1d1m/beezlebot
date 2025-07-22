from discord.ext import commands

class ExtensionsManager:
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  async def load(self, name: str):
    try:
      await self.bot.load_extension(f"cogs.{name}")
      print(f"✅ Extension '{name}' chargée.")
    except Exception as e:
      print(f"❌ Erreur au chargement de '{name}': {e}")

  async def unload(self, name: str):
    try:
      await self.bot.unload_extension(f"cogs.{name}")
      print(f"🔻 Extension '{name}' déchargée.")
    except Exception as e:
      print(f"❌ Erreur au déchargement de '{name}': {e}")

  async def reload(self, name: str):
    try:
      await self.bot.reload_extension(f"cogs.{name}")
      print(f"♻️ Extension '{name}' rechargée.")
    except Exception as e:
      print(f"❌ Erreur au rechargement de '{name}': {e}")

  def list_loaded(self) -> list[str]:
    return list(self.bot.extensions.keys())