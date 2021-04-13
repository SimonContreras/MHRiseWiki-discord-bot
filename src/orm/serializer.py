from src.orm.models import Weapon, WeaponAmmo, WeaponText

class TipSerializer():

    def __init__(self, query):
        self._query = query

    def serialize(self):
        return self._query.to_dict()
    
    def serialize_list(self):
        main_dct = {'tips': []}
        for r in self._query:
            main_dct['tips'].append({ 'name': r.name })
        return main_dct
        
class ItemSerializer():

    def __init__(self, query, locations):
        self.query = query
        self.locations = locations
    
    def _format_locations(self):
        locations = []
        if len(self.locations) >= 1:
            for l in self.locations:
                dct = {
                    'name': l.location,
                    'area': l.area,
                    'rank': l.rank,
                    'map-available':l.map_available,
                    'map-img': l.map_img
                }
                locations.append(dct)
        return locations

    def serialize(self):
        locations = self._format_locations()
        main_dct = {
            'name': self.query.name,
            'rarity': self.query.rarity,
            'description': self.query.description,
            'buy': self.query.buy_price,
            'sell': self.query.sell_price,
            'craftable': self.query.craftable,
            'product': self.query.quantity_result,
            'max': self.query.carry_limit,
            'category':self.query.category,
            'icon':self.query.icon,
            'obtain_info': self.query.obtain_info,
            'recipe': {
                'product': self.query.quantity_result,
                'items': [
                    {
                        'name': self.query.first_name,
                        'quantity': self.query.quantity_first
                    },
                    {
                        'name': self.query.second_name,
                        'quantity': self.query.quantity_second
                    }
                ]
            },
            'locations':locations
        }
        return main_dct


class HelpSerializer():

    def __init__(self, commands, header):
        self.commands = commands
        self.__header = header
    
    def serialize(self):
        comms = []
        for comm in self.commands:
            comm_dct = {
                'name': comm[0].name,
                'params':comm[1].name,
                'description':comm[0].description,
            }
            comms.append(comm_dct)
        
        main_dct = {
            'title': self.__header.title,
            'commands': comms
        }
        return main_dct

class MonsterSerializer():

    def __init__(self, monster, habitats, breaks, language: int):
        self._m = monster
        self._h = habitats
        self._b = breaks
        self._lang = language

    def _translate(self, key:str):
        esp = {
            'roar': 'rugido',
            'wind': 'presion viento',
            'tremor': 'temblor',
            'defensedown': 'bajar defensa',
            'fireblight': 'fuego',
            'waterblight': 'agua',
            'thunderblight': 'trueno',
            'iceblight': 'hielo',
            'dragonblight': 'dragon',
            'blastblight': 'nitro',
            'bleed': 'sangrado',
            'mud': 'barro',
            'fire':'fuego',
            'water':'agua',
            'ice':'hielo',
            'thunder':'trueno',
            'dragon':'dragon',
            'poison':'veneno',
            'sleep':'sueño',
            'paralysis':'paralisis',
            'blast':'nitro',
            'stun':'aturdir',
        }

        eng = {
            'roar': 'roar',
            'wind': 'wind',
            'tremor': 'tremor',
            'defensedown': 'defensedown',
            'fireblight': 'fireblight',
            'waterblight': 'waterblight',
            'thunderblight': 'thunderblight',
            'iceblight': 'iceblight',
            'dragonblight': 'dragonblight',
            'blastblight': 'blastblight',
            'bleed': 'bleed',
            'mud': 'mud',
            'fire':'fire',
            'water':'water',
            'ice':'ice',
            'thunder':'thunder',
            'dragon':'dragon',
            'poison':'poison',
            'sleep':'sleep',
            'paralysis':'paralysis',
            'blast':'blast',
            'stun':'stun',
        }
        try:
            if self._lang == 1:
                return esp[key]
            return eng[key]
        except KeyError:
            return None
    
    def _format_stats(self):
        m_stat = self._m[1].to_dict()
        weaknesses_0 = []
        weaknesses_1 = []
        weaknesses_2 = []
        weaknesses_3 = []
        ailments = []
        alt_weaknesses_0 = []
        alt_weaknesses_1 = []
        alt_weaknesses_2 = []
        alt_weaknesses_3 = []
        plague_0 = []
        plague_1 = []
        plague_2 = []
        plague_3 = []
        alt_plague_0 = []
        alt_plague_1 = []
        alt_plague_2 = []
        alt_plague_3 = []
        for w in m_stat:
            key = w.split('_')
            if len(key) > 1:
                translation = self._translate(key[-1])
                if translation is not None:
                    if key[0] == 'ailment' and m_stat[w] == True:
                        ailments.append(translation)
                    elif key[0] == 'weakness':
                        if m_stat[w] == 0:
                            weaknesses_0.append(translation)
                        elif m_stat[w] == 1:
                            weaknesses_1.append(translation)
                        elif m_stat[w] == 2:
                            weaknesses_2.append(translation)
                        elif m_stat[w] == 3:
                            weaknesses_3.append(translation)
                    elif key[0] == 'alt' and key[1] == 'weakness':
                        if m_stat[w] == 0:
                            alt_weaknesses_0.append(translation)
                        elif m_stat[w] == 1:
                            alt_weaknesses_1.append(translation)
                        elif m_stat[w] == 2:
                            alt_weaknesses_2.append(translation)
                        elif m_stat[w] == 3:
                            alt_weaknesses_3.append(translation)
                    elif key[0] == 'plague':
                        if m_stat[w] == 0:
                            plague_0.append(translation)
                        elif m_stat[w] == 1:
                            plague_1.append(translation)
                        elif m_stat[w] == 2:
                            plague_2.append(translation)
                        elif m_stat[w] == 3:
                            plague_3.append(translation)
                    elif key[0] == 'alt' and key[1] == 'plague':
                        if m_stat[w] == 0:
                            alt_plague_0.append(translation)
                        elif m_stat[w] == 1:
                            alt_plague_1.append(translation)
                        elif m_stat[w] == 2:
                            alt_plague_2.append(translation)
                        elif m_stat[w] == 3:
                            alt_plague_3.append(translation)
        
        weaknesses_0 = '-' if ((type(weaknesses_0) == list) and (len(weaknesses_0) == 0)) else weaknesses_0
        weaknesses_1 = '-' if ((type(weaknesses_1) == list) and (len(weaknesses_1) == 0)) else weaknesses_1
        weaknesses_2 = '-' if ((type(weaknesses_2) == list) and (len(weaknesses_2) == 0)) else weaknesses_2
        weaknesses_3 = '-' if ((type(weaknesses_3) == list) and (len(weaknesses_3) == 0)) else weaknesses_3
        ailments = '-' if ((type(ailments) == list) and (len(ailments) == 0)) else ailments
        alt_weaknesses_0 = '-' if ((type(alt_weaknesses_0) == list) and (len(alt_weaknesses_0) == 0)) else alt_weaknesses_0
        alt_weaknesses_1 = '-' if ((type(alt_weaknesses_1) == list) and (len(alt_weaknesses_1) == 0)) else alt_weaknesses_1
        alt_weaknesses_2 = '-' if ((type(alt_weaknesses_2) == list) and (len(alt_weaknesses_2) == 0)) else alt_weaknesses_2
        alt_weaknesses_3 = '-' if ((type(alt_weaknesses_3) == list) and (len(alt_weaknesses_3) == 0)) else alt_weaknesses_3
        plague_0 = '-' if ((type(plague_0) == list) and (len(plague_0) == 0)) else plague_0
        plague_1 = '-' if ((type(plague_1) == list) and (len(plague_1) == 0)) else plague_1
        plague_2 = '-' if ((type(plague_2) == list) and (len(plague_2) == 0)) else plague_2
        plague_3 = '-' if ((type(plague_3) == list) and (len(plague_3) == 0)) else plague_3
        alt_plague_0 = '-' if ((type(alt_plague_0) == list) and (len(alt_plague_0) == 0)) else alt_plague_0
        alt_plague_1 = '-' if ((type(alt_plague_1) == list) and (len(alt_plague_1) == 0)) else alt_plague_1
        alt_plague_2 = '-' if ((type(alt_plague_2) == list) and (len(alt_plague_2) == 0)) else alt_plague_2
        alt_plague_3 = '-' if ((type(alt_plague_3) == list) and (len(alt_plague_3) == 0)) else alt_plague_3
        
        return weaknesses_0, weaknesses_1, weaknesses_2, weaknesses_3, \
            alt_weaknesses_0, alt_weaknesses_1, alt_weaknesses_2, alt_weaknesses_3, ailments, \
            plague_0, plague_1, plague_2, plague_3, alt_plague_0, alt_plague_1, alt_plague_2, alt_plague_3

    def _format_locations(self):
        if len(self._h) >= 1:
            return self._h
        else:
            return '-'

    def _format_breakables(self):
        breakables = []
        if len(self._b) > 1:
            for b in self._b:
                breakables.append(b[1].part_name)
        else:
            return '-'
        
    def serialize(self):
        w_0, w_1, w_2, w_3, \
            alt_0, alt_1, alt_2, alt_3, a, \
            p_0, p_1, p_2, p_3, alt_p_0, alt_p_1, alt_p_2, alt_p_3 = self._format_stats()
        main_dct = {
            'name': self._m[0].name,
            'species': self._m[0].species,
            'description':self._m[0].description,
            'danger_level':self._m[1].danger_level,
            'pitfall_trap': self._m[1].pitfall_trap,
            'shock_trap':self._m[1].shock_trap,
            'img-url': self._m[1].icon,
            'ailments': a,
            'inmune': w_0,
            'weakness-3': w_3,
            'weakness-2': w_2,
            'weakness-1': w_1,
            'has-alt-weakness': self._m[1].has_alt_weakness,
            'alt-state-description': self._m[0].alt_state_description,
            'alt-inmune': alt_0,
            'alt-weakness-3': alt_3,
            'alt-weakness-2': alt_2,
            'alt-weakness-1': alt_1,
            'plague_0':p_0,
            'plague_1':p_1,
            'plague_2':p_2,
            'plague_3':p_3,
            'alt_plague_0':alt_p_0,
            'alt_plague_1':alt_p_1,
            'alt_plague_2':alt_p_2,
            'alt_plague_3':alt_p_3,
            'locations': self._format_locations(),
            'breakable': self._format_breakables(),
        }
        return main_dct

class HeaderSerializer():

    def __init__(self, query: list):
        self.q = query
    
    def serialize(self):
        dct = {}
        if len(self) > 0:
            for h in self:
                dct[h.name] = h.translation
        return dct

class WeaponSerializer():

    def __init__(self, weapon_text:WeaponText, weapon:Weapon, weapon_ammo:WeaponAmmo, \
        previous_weapon:tuple, next_weapon:tuple, create_items:list,  \
            upgrade_items:list, melodies, armorset_bonus, skills):

        self.__w_t = weapon_text
        self.__w = weapon
        self.w_a = weapon_ammo
        self._p_w = previous_weapon
        self._n_w = next_weapon
        self.__c_i = create_items
        self.__u_i = upgrade_items
        self.m = melodies
        self.a_b = armorset_bonus
        self.s = skills
    
    def __format_gun_params(self):
        special_ammo = '-'
        deviation = '-'
        if self.w_a is not None:
            special_ammo = self.w_a.special_ammo
            deviation = self.w_a.deviation
        return special_ammo, deviation
    
    def __format_coatings(self):
        coatings = []
        if self.__w.coating_blast > 0:
            coatings.append({'name': 'blast', 'quantity': self.__w.coating_blast})
        if self.__w.coating_close > 0:
            coatings.append({'name': 'close', 'quantity': self.__w.coating_close})
        if self.__w.coating_paralysis > 0:
            coatings.append({'name': 'paralysis', 'quantity': self.__w.coating_paralysis})
        if self.__w.coating_poison > 0:
            coatings.append({'name': 'poison', 'quantity': self.__w.coating_poison})
        if self.__w.coating_power > 0:
            coatings.append({'name': 'power', 'quantity': self.__w.coating_power})
        if self.__w.coating_sleep > 0:
            coatings.append({'name': 'sleep', 'quantity': self.__w.coating_sleep})
        return coatings

    def __format_elements(self):
        elements = []
        if self.__w.element1 != '-':
            e1 = {'name':self.__w.element1, 'attack': self.__w.element1_attack}
            elements.append(e1)
        if self.__w.element2 != '-':
            e2 = {'name':self.__w.element2, 'attack': self.__w.element2_attack}
            elements.append(e2)
        return elements
        
    def _format_weapon_chain(self):
        previous_weapon = '-'
        next_weapon = '-'
        if self._p_w is not None:
            previous_weapon = self._p_w.name
        if self._n_w is not None:
            next_weapon = self._n_w.name
        return previous_weapon, next_weapon

    def __format_items(self):
        create_items = []
        upgrade_items = []
        if len(self.__c_i) > 0:
            for i in self.__c_i:
                create_items.append({'name':i[0], 'quantity':i[1]})
        if len(self.__u_i) > 0:
            for i in self.__u_i:
                upgrade_items.append({'name':i[0], 'quantity':i[1]})
        
        return create_items, upgrade_items
    
    def serialize(self):
       
        slots = {'1': self.__w.slot_1, '2': self.__w.slot_2, '3': self.__w.slot_3}
        coatings = self.__format_coatings()
        special_ammo, deviation = self.__format_gun_params()
        elements = self.__format_elements()
        previous_weapon, next_weapon = self._format_weapon_chain()
        create_items, upgrade_items = self.__format_items()
        ammo = self.w_a.to_dict()
        dct = {
            'name': self.__w_t.name ,
            'type': self.__w.weapon_type,
            'rarity': self.__w.rarity,
            'attack': self.__w.attack,
            'real-attack': self.__w.attack_true,
            'damage-type': self.__w.damage_type,
            'affinity': self.__w.affinity,
            'defense': self.__w.defense,
            'elderseal': self.__w.elderseal,
            'shelling': self.__w.shelling,
            'shelling-lvl': self.__w.shelling_level,
            'special-ammo': special_ammo,
            'deviation': deviation,
            'elements':elements,
            'slots':slots,
            'coatings':coatings,
            'sharpness': self.__w.sharpness,
            'sharpness-max': self.__w.sharpness_maxed,
            'create-items':create_items,
            'upgrade-items': upgrade_items,
            'ammos':ammo,
            'previous-weapon':previous_weapon,
            'next-weapon': next_weapon
        }
        return dct
    
class SkillSerializer():

    def __init__(self, skill_text, skilltree, decorations, levels):
        self.s_t = skill_text
        self.st = skilltree
        self.j = decorations
        self.l = levels
    
    def serialize(self):
        levels = [{'level':str(l.level), 'description':l.description} for l in self.l]
        jewel = None
        if len(self.j) >=1:
            jewel = {
                        'name':self.j[0][0].name, 
                        'level':str(self.j[0][1].skill_level),
                        'description': self.j[0][0].description,
                        'materials': self.j[0][0].materials,
                        'unlock': self.j[0][0].unlock,
                        'price': str(self.j[0][1].price),
                        'rarity': str(self.j[0][1].rarity),
                        'level': str(self.j[0][1].skill_level),
                        'slot': str(self.j[0][1].slot)
                        }
        dct = {
            'name': self.s_t.name,
            'description': self.s_t.description,
            'icon': self.st.icon_color,
            'levels':levels,
            'jewel': jewel,

        }

        return dct
    
class ArmorSerializer():

    def __init__(self, armorset_text, armorset, pieces_details, skills, craft_items):
        self.as_t = armorset_text
        self.a_s = armorset
        self.details = pieces_details
        self.s = skills
        self.c_i = craft_items
       
    def _format_pieces(self):
        check ={
            'head': False,
            'chest': False,
            'arms': False,
            'waist': False,
            'legs': False
        }
        temp = {
            'head': None,
            'chest': None,
            'arms': None,
            'waist': None,
            'legs': None
        }
        for d in self.details:
            if not check[d[1].armor_type]:
                temp[d[1].armor_type] = {
                        'name': d[0].name,
                        'type':d[1].armor_type,
                        'rarity': d[1].rarity,
                        'min-def': d[1].defense_base,
                        'max-def': d[1].defense_max,
                        'slots':{
                            '1': d[1].slot_1,
                            '2': d[1].slot_2,
                            '3': d[1].slot_3
                        },
                        'resistances':{
                            'fire': d[1].fire,
                            'water': d[1].water,
                            'thunder': d[1].thunder,
                            'ice': d[1].ice,
                            'dragon': d[1].dragon
                        },
                        'skills': [],
                        'crafting-mats':[]
                }
                check[d[1].armor_type] = True
            
        for k in self.s:
            temp[k[0]]['skills'].append({'name':k[1], 'level':k[2]})
        for c in self.c_i:
            temp[c[0]]['crafting-mats'].append({'name':c[2], 'quantity':c[1]})
        return [temp['head'], temp['chest'], temp['arms'], temp['waist'], temp['legs']]
    
    def serialize(self):
        pieces = self._format_pieces()
        dct ={
            'name': self.as_t.name,
            'rarity': self.details[0][1].rarity,
            'set-bonus':{
                'name': 'TODO',
                'description': 'TODO'
            },
            'pieces': pieces
        }

        return dct