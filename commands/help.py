import importlib
import os
from templates import complete_embed

command_files = [str(file)[:-3] for file in os.listdir('./commands') if file.endswith(".py")]

name = 'help'
description = 'Display the help menu'

async def execute(message, args):
  desc = "";
  for file in command_files:
    command = importlib.import_module(f"commands.{file}")
    desc += f"**`{command.name}`** - {command.description}\n"

  await message.channel.send(embed = complete_embed.embed('Help Menu', desc, message.author))