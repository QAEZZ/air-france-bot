import discord

import datetime

from discord import ui
from discord.ext import commands
from discord.ui import View, Button

global fpinteraction
global fpmessage

"""
Callsign: AirFrans-4633
Aircraft: Concorde
IFR/VFR: IFR
Departure: IPPH
Arriving: IFRD
FL: 050
Squawk: 1612
"""

class updateSquawkModal(ui.Modal, title="Update Squawk Code"):
    try:
        squawk = ui.TextInput(label="Updated Squawk Code", style=discord.TextStyle.short,
                            placeholder="If VFR put 1200", required=True)

    except Exception as e:
        print(e)
    
    async def on_submit(self, interaction: discord.Interaction):
        try:

            fpembed.remove_field(index=3)
            fpembed.add_field(name="Squawk", value=f"```{self.squawk}```", inline=True)

            await interaction.response.send_message(embed=fpembed)
        except Exception as e:
            print(e)


class fpModal(ui.Modal, title="Flight Plan Dialog"):
    try:
        callsign_aircraft = ui.TextInput(label="Callsign and Aircraft", style=discord.TextStyle.short,
                            placeholder="Fromat: Callsign Aircraft. Ex. AirFrans-2241 B777", required=True, min_length=1)
        
        route = ui.TextInput(label="Route", style=discord.TextStyle.short,
                            placeholder="Ex. GPD Direct. Ex2. EASTN ENTEX WEISN", required=True)
        
        flight_rules = ui.TextInput(label="IFR/VFR and FL", style=discord.TextStyle.short,
                            placeholder="Format: IFR/VFR FL000. Ex. IFR FL050", required=True)

        airports = ui.TextInput(label="Departure and Arrival", style=discord.TextStyle.short,
                            placeholder="Format: Dpt. ICAO > Arr. ICAO. Ex. IPPH > IFRD", required=True)
        
        squawk = ui.TextInput(label="Squawk", style=discord.TextStyle.short,
                            placeholder="If VFR put 1200. Ex. 7500 :trolled:", required=True)

    except Exception as e:
        print(e)
    # global fpinteraction
    async def on_submit(self, fpinteraction: discord.Interaction):
        try:

            async def update_squawk_callback(fpinteraction):
                fpmessage = await fpinteraction.response.send_modal(updateSquawkModal())

            global fpembed

            fpembed = discord.Embed(
                title=f"Flight Plan for {self.callsign_aircraft}", color=discord.Color.from_rgb(47, 49, 54))
            
            fpembed.add_field(name="Flight Rules and Flight Level", value=f"```{self.flight_rules}```", inline=True)
            fpembed.add_field(name="Departing and Arriving Airports", value=f"```{self.airports}```", inline=True)
            fpembed.add_field(name="Route", value=f"```{self.route}```", inline=True)
            fpembed.add_field(name="Squawk Code", value=f"```{self.squawk}```", inline=True)
            fpembed.set_footer(text="Time out to update the squawk code is 15 minutes")

            update_squawk = Button(label="Update squawk code", style=discord.ButtonStyle.blurple)

            view = View(timeout=900)

            update_squawk.callback = update_squawk_callback

            view.add_item(update_squawk)

            await fpinteraction.response.send_message(embed=fpembed, view=view)
        except Exception as e:
            print(e)


class FlightPlan(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def fp(self, ctx):

        async def fp_callback(interaction):
            await ctx.message.delete()
            await msg.delete()
            await interaction.response.send_modal(fpModal())

        fp_button = Button(label="Click to make a flight plan!", style=discord.ButtonStyle.green)

        view = View(timeout=300)

        fp_button.callback = fp_callback

        view.add_item(fp_button)

        msg = await ctx.reply(view=view)


async def setup(bot):
    await bot.add_cog(FlightPlan(bot))