import os
import discord
import datetime

from src.common.utils import to_stars

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
    def __init__(self, dct: dict, headers: dict):
        self.__dct = dct
        self.__h = headers

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
        join_char = ', '
        embed2 = None
        embed= discord.Embed(title=self.__dct['name'], description=self.__dct['description'], color=discord.Color.blue())
        embed.set_thumbnail(url=f'''attachment://{self.__dct['img-url']}''')
        embed.add_field(name=self.__h['species'], value=self.__dct['species'], inline=True)
        embed.add_field(name=self.__h['ailments'], value=join_char.join(self.__dct['ailments']), inline=True)
        embed.add_field(name=self.__h['inmune'], value=join_char.join(self.__dct['inmune']), inline=True)
        embed.add_field(name=self.__h['weakness-3'], value=join_char.join(self.__dct['weakness-3']), inline=True)
        embed.add_field(name=self.__h['weakness-2'], value=join_char.join(self.__dct['weakness-2']), inline=True)
        embed.add_field(name=self.__h['weakness-1'], value=join_char.join(self.__dct['weakness-1']), inline=True)
        embed.add_field(name=self.__h['breakable'], value=join_char.join(self.__dct['breakable']), inline=True)
        embed.add_field(name=self.__h['location'], value=join_char.join(self.__dct['locations']), inline=True)

        if self.__dct['has-alt-weakness']:
            embed2 = discord.Embed(title=self.__h['second-state'], description=self.__dct['alt-state-description'], color=discord.Color.blue())
            embed2.set_thumbnail(url=f'''attachment://{self.__dct['img-url']}''')
            embed2.add_field(name=self.__h['inmune'], value=join_char.join(self.__dct['alt-inmune']), inline=True)
            embed2.add_field(name=self.__h['weakness-3'], value=join_char.join(self.__dct['alt-weakness-3']), inline=True)
            embed2.add_field(name=self.__h['weakness-2'], value=join_char.join(self.__dct['alt-weakness-2']), inline=True)
            embed2.add_field(name=self.__h['weakness-1'], value=join_char.join(self.__dct['alt-weakness-1']), inline=True)
        return embed, embed2

    def details(self):
        """ Retrieve embed with summary of HZV for a monster,
        show weakness of each weakpoint to blunt, shot, sever damage.
        
        Parameters
        ----------

        Returns
        -------
        Embed
            retrieve two embed with summary hzv info for each state of a monster,
            if the monster doesn't have second state, the embed is None
        """
        embed= discord.Embed(color=discord.Color.blue())
        embed2 = None
        for weakp in self.__dct['weak-points']:
            if self.__dct['weak-points'].index(weakp) == 0:
                header = self.__h['weakpoints']
            else:
                header = '\u200b'

            text_value = self.__h['weakpoints-attacks']
            formatted = text_value.format(weakp['part'],
                                            to_stars(weakp['sever']),
                                            to_stars(weakp['blunt']), 
                                            to_stars(weakp['ranged']))
            embed.add_field(name=header, value=formatted, inline=True)
        
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=self.__dct['name'])
        if self.__dct['has-alt-weakness']:
            embed2= discord.Embed(color=discord.Color.blue())
            for weakp in self.__dct['alt-weak-points']:
                if self.__dct['alt-weak-points'].index(weakp) == 0:
                    header = self.__h['weakpoints']
                else:
                    header = '\u200b'

                text_value = self.__h['weakpoints-attacks']
                formatted = text_value.format(weakp['part'],
                                                to_stars(weakp['sever']),
                                                to_stars(weakp['blunt']), 
                                                to_stars(weakp['ranged']))
                embed2.add_field(name=header, value=formatted, inline=True)
            
            embed2.timestamp = datetime.datetime.now()
            embed2.set_footer(text=self.__dct['name'])
        return embed, embed2
    
    def hzv(self):
        """ WIP

        Parameters
        ----------

        Returns
        -------
        
            
        """
        embed= discord.Embed(title=self.__dct['name'] + ' Hitzones', color=discord.Color.blue())
        embed.set_image(url=f'''attachment://{self.__dct['img-url']}''')
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=self.__dct['name'] + ' Hitzones')

        return embed