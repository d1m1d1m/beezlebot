import discord
import io
from PIL import Image, ImageDraw, ImageFont

def make_rounded_avatar(avatar_img: Image.Image, size=(144, 144)) -> Image.Image:
  avatar_img = avatar_img.resize(size).convert("RGBA")
  
  mask = Image.new("L", size, 0)
  draw = ImageDraw.Draw(mask)
  draw.ellipse((0, 0) + size, fill=255)
  
  rounded_avatar = Image.new("RGBA", size)
  rounded_avatar.paste(avatar_img, (0, 0), mask)
  
  return rounded_avatar

async def generate_welcome_banner(member : discord.Member):
  # TEMPLATE
  base = Image.open('assets/img/welcome.png').convert("RGBA")
  draw = ImageDraw.Draw(base)

  # AVATAR
  avatar_asset = member.avatar or member.default_avatar
  avatar_bytes = await avatar_asset.read()

  avatar_image = Image.open(io.BytesIO(avatar_bytes)).convert("RGBA")
  rounded_avatar = make_rounded_avatar(avatar_image)

  base.paste(rounded_avatar, (94, 216), rounded_avatar)

  # WINDOW TITLE
  font = ImageFont.truetype("assets/fonts/Jersey10-Regular.ttf", 36)
  draw.text((124, 110), f">>> INSERT INTO member VALUES ('{member.display_name}');", font=font, fill=(63, 28, 8))

  # WELCOME MESSAGE
  font = ImageFont.truetype("assets/fonts/Jersey10-Regular.ttf", 64)
  draw.text((287, 219), f"Bienvenue sur le discord".upper(), font=font, fill=(255, 255, 255))

  # GUILD NAME
  font = ImageFont.truetype("assets/fonts/Jersey10-Regular.ttf", 64)
  draw.text((287, 288), "Beezell & Co(de)", font=font, fill=(255, 255, 255))

  buffer = io.BytesIO()
  base.save(buffer, format="PNG")
  buffer.seek(0)

  return buffer