import discord
from discord.ext import commands 
from core.classes import Cog_Extension
import json, datetime


with open('s.json', 'r', encoding='utf8') as jfile:
        jdata = json.load(jfile)

class Event_react(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author == self.bot.user:
            for i in jdata["ids"]:
                if str(message.channel.id) == i:
                    message_c = message.clean_content
                    message_a = message.author.name
                    message_g = message.guild.name
                    message_avat = message.author.avatar_url
                    await message.channel.purge(limit=1)
                    for j in jdata["ids"]:    
                        if not message.channel.id == j:                        
                            embed = discord.Embed(
                                title = F"來自：",
                                color=0xF4A7B9,
                                description = f"{message_g} ")

                            embed.add_field(name="訊息內容：", value=f"{message_c}", inline=True)
                            #embed.set_thumbnail(url = f"{message_avat}")
                            embed.set_author(name=f"{message_a}", icon_url = f"{message_avat}")
                            embed.set_footer(text="開發By 赤井重工研發組")
                            embed.timestamp = datetime.datetime.utcnow()
                            channel = self.bot.get_channel(int(f'{j}'))                        
                            await channel.send(embed = embed)

                        else:
                            pass
                        
                else:
                    pass
        

def setup(bot):
    bot.add_cog(Event_react(bot))