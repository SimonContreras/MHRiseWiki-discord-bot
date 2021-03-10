import discord
from src.orm.models import Header

class PrefixEmbed(discord.Embed):
    """
    Embed that renders Prefix information
    ...

    Attributes
    ----------
    header: Header
        field titles for item information based on language set for the bot
    prefix: str
        new language set for bot
    Methods
    -------
    main(self)
        Embed with formatted info related to new language set to bot

    """
    def __init__(self, header: Header, prefix: str):
        self.__h = header
        self.__prefix = prefix

    def main(self):
        """ Retrieve embed with information for new language set to bot

        Parameters
        ----------

        Returns
        -------
        Embed
            retrieve embed with new language status
        """
        embed= discord.Embed(color=discord.Color.blurple())
        if len(self.__prefix) <= 3:
            embed.add_field(name=self.__h.name, value=self.__h.translation.format(new_prefix=self.__prefix), inline=True)
        else:
            embed.add_field(name=self.__h.name, value=self.__h.translation.format(prefix=self.__prefix), inline=True)
        return embed

    