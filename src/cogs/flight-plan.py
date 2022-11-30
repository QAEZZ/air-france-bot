import discord

import datetime

from discord import ui
from discord.ext import commands
from discord.ui import View, Button


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

            fpembed.description=f"""```diff
- updated -```"""
            fpembed.remove_field(index=3)
            fpembed.remove_footer()
            fpembed.set_footer(text="If you're told to change your squawk code, make a new fp with that squawk code.")
            if str(self.squawk) == "7500":
                embed: discord.Embed = discord.Embed(
                    title="🚨 HIJACKING IN PROGRESS 🚨",
                    description="<@&975889011044409374>",
                    color=discord.Color.from_rgb(47, 49, 54)
                )
                fpembed.add_field(name="Squawk", value=f"""```diff
- {self.squawk} -```""", inline=True)
                await interaction.response.send_message(embeds=[fpembed, embed])
            else:
                fpembed.add_field(name="Squawk", value=f"""```py
{self.squawk}```""", inline=True)

                await interaction.response.send_message(embed=fpembed)

        except Exception as e:
            print(e)


class fpModal(ui.Modal, title="Flight Plan Dialog"):
    try:
        callsign_aircraft = ui.TextInput(label="Callsign and Aircraft", style=discord.TextStyle.short,
                            placeholder="Fromat: Callsign Aircraft. Ex. AirFrans-2241 B777", required=True, min_length=1)
        
        route = ui.TextInput(label="Route", style=discord.TextStyle.short,
                            placeholder="Ex. GPS Direct. Ex2. EASTN ENTEX WEISN", required=True)
        
        flight_rules = ui.TextInput(label="IFR/VFR and FL", style=discord.TextStyle.short,
                            placeholder="Format: IFR/VFR FL000. Ex. IFR FL050", required=True)

        airports = ui.TextInput(label="Departure and Arrival", style=discord.TextStyle.short,
                            placeholder="Format: Dpt. ICAO > Arr. ICAO. Ex. IPPH > IFRD", required=True)
        
        squawk = ui.TextInput(label="Squawk", style=discord.TextStyle.short,
                            placeholder="If VFR put 1200. Ex. 7500 :trolled:", required=True)

    except Exception as e:
        print(e)
    # global interaction
    async def on_submit(self, interaction: discord.Interaction):
        try:

            async def update_squawk_callback(fpinteraction):
                await interaction.delete_original_response()
                await fpinteraction.response.send_modal(updateSquawkModal())

            global fpembed

            fpembed = discord.Embed(
                title=f"Flight Plan for {self.callsign_aircraft}", color=discord.Color.from_rgb(47, 49, 54))
            
            fpembed.add_field(name="Flight Rules and Flight Level", value=f"""```fix
{self.flight_rules}```""", inline=True)
            fpembed.add_field(name="Departing and Arriving Airports", value=f"""```prolog
{self.airports}```""", inline=True)
            fpembed.add_field(name="Route", value=f"""```fix
{self.route}```""", inline=True)
            fpembed.add_field(name="Squawk Code", value=f"""```py
{self.squawk}```""", inline=True)
            fpembed.set_footer(text="Time out to update the squawk code is 25 minutes, after that you cannot update it.")

            update_squawk = Button(label="Update squawk code", style=discord.ButtonStyle.blurple)

            view = View(timeout=1500)

            update_squawk.callback = update_squawk_callback

            view.add_item(update_squawk)

            msg = await interaction.response.send_message(embed=fpembed, view=view)
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
