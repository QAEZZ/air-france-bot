import datetime 
import random
import discord
import time
import json
from pathlib import Path

from discord import ui, FFmpegPCMAudio
from discord.ext import commands
from discord.ui import View, Button


class ATISVC(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)


    @commands.command(pass_context = True)
    async def join(ctx):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio("atis.mp3")
            player = voice.play(source)
            await ctx.send("Connected on target channel")
        else:
            await ctx.send("Please join the target voice channel")

    """
    @commands.command(pass_context = True)
    async def play(ctx):
        if ctx.voice_client:
            # voice stuff here
    """

    @commands.command(pass_context = True)
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
            await ctx.send("Disconnected from the voice channel.")
        else:
            await ctx.send("I am not in a voice channel")


async def setup(bot):
    await bot.add_cog(ATISVC(bot))
