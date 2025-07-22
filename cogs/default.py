import os
import discord
from discord.ext import commands

from core.custom_bot import CustomBot
from utils.welcome_banner import generate_welcome_banner

class DefaultCog(commands.Cog):
  def __init__(self, bot : CustomBot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member: discord.Member):
    welcome_channel = member.guild.get_channel(int(os.getenv('WELCOME_CHANNEL_ID')))
    welcome_banner = await generate_welcome_banner(member)
    
    if welcome_channel:
      file = discord.File(fp=welcome_banner, filename=f"welcome_{member.display_name}.png")
      embed = discord.Embed(title="Bienvenue dans la ruche mon ami(e) !")
      embed.set_image(url=f"attachment://welcome_{member.display_name}.png")

      await welcome_channel.send(embed=embed, file=file)

  @commands.command(name="join")
  async def join(self, ctx):
    await self.on_member_join(ctx.author)

async def setup(bot):
  await bot.add_cog(DefaultCog(bot))