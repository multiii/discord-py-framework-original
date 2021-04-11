import discord

def embed(title, text, user, image_url = None):
  embed = discord.Embed(
      color = 0x81a1c1,
      title = title,
      description = text
  )

  embed.set_footer(text = f"Requested by {user.name}#{user.discriminator}", icon_url = user.avatar_url)
  
  if image_url != None:
    embed.set_image(url = image_url)

  return embed