import discord
import datetime

from src.common.utils import color_by_rarity, num_to_emoji, text_to_emoji

class ArmorEmbed(discord.Embed):
    """
    Embeds related to command '?armor'
    ...

    Attributes
    ----------
    dct: dict
        Armor data serialized in a dictionary
    headers: dict
        Headers related to armor embeds, serialized in a dictionary
    
    Methods
    -------
    main(self)
        Return a embed with data related to an armor/armoset
    details(self, armor_piece: int)
        Return a embed with detailed info of a piece of an armorset

    """
    def __init__(self, dct: dict, headers: dict):
        self.__dct = dct
        self.__h = headers

    def main(self):
        """
        Create embed related to general info of an armorset

        Parameters
        ----------
        self: ArmorEmbed

        Returns
        -------
        Embed
            Embed with general info of an armorset
        """
        embed= discord.Embed(title=self.__dct['name'], color=color_by_rarity(self.__dct['rarity']))

        text_set_bonus = f'''**{self.__dct['set-bonus']['name']} : ** {self.__dct['set-bonus']['description']}'''
        embed.add_field(name=self.__h['armorset'], value=text_set_bonus, inline=False)
        
        min_def = 0
        max_def = 0
        max_elem_res = {
            'fire': 0,
            'water': 0,
            'thunder': 0,
            'ice': 0,
            'dragon': 0
        }
        text_full_set = ''
        text_slots_set = ''
        text_elem_res_piece = ''
        text_skills_piece = ''
        text_type_piece = ''
        text_skills_pieces = ''
        for piece in self.__dct['pieces']:
            min_def += piece['min-def']
            max_def += piece['max-def']
            max_elem_res['fire'] += piece['resistances']['fire'] 
            max_elem_res['water'] += piece['resistances']['water'] 
            max_elem_res['thunder'] += piece['resistances']['thunder'] 
            max_elem_res['ice'] += piece['resistances']['ice'] 
            max_elem_res['dragon'] += piece['resistances']['dragon'] 
            text_elem_res_piece += f'''{text_to_emoji(piece['type'])} \
                            :fire: {str(piece['resistances']['fire'])} \
                            :droplet: {str(piece['resistances']['water'])} \
                            :zap: {str(piece['resistances']['thunder'])} \
                            :snowflake: {str(piece['resistances']['ice'])} \
                            :dragon: {str(piece['resistances']['dragon'])} \n'''
            
            slots_per_piece = f'''**Lvl1: {num_to_emoji(piece['slots']['1'])} Lvl2: {num_to_emoji(piece['slots']['2'])} Lvl3: {num_to_emoji(piece['slots']['3'])}**'''
            text_full_set  +=  f'''**{text_to_emoji(piece['type'])}** : {piece['name']} \n'''
            text_slots_set += slots_per_piece + '\n'

            text_type_piece += f'''{text_to_emoji(piece['type'])}'''
            text_skills_piece = ' '.join([f'''**Lv{skill['level']}:** {skill['name']} ''' for skill in piece['skills']])
            text_skills_pieces += f''' {text_skills_piece} \n'''    
            
        
        text_resistances = f'''**:fire: {max_elem_res['fire']} :droplet: {max_elem_res['water']} :zap: {max_elem_res['thunder']}''' +\
                            f''':snowflake: {max_elem_res['ice']} :dragon: {max_elem_res['dragon']}**'''
        
        text_defense = f''' Mínima: **{min_def}** | Máxima: **{max_def}** '''
        
        embed.add_field(name=self.__h['resistances'], value= text_resistances, inline=True)
        embed.add_field(name=self.__h['defenses'], value=text_defense, inline=False)

        embed.add_field(name=self.__h['pieces'], value=text_full_set, inline=True)
        embed.add_field(name=self.__h['slots'], value=text_slots_set, inline=True)
        embed.add_field(name=self.__h['skills'], value=text_skills_pieces, inline=False)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=self.__dct['name'])

        return embed

    def details(self, armor_piece: int):
        """
        Create an embed with detailed info of a piece of armor related
        to an armorset

        Parameters
        ----------
        self: ArmorEmbed

        Returns
        -------
        Embed
            Embed with detailed info of a piece of armor
        """
        piece =  self.__dct['pieces'][armor_piece]
        embed= discord.Embed(title=piece['name'], description=f'''Rareza: {str(piece['rarity'])}''', color=color_by_rarity(self.__dct['rarity']))
    
        text_resistances_piece = f'''{text_to_emoji(piece['type'])} \
                            :fire: {str(piece['resistances']['fire'])} \
                            :droplet: {str(piece['resistances']['water'])} \
                            :zap: {str(piece['resistances']['thunder'])} \
                            :snowflake: {str(piece['resistances']['ice'])} \
                            :dragon: {str(piece['resistances']['dragon'])} \n'''

        text_skills_piece = '\n'.join([f'''**Lv{skill['level']}:** {skill['name']} ''' for skill in piece['skills']])
            
        text_crafting_mats_piece ='\n'.join([f'''**{mat['name']}:** {mat['quantity']} ''' for mat in piece['crafting-mats']])
        
        text_defs_piece = f'''Mínima: **{piece['min-def']}** | Máxima: {piece['max-def']}'''
        text_slots_piece = f'''**Lvl1: {num_to_emoji(piece['slots']['1'])} \
                            Lvl2: {num_to_emoji(piece['slots']['2'])} \
                            Lvl3: {num_to_emoji(piece['slots']['3'])}**'''

        embed.add_field(name=self.__h['defenses'], value=text_defs_piece, inline=True)
        embed.add_field(name=self.__h['resistances'], value=text_resistances_piece, inline=False)
        embed.add_field(name=self.__h['slots'], value=text_slots_piece, inline=False)
        embed.add_field(name=self.__h['skills'], value=text_skills_piece, inline=True)
        embed.add_field(name=self.__h['craft-mats'], value=text_crafting_mats_piece, inline=False)
    
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=self.__dct['name'])
        
        return embed