import os
import discord
import datetime

from discord.ext import commands

from src.common.utils import format_uppercase, status_or_element_to_emoji

MONSTER_IMG_ROUTE = os.getenv('MONSTER_IMG_ROUTE')

class MonsterEmbed(discord.Embed):
    """
    Embed that renders Monster information
    ...

    Attributes
    ----------
    dct : dict
        Dictionary with info to show in embed
   headers: dict
        field titles for item information based on language set for the bot
    
    Methods
    -------
    main(self)
        return Embed with detailed info of a monster
    details(self)
        return Embed with summary info of hitzones values of a monster
    hzv(self)
        WIP TODO
    """
    def __init__(self, ctx: commands.Context, dct: dict, headers: dict):
        self.ctx = ctx
        self.dct = dct
        self.h = headers

    def main(self):
        """ Retrieve embed with Monster information formatted:
        name, description, specie, ailments, inmunity, weaknesses,
        locations, also show alternative state wth same info.

        Parameters
        ----------

        Returns
        -------
        Embed
            retrieve two embed one for each state of a monster, if monster doesn't 
            have second state, second embed is None
        """
        embed2 = None
        embed= discord.Embed(title=format_uppercase(self.dct['name']), description=self.dct['description'], color=discord.Color.blue())
        embed.set_thumbnail(url=f'''attachment://{self.dct['img-url']}''')
        embed.add_field(name=self.h['species'], value=self.dct['species'], inline=True)
        embed.add_field(name=self.h['ailments'], value=status_or_element_to_emoji(self.ctx,self.dct['ailments']), inline=True)
        embed.add_field(name=self.h['inmune'], value=status_or_element_to_emoji(self.ctx,self.dct['inmune']), inline=True)
        embed.add_field(name=self.h['weakness-3'], value=status_or_element_to_emoji(self.ctx,self.dct['weakness-3']), inline=True)
        embed.add_field(name=self.h['weakness-2'], value=status_or_element_to_emoji(self.ctx,self.dct['weakness-2']), inline=True)
        embed.add_field(name=self.h['weakness-1'], value=status_or_element_to_emoji(self.ctx,self.dct['weakness-1']), inline=True)
        embed.add_field(name=self.h['breakable'], value=status_or_element_to_emoji(self.ctx,self.dct['breakable']), inline=True)
        embed.add_field(name=self.h['location'], value=status_or_element_to_emoji(self.ctx,self.dct['locations']), inline=True)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=format_uppercase(self.dct['name']))

        if self.dct['has-alt-weakness']:
            embed2 = discord.Embed(title=self.h['second-state'], description=self.dct['alt-state-description'], color=discord.Color.blue())
            embed2.set_thumbnail(url=f'''attachment://{self.dct['img-url']}''')
            embed2.add_field(name=self.h['inmune'], value=status_or_element_to_emoji(self.ctx,self.dct['alt-inmune']), inline=True)
            embed2.add_field(name=self.h['weakness-3'], value=status_or_element_to_emoji(self.ctx,self.dct['alt-weakness-3']), inline=True)
            embed2.add_field(name=self.h['weakness-2'], value=status_or_element_to_emoji(self.ctx,self.dct['alt-weakness-2']), inline=True)
            embed2.add_field(name=self.h['weakness-1'], value=status_or_element_to_emoji(self.ctx,self.dct['alt-weakness-1']), inline=True)
            embed.timestamp = datetime.datetime.now()
            embed.set_footer(text=format_uppercase(self.dct['name']))
        return embed, embed2

    
    def hzv(self):
        """ WIP

        Parameters
        ----------

        Returns
        -------
        
            
        """
        embed= discord.Embed(title=format_uppercase(self.dct['name']) + ' Hitzones', color=discord.Color.blue())
        embed.set_image(url=f'''attachment://{self.dct['img-url']}''')
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=format_uppercase(self.dct['name']) + ' Hitzones')

        return embed
    
    def drops(self):
        """ WIP

        Parameters
        ----------

        Returns
        -------
        
            
        """
        embed= discord.Embed(title=format_uppercase(self.dct['name']) + ' Drops', color=discord.Color.blue())
        embed.set_image(url=f'''attachment://{self.dct['img-url']}''')
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=format_uppercase(self.dct['name']) + ' Drops')

        return embed