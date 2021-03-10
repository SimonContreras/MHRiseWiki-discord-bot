import discord
import datetime

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
        self.__dct = dct
        self.__h = headers

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
        embed= discord.Embed(title=self.__dct['name'], description=self.__dct['description'], color=discord.Color.blue())
        
        text_skill_levels = ''
        for l in self.__dct['levels']:
            text_skill_levels += f'''**Lv{l['level']}:** {l['description']} \n'''
        
        text_jewels = ''
        for jwl in self.__dct['jewels']:
            text_jewels += f'''**Lv{str(jwl['level'])}:** {jwl['name']} \n'''

        embed.add_field(name=self.__h['level'], value=text_skill_levels, inline=False)
        embed.add_field(name=self.__h['talisman'], value=self.__dct['talisman'], inline=True)
        embed.add_field(name=self.__h['jewels'], value=text_jewels, inline=True)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=self.__dct['name'])
        return embed