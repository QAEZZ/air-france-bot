import discord
from discord.ext import commands


class Manifest(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def manifest(self, ctx, channel_id="MISSING", message_id="MISSING"):
        try:
            if channel_id == "MISSING" or message_id == "MISSING":
                await ctx.reply("**Please specify a channel ID and message ID.**")
                await ctx.reply(channel_id)
                await ctx.reply(message_id)
            else:
                channel_id = int(channel_id)
                message_id = int(message_id)

                channel = self.bot.get_channel(channel_id)
                message = await channel.fetch_message(message_id)
                users = set()
                for reaction in message.reactions:
                    async for user in reaction.users():
                        users.add(user)

                embed: discord.Embed = discord.Embed(
                    title="Manifest",
                    description='\n'.join(user.mention for user in users),
                    color=discord.Color.from_rgb(47, 49, 54)
                )

                await message.reply(embed=embed)
        except Exception as e:
            embed: discord.Embed = discord.Embed(
                    title=f"``{e}``", color=discord.Color.from_rgb(255, 100, 100)
            )
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Manifest(bot))
