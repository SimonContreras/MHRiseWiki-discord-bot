from enum import unique
import os
from pony.orm import *
from dotenv import load_dotenv
load_dotenv()

db = Database()
db.bind(provider=os.getenv('PROVIDER_DB'), 
        user=os.getenv('USER_DB'),
        password=os.getenv('PASSWORD_DB'),
        host=os.getenv('HOST_DB'),
        port=os.getenv('PORT_DB'),
        database=os.getenv('DATABASE_NAME'))

'''
Miscelaneous 
'''
class Tip(db.Entity):
    name = PrimaryKey(str)
    link = Required(str, unique=True)

'''
Discord and management entities and relations
'''
class Language(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    initials = Required(str)
    is_complete = Required(bool, default=False)

    commands = Set('Command')
    guilds = Set('Guild')
    item_translations = Set('ItemText')
    locations = Set('Location')
    location_camps = Set('LocationCamp')
    monster_texts = Set('MonsterText')
    monster_hitzones_texts = Set('MonsterHitzoneText')
    monster_break_texts = Set('MonsterBreakText')
    monster_reward_condition_texts = Set('MonsterRewardConditionText')
    skillTree_texts = Set('SkillTreeText')
    skillLvls = Set('SkillLvlText')
    armorsets = Set('ArmorSetText')
    armorsets_bonuses = Set('ArmorSetBonusText')
    armor_texts = Set('ArmorText')
    weapon_texts = Set('WeaponText')
    weapon_melody_texts = Set('WeaponMelodyText')
    decoration_texts = Set('DecorationText')
    talisman_texts = Set('TalismanText')
    kinsect_texts = Set('KinsectText')
    quest_texts = Set('QuestText')
    tool_texts = Set('ToolText')

class Command(db.Entity):
    id = PrimaryKey(int, auto=True)
    language = Required(Language)
    name = Required(str)
    title = Required(str)
    description = Required(str)
    scope = Required(str, default='anyone')
    active = Required(bool, default=False)
    arguments = Set('Argument')
    headers = Set('Header')

class Argument(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    command = Required(Command)

class Guild(db.Entity):
    id = PrimaryKey(str)
    prefix = Required(str, default="?")
    language = Required(Language)

class Header(db.Entity):
    id = Required(int, auto=True)
    name = Required(str, default='-')
    translation = Required(str)
    type= Required(str)
    command = Required(Command)
    PrimaryKey(id, command)

'''
MH RISE Entitites and relations
'''
class Item(db.Entity):
    id = PrimaryKey(int, auto=True)
    rarity = Required(int, default=0)
    buy_price = Required(int, default=0)
    sell_price = Required(int, default=0)
    carry_limit = Required(int, default=0)
    craftable = Required(bool, default=False)
    points = Required(int, default=0)
    icon = Required(str, default='unknown.png')


    translations = Set('ItemText')
    comb_first = Set('ItemCombination', reverse='first')
    comb_second = Set('ItemCombination', reverse='second')
    comb_result = Set('ItemCombination', reverse='result')
    location_items = Set('LocationItem')
    monster_rewards = Set('MonsterReward')
    quest_rewards = Set('QuestReward')
    req_items = Set('RequiredItem')

class ItemText(db.Entity):
    language = Required(Language)
    name = Required(str)
    category=Required(str, default='other')
    description = Required(str, default='-')
    obtain_info = Required(str, default='-')
    item = Required(Item)
    PrimaryKey(item, language)

class ItemCombination(db.Entity):
    id = PrimaryKey(int, auto=True)
    first = Required(Item, reverse='comb_first')
    second = Required(Item, reverse='comb_second')
    result = Required(Item, reverse='comb_result')
    quantity_first = Optional(int)
    quantity_second = Optional(int)
    quantity_result = Required(int)

class RequiredItem(db.Entity):
    item = Required(Item)
    quantity = Required(int)
    PrimaryKey(item, quantity)

    armor_pieces = Set('Armor')
    create_weapons = Set('Weapon', reverse='create_items')
    upgrade_weapons = Set('Weapon', reverse='upgrade_items')
    create_talismans = Set('Talisman')
    create_kinsects = Set('Kinsect', reverse='create_items')
    upgrade_kinsects = Set('Kinsect', reverse='upgrade_items')

class Location(db.Entity):
    id = Required(int, auto=True)
    language = Required(Language)
    name = Required(str)
    PrimaryKey(id, language)
    location_items = Set('LocationItem')
    location_camps = Set('LocationCamp')
    monster_locations = Set('MonsterHabitat')
    quests = Set('Quest')

class LocationItem(db.Entity):
    # note: it is possible for there to be multiple entries of the same thing.
    # therefore, this join-table has no "real id" and uses a surrogate instead
    id = PrimaryKey(int, auto=True)
    location = Required(Location)
    area = Required(str, default='0')
    rank = Required(str)
    item = Required(Item)
    stack = Required(int, default=0)
    percentage = Required(int, default=0)
    map_available = Required(bool, default=False)
    map_img = Required(str, default='-')


class LocationCamp(db.Entity):
    """Defines a location camp and a name entry. 
    As this has limited data, its the text entry as well"""
    # This join-table has no "real id" and uses a surrogate instead
    id = PrimaryKey(int, auto=True)
    location = Required(Location)
    language = Required(Language)
    name = Required(str)
    area = Required(int)

class Monster(db.Entity):
    id = PrimaryKey(int, auto=True)
    size = Required(str)
    icon = Required(str)
    danger_level= Required(int)

    pitfall_trap = Required(bool, default=False)
    shock_trap = Required(bool, default=False)

    has_weakness = Required(bool, default=False)
    has_alt_weakness = Required(bool, default=False)

    weakness_fire = Required(int)
    weakness_water = Required(int)
    weakness_ice = Required(int)
    weakness_thunder = Required(int)
    weakness_dragon = Required(int)

    weakness_poison = Required(int)
    weakness_sleep = Required(int)
    weakness_paralysis = Required(int)
    weakness_blast = Required(int)
    weakness_stun = Required(int)
    weakness_exhaust = Required(int)
    
    plague_fire = Required(int)
    plague_water = Required(int)
    pague_thunder = Required(int)
    plague_ice = Required(int)

    alt_weakness_fire = Optional(int)
    alt_weakness_water = Optional(int)
    alt_weakness_ice = Optional(int)
    alt_weakness_thunder =Optional(int)
    alt_weakness_dragon = Optional(int)

    alt_weakness_poison = Optional(int)
    alt_weakness_sleep = Optional(int)
    alt_weakness_paralysis = Optional(int)
    alt_weakness_blast = Optional(int)
    alt_weakness_stun = Optional(int)
    alt_weakness_exhaust = Optional(int)
    
    alt_plague_fire = Optional(int)
    alt_plague_water = Optional(int)
    alt_pague_thunder = Optional(int)
    alt_plague_ice = Optional(int)

    ailment_roar = Required(str)
    ailment_wind = Required(str)
    ailment_tremor = Required(str)
    ailment_defensedown = Required(bool, default=False)
    ailment_fireblight = Required(bool, default=False)
    ailment_waterblight = Required(bool, default=False)
    ailment_thunderblight = Required(bool, default=False)
    ailment_iceblight = Required(bool, default=False)
    ailment_dragonblight = Required(bool, default=False)
    ailment_blastblight = Required(bool, default=False)

    ailment_poison = Required(bool, default=False)
    ailment_sleep = Required(bool, default=False)
    ailment_paralysis = Required(bool, default=False)
    ailment_bleed = Required(bool, default=False)
    ailment_stun = Required(bool, default=False)
    ailment_mud = Required(bool, default=False)
    ailment_bubbleblight = Required(bool, default=False)
    ailment_dung = Required(bool, default=False)
    ailment_hellfireblight = Required(bool, default=False)
    ailment_webbed = Required(bool, default=False)

    translations = Set('MonsterText')
    hitzones = Set('MonsterHitzone')
    breaks = Set('MonsterBreak')
    rewards = Set('MonsterReward')
    habitats = Set('MonsterHabitat')
    armor_sets = Set('ArmorSet')
    quests = Set('QuestMonster')

class MonsterText(db.Entity):
    monster = Required(Monster)
    language = Required(Language)
    name = Optional(str)
    species = Optional(str)
    description = Optional(str)
    hzv_img = Optional(str)
    drops_low_rank_img = Optional(str)
    drops_high_rank_img = Optional(str)
    drops_g_rank_img = Optional(str)
    alt_state_description = Required(str, default='-')
    PrimaryKey(monster, language)

class MonsterHabitat(db.Entity):
    monster = Required(Monster)
    location = Required(Location)
    start_area = Required(int, default=0)
    move_area = Required(int, default=0)
    rest_area = Required(int, default=0)
    PrimaryKey(monster, location)

class MonsterHitzone(db.Entity):
    id = PrimaryKey(int, auto=True)
    alt = Required(bool, default=False)
    monster = Required(Monster)
    cut = Optional(int)
    impact = Optional(int)
    shot = Optional(int)
    fire = Optional(int)
    water = Optional(int)
    ice = Optional(int)
    thunder = Optional(int)
    dragon = Optional(int)
    ko = Optional(int)
    translations = Set('MonsterHitzoneText')

class MonsterHitzoneText(db.Entity):
    hitzone = Required(MonsterHitzone)
    language = Required(Language)
    name = Optional(str)
    PrimaryKey(hitzone, language)

class MonsterBreak(db.Entity):
    id = PrimaryKey(int, auto=True)
    monster = Required(Monster)
    flinch = Optional(int)
    wound = Optional(int)
    sever = Optional(int)
    extract = Optional(str)
    translations = Set('MonsterBreakText')

class MonsterBreakText(db.Entity):
    monster_break = Required(MonsterBreak)
    language = Required(Language)
    part_name = Optional(str)
    PrimaryKey(monster_break, language)

class MonsterReward(db.Entity):
    # note: it is possible for there to be multiple entries of the same thing.
    # therefore, this join-table has no "real id" and uses a surrogate instead
    id = PrimaryKey(int, auto=True)

    monster = Required(Monster)
    conditions = Set('MonsterRewardConditionText') 
    
    rank = Optional(str)
    item = Required(Item)
    
    stack = Optional(int)
    percentage = Optional(int)

class MonsterRewardConditionText(db.Entity):
    id = PrimaryKey(int, auto=True)
    language = Required(Language)
    name = Optional(str)
    monster_reward = Required(MonsterReward)

class SkillTree(db.Entity):
    id = PrimaryKey(int, auto=True)
    max_level = Required(int)
    icon_color = Required(str)
    secret = Required(int, default=0)
    unlocks_tree = Optional('SkillTree', reverse='unlocks_tree')

    translations = Set('SkillTreeText')
    skillLvls = Set('SkillLvlText')
    armor_set_bonus_skills = Set('ArmorSetBonus')
    decorations = Set('Decoration', reverse='skilltree')
    decorations2 = Set('Decoration', reverse='skilltree2')
    talisman_skills = Set('TalismanSkill')
    armor_skills = Set('ArmorSkill')
    weapon_skills = Set('WeaponSkill', reverse='skilltree')

class SkillTreeText(db.Entity):
    skillTree = Required(SkillTree)
    language = Required(Language)
    name = Required(str)
    description = Required(str)
    PrimaryKey(skillTree, language)

class SkillLvlText(db.Entity):
    '''Represents a skill in a skill tree. These are tied to a language'''
    skillTree = Required(SkillTree)
    language = Required(Language)
    level = Required(int)
    description = Required(str)
    PrimaryKey(skillTree, language, level)

class ArmorSet(db.Entity):
    id = PrimaryKey(int, auto=True)
    rank = Required(str)
    monster = Required(Monster)
    armorset_bonus = Optional(int)

    armorset_bonuses = Set('ArmorSetBonus')
    translations = Set('ArmorSetText')
    armor_pieces = Set('Armor')

class ArmorSetText(db.Entity):
    armorset = Required(ArmorSet)
    language = Required(Language)
    name = Required(str)
    PrimaryKey(armorset, language)

class Armor(db.Entity):
    id = PrimaryKey(int, auto=True)
    order_id = Required(int)
    rarity = Required(int)
    rank = Required(str)
    armor_type = Required(str)
    armorset = Required(ArmorSet)
    armorset_bonus = Set('ArmorSetBonus')
    
    male = Required(bool)
    female = Required(bool)
    slot_1 = Required(int)
    slot_2 = Required(int)
    slot_3 = Required(int)
    defense_base = Required(int)
    defense_max = Required(int)
    defense_augment_max = Required(int)
    fire = Required(int)
    water = Required(int)
    thunder = Required(int)
    ice = Required(int)
    dragon = Required(int)

    translations = Set('ArmorText')
    skills = Set('ArmorSkill')
    craft_items = Set('RequiredItem')

class ArmorText(db.Entity):
    armor = Required(Armor)
    language = Required(Language)
    name = Required(str)
    PrimaryKey(armor, language)

class ArmorSkill(db.Entity):
    armor = Required(Armor)
    skilltree = Required(SkillTree)
    level = Required(int)
    PrimaryKey(armor, skilltree)

class ArmorSetBonus(db.Entity):
    skilltree = Required(SkillTree)
    armorset = Required(ArmorSet)
    pieces_required = Required(int)
    armor_pieces = Set(Armor)
    PrimaryKey(armorset, skilltree)

    weapons = Set('Weapon')
    translations = Set('ArmorSetBonusText')

class ArmorSetBonusText(db.Entity):
    armorset_bonus = Required(ArmorSetBonus)
    language = Required(Language)
    name = Required(str)
    description = Required(str)
    PrimaryKey(armorset_bonus, language)

class Weapon(db.Entity):
    id = PrimaryKey(int, auto=True)
    order_id = Required(int)
    weapon_type = Required(str)
    rarity = Required(int)
    category = Required(str)
    damage_type = Required(str)

    previous_weapon = Optional(int, default=0)
    next_weapon = Set('Weapon', reverse='next_weapon')
    create_items =Set(RequiredItem)
    upgrade_items = Set(RequiredItem)
    
    attack = Required(int)
    attack_true = Required(int)
    affinity = Required(int, default=0)
    defense = Optional(int, default=0)
    slot_1 = Required(int, default=0)
    slot_2 = Required(int, default=0)
    slot_3 = Required(int, default=0)

    element1 = Required(str, default='-')
    element1_attack = Required(int, default=0)
    element2 = Required(str, default='-')
    element2_attack = Required(int, default=0)
    element_hidden = Required(bool, default=False)
    elderseal = Required(str, default='-')

    sharpness = Required(str, default='-')
    sharpness_maxed = Required(bool, default=False)

    craftable = Required(bool, default=False)
    final = Required(bool, default=False)

    kinsect_bonus = Required(str, default='-')
    phial =Required(str, default='-')
    phial_power = Required(int, default=0)
    shelling = Required(str, default='-')
    shelling_level = Required(int, default=0)
    notes = Required(str, default='-')

    coating_close = Required(int, default=0)
    coating_power = Required(int, default=0)
    coating_paralysis = Required(int, default=0)
    coating_poison = Required(int, default=0)
    coating_sleep = Required(int, default=0)
    coating_blast = Required(int, default=0)

    ammo = Optional('WeaponAmmo')
    melodies = Optional('WeaponMelody')
    armorset_bonus = Optional(ArmorSetBonus)

    translations = Set('WeaponText')
    skills = Set('WeaponSkill')

class WeaponAmmo(db.Entity):
    weapon = PrimaryKey(Weapon)

    deviation = Required(str, default='-')
    special_ammo = Required(str, default='-')
    
    normal1_clip = Required(int, default=0)
    normal1_rapid = Required(bool, default=False)
    normal1_recoil = Required(int, default=0)
    normal1_reload = Required(str, default='-')
    
    normal2_clip = Required(int, default=0)
    normal2_rapid = Required(bool, default=False)
    normal2_recoil = Required(int, default=0)
    normal2_reload = Required(str, default='-')

    normal3_clip = Required(int, default=0)
    normal3_rapid = Required(bool, default=False)
    normal3_recoil = Required(int, default=0)
    normal3_reload = Required(str, default='-')
    
    pierce1_clip = Required(int, default=0)
    pierce1_rapid = Required(bool, default=False)
    pierce1_recoil = Required(int, default=0)
    pierce1_reload = Required(str, default='-')

    pierce2_clip = Required(int, default=0)
    pierce2_rapid = Required(bool, default=False)
    pierce2_recoil = Required(int, default=0)
    pierce2_reload = Required(str, default='-')

    pierce3_clip = Required(int, default=0)
    pierce3_rapid = Required(bool, default=False)
    pierce3_recoil = Required(int, default=0)
    pierce3_reload = Required(str, default='-')
    
    spread1_clip = Required(int, default=0)
    spread1_rapid = Required(bool, default=False)
    spread1_recoil = Required(int, default=0)
    spread1_reload = Required(str, default='-')

    spread2_clip = Required(int, default=0)
    spread2_rapid = Required(bool, default=False)
    spread2_recoil = Required(int, default=0)
    spread2_reload = Required(str, default='-')

    spread3_clip = Required(int, default=0)
    spread3_rapid = Required(bool, default=False)
    spread3_recoil = Required(int, default=0)
    spread3_reload = Required(str, default='-')
    
    sticky1_clip = Required(int, default=0)
    sticky1_rapid = Required(bool, default=False)
    sticky1_recoil = Required(int, default=0)
    sticky1_reload = Required(str, default='-')

    sticky2_clip = Required(int, default=0)
    sticky2_rapid = Required(bool, default=False)
    sticky2_recoil = Required(int, default=0)
    sticky2_reload = Required(str, default='-')

    sticky3_clip = Required(int, default=0)
    sticky3_rapid = Required(bool, default=False)
    sticky3_recoil = Required(int, default=0)
    sticky3_reload = Required(str, default='-')
    
    cluster1_clip = Required(int, default=0)
    cluster1_rapid = Required(bool, default=False)
    cluster1_recoil = Required(int, default=0)
    cluster1_reload = Required(str, default='-')

    cluster2_clip = Required(int, default=0)
    cluster2_rapid = Required(bool, default=False)
    cluster2_recoil = Required(int, default=0)
    cluster2_reload = Required(str, default='-')
    
    cluster3_clip = Required(int, default=0)
    cluster3_rapid = Required(bool, default=False)
    cluster3_recoil = Required(int, default=0)
    cluster3_reload = Required(str, default='-')
    
    recover1_clip = Required(int, default=0)
    recover1_rapid = Required(bool, default=False)
    recover1_recoil = Required(int, default=0)
    recover1_reload = Required(str, default='-')

    recover2_clip = Required(int, default=0)
    recover2_rapid = Required(bool, default=False)
    recover2_recoil = Required(int, default=0)
    recover2_reload = Required(str, default='-')
    
    poison1_clip = Required(int, default=0)
    poison1_rapid = Required(bool, default=False)
    poison1_recoil = Required(int, default=0)
    poison1_reload = Required(str, default='-')

    poison2_clip = Required(int, default=0)
    poison2_rapid = Required(bool, default=False)
    poison2_recoil = Required(int, default=0)
    poison2_reload = Required(str, default='-')
    
    paralysis1_clip = Required(int, default=0)
    paralysis1_rapid = Required(bool, default=False)
    paralysis1_recoil = Required(int, default=0)
    paralysis1_reload = Required(str, default='-')

    paralysis2_clip = Required(int, default=0)
    paralysis2_rapid = Required(bool, default=False)
    paralysis2_recoil = Required(int, default=0)
    paralysis2_reload = Required(str, default='-')
    
    sleep1_clip = Required(int, default=0)
    sleep1_rapid = Required(bool, default=False)
    sleep1_recoil = Required(int, default=0)
    sleep1_reload = Required(str, default='-')

    sleep2_clip = Required(int, default=0)
    sleep2_rapid = Required(bool, default=False)
    sleep2_recoil = Required(int, default=0)
    sleep2_reload = Required(str, default='-')

    exhaust1_clip = Required(int, default=0)
    exhaust1_rapid = Required(bool, default=False)
    exhaust1_recoil = Required(int, default=0)
    exhaust1_reload = Required(str, default='-')

    exhaust2_clip = Required(int, default=0)
    exhaust2_rapid = Required(bool, default=False)
    exhaust2_recoil = Required(int, default=0)
    exhaust2_reload = Required(str, default='-')

    flaming_clip = Required(int, default=0)
    flaming_rapid = Required(bool, default=False)
    flaming_recoil = Required(int, default=0)
    flaming_reload = Required(str, default='-')

    water_clip = Required(int, default=0)
    water_rapid = Required(bool, default=False)
    water_recoil = Required(int, default=0)
    water_reload = Required(str, default='-')
    
    freeze_clip = Required(int, default=0)
    freeze_rapid = Required(bool, default=False)
    freeze_recoil = Required(int, default=0)
    freeze_reload = Required(str, default='-')

    thunder_clip = Required(int, default=0)
    thunder_rapid = Required(bool, default=False)
    thunder_recoil = Required(int, default=0)
    thunder_reload = Required(str, default='-')
    
    dragon_clip = Required(int, default=0)
    dragon_rapid = Required(bool, default=False)
    dragon_recoil = Required(int, default=0)
    dragon_reload = Required(str, default='-')

    slicing_clip = Required(int, default=0)
    slicing_rapid = Required(bool, default=False)
    slicing_recoil = Required(int, default=0)
    slicing_reload = Required(str, default='-')

    wyvern_clip = Required(int, default=0)
    wyvern_rapid = Required(bool, default=False)
    wyvern_recoil = Required(int, default=0)
    wyvern_reload = Required(str, default='-')

    demon_clip = Required(int, default=0)
    demon_rapid = Required(bool, default=False)
    demon_recoil = Required(int, default=0)
    demon_reload = Required(str, default='-')

    armor_clip = Required(int, default=0)
    armor_rapid = Required(bool, default=False)
    armor_recoil = Required(int, default=0)
    armor_reload = Required(str, default='-')

    tranq_clip = Required(int, default=0)
    tranq_rapid = Required(bool, default=False)
    tranq_recoil = Required(int, default=0)
    tranq_reload = Required(str, default='-')

class WeaponText(db.Entity):
    weapon = Required(Weapon)
    language = Required(Language)
    name = Required(str)
    PrimaryKey(weapon, language)

class WeaponMelody(db.Entity):
    weapon = PrimaryKey(Weapon)
    base_duration = Required(int, default=0)
    base_extension = Required(int, default=0)
    m1_duration = Required(int, default=0)
    m1_extension = Required(int, default=0)
    m2_duration = Required(int, default=0)
    m2_extension = Required(int, default=0)
    
    notes = Set('WeaponMelodyNotes')
    translations = Set('WeaponMelodyText')

class WeaponMelodyNotes(db.Entity):
    weapon_melody = Required(WeaponMelody)
    notes = Required(str)
    PrimaryKey(weapon_melody, notes)

class WeaponMelodyText(db.Entity):
    weapon_melody = Required(WeaponMelody)
    language = Required(Language)
    name = Required(str)
    effect1 = Required(str)
    effect2 = Required(str)
    PrimaryKey(weapon_melody, language)

class WeaponSkill(db.Entity):
    weapon = Required(Weapon)
    skilltree = Required(SkillTree)
    level = Required(int)
    PrimaryKey(weapon, skilltree)

class Decoration(db.Entity):
    id = PrimaryKey(int, auto=True)
    slot = Required(int)
    rarity = Required(int)
    price = Required(int)

    skilltree = Required(SkillTree)
    skill_level = Required(int)
    skilltree2 = Optional(SkillTree)
    skill_level2 = Optional(int)

    translations = Set('DecorationText')
    
class DecorationText(db.Entity):
    decoration = Required(Decoration)
    language = Required(Language)
    name = Required(str)
    description=Required(str)
    unlock=Required(str)
    materials=Required(str)

    PrimaryKey(decoration, language)

class Talisman(db.Entity):
    id = PrimaryKey(int, auto=True)
    order_id = Required(int)
    rarity = Required(int)
    
    previous = Optional('Talisman', reverse='previous')
    craft_items = Set(RequiredItem)

    skills = Set('TalismanSkill')
    translations = Set('TalismanText')

class TalismanSkill(db.Entity):
    talisman = Required(Talisman)
    skilltree = Required(SkillTree)
    level = Required(int)
    PrimaryKey(talisman, skilltree)

class TalismanText(db.Entity):
    talisman = Required(Talisman)
    language = Required(Language)
    name = Required(str)
    description = Required(str)
    PrimaryKey(talisman, language)

class Kinsect(db.Entity):
    id = PrimaryKey(int, auto=True)
    rarity = Required(int)
    
    previous = Optional('Kinsect', reverse='previous')
    create_items = Set(RequiredItem)
    upgrade_items =  Set(RequiredItem)

    attack_type = Required(str)
    dust_effect = Required(str)
    power = Required(int)
    speed = Required(int)
    heal = Required(int)

    final = Required(bool, default=False)
    translations = Set('KinsectText')

class KinsectText(db.Entity):
    kinsect = Required(Kinsect)
    language = Required(Language)
    name = Required(str)
    PrimaryKey(kinsect, language)

class Quest(db.Entity):
    id = PrimaryKey(int, auto=True)
    order_id = Required(int)
    category = Required(str)
    rank = Required(str)
    stars = Required(int)
    stars_raw = Required(int)
    quest_type = Required(str)
    location = Required(Location)
    zenny = Required(int)

    translations = Set('QuestText')
    monsters = Set('QuestMonster')
    rewards = Set('QuestReward')

class QuestText(db.Entity):
    quest = Required(Quest)
    language = Required(Language)
    name = Required(str)
    objective = Required(str)
    description = Required(str)
    PrimaryKey(quest, language)

class QuestMonster(db.Entity):
    quest = Required(Quest)
    monster = Required(Monster)
    quantity = Required(int)
    is_objective = Required(bool, default=False)
    PrimaryKey(quest, monster)

class QuestReward(db.Entity):
    id = PrimaryKey(int, auto=True)
    quest = Required(Quest)
    group = Required(str)
    item = Required(Item)
    stack = Required(int)
    percentage = Required(int)

class Tool(db.Entity):
    id = PrimaryKey(int, auto=True)
    order_id = Required(int)
    tool_type = Required(str)

    duration = Required(int)
    duration_upgraded = Required(int)
    recharge = Required(int)
    
    slot_1 = Required(int)
    slot_2 = Required(int)
    slot_3 = Required(int)

    icon_color = Required(str)
    translations = Set('ToolText')

class ToolText(db.Entity):
    tool = Required(Tool)
    language = Required(Language)
    name = Required(str)
    name_base = Required(str)
    description = Required(str)
    PrimaryKey(tool, language)


db.generate_mapping(create_tables=True, check_tables=True)
   