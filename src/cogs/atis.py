import datetime 
import random
import discord
import time

from discord import ui
from discord.ext import commands
from discord.ui import View, Button


class atisModal(ui.Modal, title="Create ATIS Report Dialog"):
    try:
        phonetic_alpha = ui.TextInput(label="Phonetic Alpha", style=discord.TextStyle.short,
                                placeholder="Ex. Alpha, Bravo, Charlia, Etc.", required=True)
        airport_code = ui.TextInput(label="Airport ICAO Code", style=discord.TextStyle.short,
                                placeholder="Ex. IFRD, IPPH, Etc.", required=True)
        atis_information = ui.TextInput(label="ATIS Information", style=discord.TextStyle.long,
                                placeholder="Information that is included in ATIS reports. Do NOT include the airport name or time. ", required=True)

    except Exception as e:
        print(e)
    
    async def on_submit(self, interaction: discord.Interaction):
        try:

            embed: discord.Embed = discord.Embed(
                title=f"Information {self.phonetic_alpha} for {self.airport_code}.\n<t:{int(time.time())}:f> local",
                color=discord.Color.from_rgb(47, 49, 54),
                description=f"```{self.atis_information}```"
            )
            await interaction.response.send_message(embed=embed)
        
        except Exception as e:
            print(e)


def get_code():
    alpha_list = [
        "alpha",
        "bravo",
        "charlie",
        "delta",
        "echo",
        "foxtrot",
        "golf",
        "hotel",
        "india",
        "juliet",
        "kilo",
        "lima",
        "mike",
        "november",
        "oscar",
        "papa",
        "quebec",
        "romeo",
        "sierra",
        "tango",
        "uniform",
        "victor",
        "whiskey",
        "xray",
        "yankee",
        "zulu"
    ]
    
    return random.choice(alpha_list)


class ATIS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def atis(self, ctx, airport: str = "MISSING"):
        self.airport = airport
        if self.airport == "MISSING":
            await ctx.reply("``Please define an airport via ICAO code!``")
        
        if self.airport.lower() == "create":

            try:

                async def create_atis_callback(interaction):
                    await ctx.message.delete()
                    await msg.delete()
                    await interaction.response.send_modal(atisModal())

                create_atis = Button(label="Click to create an ATIS report!", style=discord.ButtonStyle.green)

                view = View(timeout=300)

                create_atis.callback = create_atis_callback

                view.add_item(create_atis)

                msg = await ctx.reply(view=view)
            
            except Exception as e:
                print(e)

        else:
            embed: discord.Embed = discord.Embed(
                title=f"Information \"{get_code()}\" for {self.airport.upper()}", color=self.eColor
            )
            embed.set_footer(text="Soon™")
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(ATIS(bot))
