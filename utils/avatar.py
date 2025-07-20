from PIL import Image, ImageDraw

def make_rounded_avatar(avatar_img: Image.Image, size=(144, 144)) -> Image.Image:
  avatar_img = avatar_img.resize(size).convert("RGBA")
  
  mask = Image.new("L", size, 0)
  draw = ImageDraw.Draw(mask)
  draw.ellipse((0, 0) + size, fill=255)
  
  rounded_avatar = Image.new("RGBA", size)
  rounded_avatar.paste(avatar_img, (0, 0), mask)
  
  return rounded_avatar