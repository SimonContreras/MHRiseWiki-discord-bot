import discord
import datetime
from src.common.utils import format_uppercase, color_by_rarity

class ItemEmbed(discord.Embed):
    """
    Embed that renders Item information
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
        Embed with formatted info for a certain item

    """
    def __init__(self, dct: dict, headers: dict):
        self._dct = dct
        self._h = headers

    def main(self):
        """ Retrieve embed with Item information formatted:
        rarity, name, price, max-carry and recipe if it can be craftable

        Parameters
        ----------

        Returns
        -------
        Embed
            retrieve embed with 'not found' info
        """
        maps_embeds = []
        embed= discord.Embed(title=format_uppercase(self._dct['name']), description=self._dct['description'], color=color_by_rarity(self._dct['rarity']))
        embed.set_thumbnail(url=f'''attachment://{self._dct['icon']}''')
        embed.add_field(name=self._h['category'], value=format_uppercase(self._dct['category']), inline=True)
        embed.add_field(name=self._h['rarity'], value=self._dct['rarity'], inline=True)
        embed.add_field(name=self._h['buy'], value=str(self._dct['buy'])+'z', inline=True)
        embed.add_field(name=self._h['sell'], value=str(self._dct['sell'])+'z', inline=True)
        embed.add_field(name=self._h['max-carry'], value=str(self._dct['max']), inline=True)
        
        if self._dct['craftable']:
            if self._dct['recipe']['items'][1]['quantity'] == 0:
                text_recipe = f''' **{self._dct['recipe']['items'][0]['name']}** ({self._dct['recipe']['items'][0]['quantity']})\
                      =   **{self._dct['name']}** ({self._dct['recipe']['product']})''' 
            else:
                text_recipe = f''' **{self._dct['recipe']['items'][0]['name']}** ({self._dct['recipe']['items'][0]['quantity']})  + \
                **{self._dct['recipe']['items'][1]['name']}** ({self._dct['recipe']['items'][1]['quantity']}) = **{self._dct['name']}** \
                ({self._dct['recipe']['product']})''' 
            embed.add_field(name=self._h['combination'], value=text_recipe, inline=False)

        if len(self._dct['locations']) >= 1:
            l_text = ''
            ls = []
            for l in self._dct['locations']:
                area = 'Ver mapa' if l['area'] == '0' else l['area']
                if l['name'] not in ls:
                    l_text += f'''**{format_uppercase(l['name'])}:** | **zonas:** {area} | **rango:**{l['rank']} \n'''
                    ls.append(l['name'])
                if l['map-available']:
                    e = discord.Embed(title=format_uppercase(l['name']), color=color_by_rarity(self._dct['rarity']))
                    e.set_image(url=f'''attachment://{l['map-img']}''')
                    d = {
                        'map-img': l['map-img'],
                        'embed': e,
                        }
                    maps_embeds.append(d)
        else:
            l_text = f'''{self._dct['obtain_info']}'''

        embed.add_field(name=self._h['location']+':', value=l_text, inline=False) 
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=format_uppercase(self._dct['name']))

        return embed, maps_embeds