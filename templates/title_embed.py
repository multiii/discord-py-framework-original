import discord

def embed(title, text):
    return discord.Embed(
      color = 0x81a1c1,
      title = title,
      description = text
    )