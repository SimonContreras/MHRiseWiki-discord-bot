import discord
import datetime

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
        self.__dct = dct
        self.__h = headers

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
        embed= discord.Embed(title=self.__dct['name'], description=self.__dct['description'], color=discord.Color.blue())
        embed.add_field(name=self.__h['rarity'], value=self.__dct['rarity'], inline=True)
        embed.add_field(name=self.__h['price'], value=str(self.__dct['price']), inline=True)
        embed.add_field(name=self.__h['max-carry'], value=str(self.__dct['max']), inline=True)
       
        if self.__dct['craftable']:
            text_recipe = f''' **{self.__dct['recipe']['items'][0]['name']}** ({self.__dct['recipe']['items'][0]['quantity']})  + \
                **{self.__dct['recipe']['items'][1]['name']}** ({self.__dct['recipe']['items'][1]['quantity']}) = **{self.__dct['name']}** \
                ({self.__dct['recipe']['product']})''' 
            embed.add_field(name=self.__h['combination'], value=text_recipe, inline=False)

        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=self.__dct['name'])
        return embed