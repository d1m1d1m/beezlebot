from discord.ext import commands

from core.custom_bot import CustomBot

class DeveloperCog(commands.Cog):
  def __init__(self, bot : CustomBot):
    self.bot = bot

  @commands.group(name="cogs", invoke_without_command=True)
  @commands.is_owner()
  async def cogs(self, ctx):
    await ctx.send("Utilise `!cogs --ls` pour lister ou `!cogs --reload <cog>` pour recharger.")

  @cogs.command(name="--ls")
  async def list_cogs(self, ctx):
    self.bot.extensions_manager.list_loaded()

  @cogs.command(name="--reload")
  async def reload_cog(self, ctx, cog_name: str):
    try:
      await self.bot.extensions_manager.reload(cog_name)
      await ctx.send(f"✅ Extension `{cog_name}` rechargée.")
    except Exception as e:
      await ctx.send(f"❌ Erreur lors du rechargement de `{cog_name}`:\n```{e}```")

  @cogs.command(name="--load")
  async def load_cog(self, ctx, cog_name: str):
    try:
      await self.bot.extensions_manager.load(cog_name)
      await ctx.send(f"✅ Extension `{cog_name}` chargée.")
    except Exception as e:
      await ctx.send(f"❌ Erreur lors du chargement de `{cog_name}`:\n```{e}```")

  @cogs.command(name="--unload")
  async def unload_cog(self, ctx, cog_name: str):
    try:
      await self.bot.extensions_manager.unload(cog_name)
      await ctx.send(f"✅ Extension `{cog_name}` déchargée.")
    except Exception as e:
      await ctx.send(f"❌ Erreur lors du déchargement de `{cog_name}`:\n```{e}```")

async def setup(bot):
  await bot.add_cog(DeveloperCog(bot))