import discord
import datetime
from src.common.utils import format_uppercase
class SkillEmbed(discord.Embed):
    """
    Embed that renders Skill information
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
        Embed with formatted info for a certain skill

    """
    def __init__(self, dct: dict, headers: dict):
        self._dct = dct
        self._h = headers

    def main(self):
        """ Retrieve embed with Skill information formatted:
            name, level, jewels, talisman

        Parameters
        ----------

        Returns
        -------
        Embed
            retrieve embed with skill info formatted
        """
        embed= discord.Embed(title=format_uppercase(self._dct['name']), description=self._dct['description'], color=discord.Color.blue())
        embed.set_thumbnail(url=f'''attachment://{self._dct['icon']}''')
        text_skill_levels = ' '
        for l in self._dct['levels']:
            text_skill_levels += f'''**Lv{l['level']}:** {l['description'][3:]} \n'''
        
        #text_jewels = ' '
        #for jwl in self._dct['jewels']:
        #    text_jewels += f'''**Lv{str(jwl['level'])}:** {jwl['name']} \n'''

        embed.add_field(name=self._h['level'], value=text_skill_levels, inline=False)
        #embed.add_field(name=self._h['talisman'], value=self._dct['talisman'], inline=True)
        #embed.add_field(name=self._h['jewels'], value=text_jewels, inline=True)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=format_uppercase(self._dct['name']))
        return embed