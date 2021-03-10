import discord
from src.orm.models import Header

class LanguageEmbed(discord.Embed):
    """
    Embed that renders Language information
    ...

    Attributes
    ----------
    header : Header
        field titles for changeLanguage command
   lang: str
        new language changed for the bot
    
    Methods
    -------
    main(self)
        Embed with formatted info related to changed language

    """
    def __init__(self, header: Header, lang: str):
        self.__h = header
        self.__lang = lang

    def main(self):
        """ Retrieve embed with Language information, related to
        the change of language bot.

        Parameters
        ----------

        Returns
        -------
        Embed
            retrieve embed with status of change language action
        """
        embed = discord.Embed(color=discord.Color.blurple())
        if self.__lang is not None:
            embed.add_field(name=self.__h.name, value=self.__h.translation.format(new_lang=self.__lang), inline=True)
        else:
            embed.add_field(name=self.__h.name, value=self.__h.translation, inline=True)
        return embed

    