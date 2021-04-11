from templates import complete_embed

name = 'test'
description = 'Testing the bot'

async def execute(message, args):
  await message.channel.send(embed = complete_embed.embed('Testing', '**Test Successful**', message.author))