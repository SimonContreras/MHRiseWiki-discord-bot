import discord
import datetime
from discord.ext import commands
from src.common.utils import color_by_rarity, weapon_to_emoji, num_to_emoji

class WeaponEmbed(discord.Embed):

    def __init__(self, dct: dict, ctx: commands.Context, headers:dict):
        self.__dct = dct
        self.extra_page = False
        self.__ctx = ctx
        self.__h = headers

    def main(self):
        """ Retrieve embed with Weapon information formatted based on type of weapon:
        Common:
            - name
            - rarity
            - type
            - attack
            - real-attack
            - damage type
            - affinity,
            - defense
            - elderseal
            - slots
            - crafting materials
            - upgrade materials
        Bow:
            - coatings
        Gunlance: 
            - shelling type
            - shelling level
        Bowguns:
            - special ammo
            - deviation
        Sever weapons:
            - sharpness


        Parameters
        ----------

        Returns
        -------
        Embed
            retrieve embed with formmatted data for a certain weapon
        """
        txt_title = f'''{self.__dct['name']} {weapon_to_emoji(self.__ctx, self.__dct['type'])}'''
        embed= discord.Embed(title=txt_title, color=color_by_rarity(self.__dct['rarity']))
        
        text_elems_weapon = '\n'.join([f'''{elem['name']}:{elem['attack']}'''for elem in self.__dct['elements']])
        text_slots_weapon = f'''Lv1:{self.__dct['slots']['1']}\nLv2:{self.__dct['slots']['2']}\nLv3:{self.__dct['slots']['3']}'''
        text_coatings_weapon = '\n'.join([f'''{coat['name']}:{coat['quantity']}''' for coat in self.__dct['coatings']])
        text_crafting_mats_weapon = '\n'.join([f'''{mat['name']}**({mat['quantity']})**''' for mat in self.__dct['create-items']])
        text_upgrade_mats_weapon = '\n'.join([f'''{mat['name']}**({mat['quantity']})**''' for mat in self.__dct['upgrade-items']])


        if self.__dct['type'] == 'light-bowgun' or self.__dct['type'] == 'heavy-bowgun':
            self.extra_page = True

            embed.add_field(name=self.__h['type'], value=self.__dct['type'], inline=True)
            embed.add_field(name=self.__h['rarity'], value=str(self.__dct['rarity']), inline=True)
            embed.add_field(name=self.__h['attack'], value=str(self.__dct['attack']), inline=True)
            embed.add_field(name=self.__h['real-attack'], value=str(self.__dct['real-attack']), inline=True)
            embed.add_field(name=self.__h['damage-type'], value=self.__dct['damage-type'], inline=True)
            embed.add_field(name=self.__h['affinity'], value=self.__dct['affinity'], inline=True)
            embed.add_field(name=self.__h['defense'], value=self.__dct['defense'], inline=True)
            embed.add_field(name=self.__h['elderseal'], value=self.__dct['elderseal'], inline=True)
            embed.add_field(name=self.__h['special-ammo'], value=self.__dct['special-ammo'], inline=True)
            embed.add_field(name=self.__h['deviation'], value=self.__dct['deviation'], inline=True)
            embed.add_field(name=self.__h['slots'], value=text_slots_weapon, inline=True)
            embed.add_field(name="\u200b", value="\u200b", inline=True)
            if len(text_crafting_mats_weapon) > 0:
                embed.add_field(name=self.__h['craft-materials'], value=text_crafting_mats_weapon, inline=True)
            if len(text_upgrade_mats_weapon) > 0:
                embed.add_field(name=self.__h['upgrade-materials'], value=text_upgrade_mats_weapon, inline=True)
        
        else:
            embed.add_field(name=self.__h['type'], value=self.__dct['type'], inline=True)
            embed.add_field(name=self.__h['rarity'], value=str(self.__dct['rarity']), inline=True)
            embed.add_field(name=self.__h['attack'], value=str(self.__dct['attack']), inline=True)
            embed.add_field(name=self.__h['real-attack'], value=str(self.__dct['real-attack']), inline=True)
            embed.add_field(name=self.__h['damage-type'], value=self.__dct['damage-type'], inline=True)
            embed.add_field(name=self.__h['affinity'], value=self.__dct['affinity'], inline=True)
            embed.add_field(name=self.__h['defense'], value=self.__dct['defense'], inline=True)
            embed.add_field(name=self.__h['elderseal'], value=self.__dct['elderseal'], inline=True)

            if self.__dct['type'] == 'gl':
                embed.add_field(name=self.__h['shelling-type'], value=self.__dct['shelling'] + str(self.__dct['shelling-lvl']), inline=True)

            embed.add_field(name=self.__h['element-ailment'], value=text_elems_weapon, inline=True)
            embed.add_field(name=self.__h['slots'], value=text_slots_weapon, inline=True)
            
            if self.__dct['type'] == 'bow':
                embed.add_field(name=self.__h['coatings'], value=text_coatings_weapon, inline=True)
            
            embed.add_field(name=self.__h['sharpness'], value=self.__dct['sharpness'], inline=True)
            if len(text_crafting_mats_weapon) > 0:
                embed.add_field(name=self.__h['craft-materials'], value=text_crafting_mats_weapon, inline=True)
            if len(text_upgrade_mats_weapon) > 0:
                embed.add_field(name=self.__h['upgrade-materials'], value=text_upgrade_mats_weapon, inline=True)
    
        embed.add_field(name=self.__h['previous-weapon'], value=self.__dct['previous-weapon'], inline=True)
        embed.add_field(name=self.__h['next-weapon'], value=self.__dct['next-weapon'], inline=True)
            
        
        embed.timestamp = datetime.datetime.now()
        if self.extra_page:
            embed.set_footer(text=f'''P. 1/2 {self.__dct['name']}''')
        else:
            embed.set_footer(text=self.__dct['name'])
        return embed
    
    def details(self):
        """ Retrieve embed with Weapon ammo information formatted for bowguns:
            - capacity
            - ammot type
            - rapid fire
            - recoil
            - reload
            
        Parameters
        ----------

        Returns
        -------
        Embed
            retrieve embed with formmatted data for a certain weapon ammo
        """
        txt_title = f'''{self.__dct['name']} {weapon_to_emoji(self.__ctx, self.__dct['type'])}'''
        embed= discord.Embed(title=txt_title, color=color_by_rarity(self.__dct['rarity']))
        embed.add_field(name=self.__h['ammo-type'], value='\u200b', inline=False)

        ammo_types = self.__dct['ammos'].keys()
        non_lvl_ammo = ['flaming', 'water', 'freeze', 'thunder', 'dragon', 'slicing', 'wyvern', 'demon', 'armor', 'tranq']
        for ammo in ammo_types:
            if ammo.find('clip') > -1:
                if self.__dct['ammos'][ammo] > 0:
                    ammo_t = ammo.split('_')[0]
                    rapid_fire = ':x:'
                    if self.__dct['ammos'][ammo_t+'_rapid']:
                        rapid_fire = ':white_check_mark:'
                    
                    text = f''' - {self.__h['capacity']}: **{str(self.__dct['ammos'][ammo_t+'_clip'])}** 
                                - {self.__h['rapid-fire']}:{rapid_fire}
                                - {self.__h['recoil']}:**+{str(self.__dct['ammos'][ammo_t+'_recoil'])}**
                                - {self.__h['reload']}:**+{self.__dct['ammos'][ammo_t+'_reload']}**
                            '''

                    if ammo_t in non_lvl_ammo:
                        ammo_name = ammo_t
                        ammo_lvl = '\u200b'
                    else:
                        ammo_name = ammo_t[:-1]
                        ammo_lvl = num_to_emoji(int(ammo_t[-1]))
                    embed.add_field(name=f'''**{ammo_name}** {ammo_lvl} :''', value=text, inline=True)
    
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=f'''P. 2/2 {self.__dct['name']}''')
        return embed