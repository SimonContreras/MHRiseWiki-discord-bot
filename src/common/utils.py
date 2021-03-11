import discord
"""Classes and functions to map info from database to discord representation
"""
class InputParser():
    """
    Format arguments sent via a discord command to a single string
    ...

    Attributes
    ----------
    args : list
        list of arguments
    
    Methods
    -------
    concat(self)
        return a single string that contains command arguments

    """
    def __init__(self, args):
        self.args = args
    
    def concat(self):
        """ Concatenate list of arguments

        Parameters
        ----------

        Returns
        -------
        str
            arguments concatenated in a single string in lowercase
        """
        if len(self.args) == 1:
            return self.args[0]
        return ' '.join(self.args).lower()

def to_stars(value: int):
    """ Retrieve string of stars emojis based in certain threshold rule

        Parameters
        ----------
        value: int
            number of certain param of an item of the game
        Returns
        -------
        str
            String of stars emojis
    """
    if value >= 40:
        return ':star: :star: :star:'
    elif 20 >= value > 40:
        return ':star: :star:'
    else:
        return ':star:'

def color_by_rarity(rarity: int):
    """ Return a discord color based in a number

        Parameters
        ----------
        rarity: int
            rarity of an item
        
        Returns
        -------
        discord.Color
            Discord color related to a certain rarity
        """
    color = {
        1: discord.Color.from_rgb(224, 224, 224),
        2: discord.Color.from_rgb(255,255,255),
        3: discord.Color.from_rgb(128, 255, 0),
        4: discord.Color.from_rgb(0, 255, 0),
        5: discord.Color.from_rgb(0, 255, 255),
        6: discord.Color.from_rgb(76, 0, 153),
        7: discord.Color.from_rgb(153, 0, 153),
        8: discord.Color.from_rgb(255, 128, 0),
        9: discord.Color.from_rgb(255, 0, 0),
        10: discord.Color.from_rgb(0, 204, 204),
        11: discord.Color.from_rgb(255, 255, 0),
        12: discord.Color.from_rgb(204, 229, 255)
    }
    return color[rarity]


def num_to_emoji(num:int):
    """ Retrieve emoji related to a number

        Parameters
        ----------
        num: int
            number
        Returns
        -------
        str
            emoji that represent a number
        """
    number = {
        0: ':zero:',
        1: ':one:',
        2: ':two:',
        3: ':three:',
        4: ':four:',
        5: ':five:',
        6: ':six:',
        7: ':seven:',
        8: ':eight:',
        9: ':nine:',
    }
    return number[num]

def text_to_emoji(text: str):
    """ Retrieve emoji related to a certain piece of an armorset

        Parameters
        ----------
        text: str
            text
        Returns
        -------
        Embed
            emoji that represent a part of an armorset
        """
    emoji = {
        'head': ':military_helmet:',
        'chest': ':martial_arts_uniform:',
        'arms': ':gloves:',
        'waist': ':shorts:',
        'legs': ':mechanical_leg:'
    }
    return emoji[text]

def weapon_to_emoji(ctx, weapon: str):
    """ Retrieve custom emoji that represent a weapon

        Parameters
        ----------
        ctx: commands.Context
            context of server that create request
        weapon: str
            weapon to map

        Returns
        -------
        str
            Custom emoji of a weapon
        """
    wp = {
        'hunting-horn': 'hh',
        'long-sword': 'ls',
        'sword-and-shield': 'sns',
        'switch-axe': 'swax',
        'light-bowgun': 'lbg',
        'lance': 'lance',
        'insect-glaive': 'ig',
        'heavy-bowgun': 'hbg',
        'charge-blade': 'cb',
        'gunlance': 'gl',
        'dual-blades': 'db',
        'great-sword': 'gs',
        'hammer': 'hammer',
        'bow': 'bow',

    }
    e = ' '
    for emoji in ctx.guild.emojis:
        if (wp[weapon] == emoji.name) and (emoji.is_usable()):
            e = f'''<:{emoji.name}:{emoji.id}>'''
            break
    
    return e
