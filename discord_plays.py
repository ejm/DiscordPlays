#!/usr/bin/env python3

import asyncio
import discord
import keyboard
import json
import os

config = {}
bot = discord.Client()
queue_ = asyncio.Queue()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.guild.id != config["server"]:
        return
    if message.channel.id != config["channel"]:
        return
    key = message.content.lower()
    if key not in config["allowed_keys"]:
        return
    await queue_.put(config["allowed_keys"][key])

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    if "game" in config:
        game = discord.Game(config["game"])
        await bot.change_presence(activity=game)
    asyncio.create_task(worker())

async def worker():
    while True:
        key = sleep_for = await queue_.get()
        keyboard.send(key)
        await asyncio.sleep(.1)
        queue_.task_done()

if __name__ == "__main__":
    config_file = os.environ.get("DISCORD_PLAYS_CONFIG", "config.json")
    with open(config_file) as f:
        config = json.load(f)
    bot.run(config["token"])