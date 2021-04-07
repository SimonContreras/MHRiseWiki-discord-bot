import discord
import datetime
from src.common.utils import format_uppercase, color_by_rarity, num_to_emoji

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
            n = 0
            last_name = ''
            for l in self._dct['locations']:
                n+= 1
                area = 'Ver mapa' if l['area'] == '0' else l['area'].replace(';', ',')
                if l['name'] != last_name:
                    l_text += f'''{num_to_emoji(n)} | **{format_uppercase(l['name'])}:** | **{self._h['zones']}:**  \
                                {area} | **{self._h['rank']}:**{l['rank']} \n'''
                    last_name = l['name']
                else:
                    l_text = l_text.replace(f'''{num_to_emoji(n-1)}''',f'''{num_to_emoji(n-1)}-{num_to_emoji(n)}''' )
                if l['map-available']:
                    e = discord.Embed(title=num_to_emoji(n)+format_uppercase(l['name']), color=color_by_rarity(self._dct['rarity']))
                    m_text = f'''**{self._h['zones']}:** {area} | **{self._h['rank']}:**{l['rank']}'''
                    e.add_field(name='Información mapa', value=m_text, inline=False) 
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