import importlib
import os
import random
import json

from discord.ext import commands, tasks
from templates.status import status

prefix = ""
token = ""

with open("config.json", "r") as file:
  prefix = json.load(file)["prefix"]
  token = json.load(file)["token"]

client = commands.Bot(command_prefix=prefix)
client.remove_command("help")

# Set Status
async def set_status():
  options = status(prefix, client)
  option = random.choice(options)

  await client.change_presence(activity=option)

@client.event
async def on_ready():
  print("Ready!")
  loop.start()

@tasks.loop(minutes=50)
async def loop():
  await set_status()

commands = {}
command_files = [str(file)[:-3] for file in os.listdir('./commands') if file.endswith(".py")]

for file in command_files:
  command = importlib.import_module(f"commands.{file}")
  commands.update({command.name: command})

@client.event
async def on_message(message):
  if not message.content.startswith(prefix) or message.author.bot: return

  args = message.content[len(prefix):].strip().split()
  command = args[0].lower()

  args = args[1:]

  if commands.get(command) == None: return

  try:
    await commands.get(command).execute(message, args)

  except Exception as error:
    await message.channel.send(f'{message.author.mention}, There was an error trying to execute that command!')
    raise error

client.run(token)