import datetime 
import random
import discord
import time
import json
from pathlib import Path

from discord import ui
from discord.ext import commands
from discord.ui import View, Button


class atisModal(ui.Modal, title="Create ATIS Report Dialog"):
    try:
        phonetic_alpha = ui.TextInput(label="Phonetic Alpha", style=discord.TextStyle.short,
                                placeholder="Ex. Alpha, Bravo, Charlie, Etc.", required=True)
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
                description=f"""```fix
{self.atis_information}```"""
            )
            file = Path(f"./atis/{self.airport_code} - Information {self.phonetic_alpha}.json")
            file.touch(exist_ok=True)
            atis_file = open(f"./atis/{self.airport_code} - Information {self.phonetic_alpha}.json")
            atis_dict = {
                "phonetic_alpha": self.phonetic_alpha,
                "airport_code": self.airport_code,
                "atis_information": self.atis_information
            }
            to_write = json.loads(atis_dict)
            atis_file.write(to_write)
            atis_file.close()

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

        if self.airport.lower() == "example":
            try:

                embed: discord.Embed = discord.Embed(
                    title=f"Information {get_code().capitalize()} for EXAMPLE AIRPORT",
                    color=self.eColor,
                    description="""```fix
GREATER ROCKFORD INFORMATION SIERRA.
WEATHER MEASURED CEILING TEN THOUSAND PARTLY CLOUDY.
VISIBILITY SIX NAUTICAL MILES, CLEAR.
TEMPERATURE SIX EIGHT. DEWPOINT FOUR THREE.
WIND THREE FIVE ZERO AT EIGHT.
ALTIMETER TWO NINER NINER TWO.
ILS RUNWAY THREE SIX RIGHT APPROACH IN USE.
LANDING RUNWAY THREE SIX RIGHT AND LEFT, DEPARTURE RUNWAY THREE SIX RIGHT AND LEFT.
CAUTION TERRAIN ON APPROACH PLATE.

ADVISE YOU HAVE INFORMATION SIERRA.```"""
                )

                await ctx.reply(embed=embed)
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
