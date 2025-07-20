import io
import discord
from PIL import Image, ImageDraw, ImageFont
from discord.ext import commands

from utils.avatar import make_rounded_avatar

class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="ping")
  async def ping(self, ctx):
    await ctx.send("🏓 Pong !")

  @commands.Cog.listener()
  async def on_member_join(self, member: discord.Member):
    member_name = member.name;
    # Charger template
    base = Image.open('assets/welcome.png').convert("RGBA")
    draw = ImageDraw.Draw(base)

    # Avatar
    avatar_asset = member.avatar or member.default_avatar
    avatar_bytes = await avatar_asset.read()

    avatar_image = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA")
    rounded_avatar = make_rounded_avatar(avatar_image)

    # Avatar sur base
    base.paste(rounded_avatar, (94, 216), rounded_avatar)

    # Texte
    font = ImageFont.truetype("assets/Jersey10-Regular.ttf", 36)
    draw.text((124, 110), f">>> INSERT INTO member VALUES ('{member_name}');", font=font, fill=(63, 28, 8))

    font = ImageFont.truetype("assets/Jersey10-Regular.ttf", 64)
    draw.text((287, 219), f"Bienvenue sur le discord".upper(), font=font, fill=(255, 255, 255))

    font = ImageFont.truetype("assets/Jersey10-Regular.ttf", 64)
    draw.text((287, 288), member.guild.name, font=font, fill=(255, 255, 255))

    buffer = io.BytesIO()
    base.save(buffer, format="PNG")
    buffer.seek(0)

    channel_id = "welcome channel id here"
    channel = member.guild.get_channel(channel_id)

    if channel:
      file = discord.File(fp=buffer, filename="welcome.png")
      await channel.send(file=file)

  @commands.command(name="join")
  async def join(self, ctx):
    await self.on_member_join(ctx.author)

async def setup(bot):
  await bot.add_cog(General(bot))