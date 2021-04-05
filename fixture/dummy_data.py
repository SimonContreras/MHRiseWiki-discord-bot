from pony.orm import *
from src.orm.models import *

def dummy_item():
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()

    i1 = Item(
        category='yeet1',
        subcategory='yete1',
        rarity=1,
        buy_price=300,
        sell_price=555,
        carry_limit= 7,
        points=34,
        icon_name='icon_1',
        icon_color='red',
        craftable = False
    )

    i2 = Item(
        category='yeet2',
        subcategory='yetete2',
        rarity=1,
        buy_price=3000,
        sell_price=5575,
        carry_limit= 7654,
        points=3,
        icon_name='icon_2',
        icon_color='green',
        craftable = True
    ) 

    i3 = Item(
        category='yeet3',
        subcategory='y3',
        rarity=1,
        buy_price=30,
        sell_price=575,
        carry_limit= 7684,
        points=37,
        icon_name='icon_3',
        icon_color='blue',
        craftable = True
    )  
    commit()
    iT1 = ItemText(
        item = i1,
        language = spanish,
        name = "hierba",
        description = "descripcion item 1 en esp",
        )

    iT2 = ItemText(
        language = english,
        name = 'item 1 en eng',
        description = 'description item 1 in eng',
        item=i1
    )

    iT3 = ItemText(
        language = spanish,
        name = 'seta-azul',
        description = 'descripcion item 2 en esp',
        item = i2
    )
    iT4 = ItemText(
        language = english,
        name = 'item 2 en eng',
        description = 'descripcion item 2 en eng',
        item = i2
    )

    iT5 = ItemText(
        language = spanish,
        name = 'pocion',
        description = 'descripcion item 3 en esp',
        item = i3
    )
    iT6 = ItemText(
        language = english,
        name = 'item 3 en eng',
        description = 'descripcion item 3 en eng',
        item = i3
    )

    iC = ItemCombination(
        first= i1,
        second= i2,
        result = i3,
        quantity_first= 4,
        quantity_second= 1,
        quantity_result= 6,
    )


def dummy_monster():
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()

    m = Monster(
        size='large',
        icon='alatreon.png',
        has_weakness = True, 
        has_alt_weakness = True, 
        weakness_fire = 0,
        weakness_water = 1,
        weakness_ice = 2,
        weakness_thunder = 3,
        weakness_dragon = 3,
        weakness_poison = 2,
        weakness_sleep = 1 ,
        weakness_paralysis = 2,
        weakness_blast = 1 ,
        weakness_stun = 0,
        alt_weakness_fire = 0,
        alt_weakness_water = 2,
        alt_weakness_ice = 2,
        alt_weakness_thunder = 3,
        alt_weakness_dragon = 1,
        alt_weakness_poison = 1,
        alt_weakness_sleep = 2,
        alt_weakness_paralysis = 3,
        alt_weakness_blast = 1,
        alt_weakness_stun =2,
        ailment_roar = 'large',
        ailment_wind = 'large',
        ailment_tremor = 'large',
        ailment_defensedown = False,
        ailment_fireblight = True,
        ailment_waterblight = False,
        ailment_thunderblight = True,
        ailment_iceblight = True,
        ailment_dragonblight = True,
        ailment_blastblight = True,
        ailment_regional = False,
        ailment_poison = False,
        ailment_sleep = False,
        ailment_paralysis = False,
        ailment_bleed =False,
        ailment_stun =False,
        ailment_mud = False,
        ailment_effluvia = True
    )

    eng = MonsterText(
        language=english,
        monster=m,
        name='alatreon',
        species='elder dragon',
        hzv_img='great-izuchi.png',
        description='Known as a symbol of destruction, it\'s rumored to harness the full force of nature, but no records remain. ',
        alt_state_description = 'enraged mode'
    )

    esp = MonsterText(
        language=spanish,
        monster=m,
        name='alatreon',
        species='Dragon Anciano',
        hzv_img='great-izuchi.png',
        description='Un símbolo de destrucción. Se dice que puede controlar a toda la naturaleza, pero no hay registros sobre ello. ',
        alt_state_description = 'modo furia'
    )

    l1_esp = Location(
        id=1,
        language=spanish,
        name='BosquePrimigenio'
    )
    l2_esp = Location(
        id=2,
        language=spanish,
        name='Isla Ingle'
    )
    l1_eng = Location(
        id=1,
        language=english,
        name='Bosque Primigénio'
    )
    l2_eng = Location(
        id=2,
        language=english,
        name='Isla Ingle'
    )
    mhab1 = MonsterHabitat(
        monster=m,
        location=l1_esp
    )
    mhab2 = MonsterHabitat(
        monster=m,
        location=l2_esp
    )
    mhab3 = MonsterHabitat(
        monster=m,
        location=l1_eng
    )
    mhab4 = MonsterHabitat(
        monster=m,
        location=l2_eng
    )
    hz1 = MonsterHitzone(
        monster=m,
        cut=20,
        impact=10,
        shot=20,
        fire=20,
        water=30,
        ice=40,
        thunder=40,
        dragon=40,
        ko=5
    )
    hz2 = MonsterHitzone(
        monster=m,
        cut=50,
        impact=0,
        shot=20,
        fire=12,
        water=40,
        ice=12,
        thunder=40,
        dragon=20,
        ko=9
    )
    hz3 = MonsterHitzone(
        monster=m,
        cut=10,
        impact=20,
        shot=15,
        fire=53,
        water=78,
        ice=54,
        thunder=32,
        dragon=12,
        ko=12
    )
    thz1_eng = MonsterHitzoneText(
        language=english,
        hitzone=hz1,
        name='head'
    )
    thz1_esp = MonsterHitzoneText(
        language=spanish,
        hitzone=hz1,
        name='cabeza'
    )
    thz2_eng = MonsterHitzoneText(
        language=english,
        hitzone=hz2,
        name='body'
    )
    thz2_esp = MonsterHitzoneText(
        language=spanish,
        hitzone=hz2,
        name='cuerpo'
    )
    thz3_eng = MonsterHitzoneText(
        language=english,
        hitzone=hz3,
        name='tail'
    )
    thz3_esp = MonsterHitzoneText(
        language=spanish,
        hitzone=hz3,
        name='cola'
    )
    hz1_a = MonsterHitzone(
        monster=m,
        alt=True,
        cut=0,
        impact=10,
        shot=20,
        fire=20,
        water=30,
        ice=40,
        thunder=40,
        dragon=40,
        ko=5
    )
    hz2_a = MonsterHitzone(
        monster=m,
        alt=True,
        cut=0,
        impact=0,
        shot=20,
        fire=12,
        water=40,
        ice=12,
        thunder=40,
        dragon=20,
        ko=9
    )
    hz3_a = MonsterHitzone(
        monster=m,
        alt=True,
        cut=0,
        impact=20,
        shot=15,
        fire=53,
        water=78,
        ice=54,
        thunder=32,
        dragon=12,
        ko=12
    )
    thz1_eng = MonsterHitzoneText(
        language=english,
        hitzone=hz1_a,
        name='head'
    )
    thz1_esp = MonsterHitzoneText(
        language=spanish,
        hitzone=hz1_a,
        name='cabeza'
    )
    thz2_eng = MonsterHitzoneText(
        language=english,
        hitzone=hz2_a,
        name='body'
    )
    thz2_esp = MonsterHitzoneText(
        language=spanish,
        hitzone=hz2_a,
        name='cuerpo'
    )
    thz3_eng = MonsterHitzoneText(
        language=english,
        hitzone=hz3_a,
        name='tail'
    )
    thz3_esp = MonsterHitzoneText(
        language=spanish,
        hitzone=hz3_a,
        name='cola'
    )
    b1 = MonsterBreak(
        monster=m,
        wound= 10,
        sever=40
    )
    b2 = MonsterBreak(
        monster=m,
        wound=10,
        sever=50
    )
    b1_esp = MonsterBreakText(
        language=spanish,
        monster_break=b1,
        part_name='cuerno'
    )
    b2_esp = MonsterBreakText(
        language=spanish,
        monster_break=b2,
        part_name='cola'
    )
    b1_eng = MonsterBreakText(
        language=english,
        monster_break=b1,
        part_name='horn'
    )
    b2_eng = MonsterBreakText(
        language=english,
        monster_break=b2,
        part_name='tail'
    )


def dummy_weapons():
    ri_1 = RequiredItem(
        item = 1,
        quantity = 4
    )
    ri_2 = RequiredItem(
        item = 2,
        quantity = 5
    )
    ri_3 = RequiredItem(
        item = 3,
        quantity = 2
    )
    commit()
    w1 = Weapon(
        order_id = 1,
        weapon_type = 'light-bowgun',
        damage_type = 'shot',
        rarity = 10,
        category = 'None',
        create_items =[ri_1],
        upgrade_items = [ri_1, ri_2],
        attack = 231,
        attack_true = 102,
        affinity = 15,
        defense = 100,
        slot_1 = 1,
        slot_2 = 1,
        slot_3 = 1,
        element1 = 'fire',
        element1_attack = 230,
        element2 = 'water',
        element2_attack = 340,
        element_hidden = True,
        elderseal = 'low',
        sharpness = 'blue',
        sharpness_maxed = False,
        craftable = True,
        final = False,
        kinsect_bonus = 'heal',
        phial = 'power',
        phial_power = 120,
        shelling = 'long',
        shelling_level = 5,
        notes ='PYR',
        coating_close = 10,
        coating_power = 20,
        coating_paralysis = 30,
        coating_poison = 20,
        coating_sleep = 20,
        coating_blast = 20
    )
    commit()
    w2 = Weapon(
        order_id = 2,
        weapon_type = 'light-bowgun',
        damage_type = 'shot',
        rarity = 11,
        category = 'None',
        previous_weapon = 1,
        upgrade_items = [ri_2, ri_3],
        attack = 331,
        attack_true = 202,
        affinity = 15,
        defense = 100,
        slot_1 = 1,
        slot_2 = 1,
        slot_3 = 1,
        element1 = 'fire',
        element1_attack = 230,
        element2 = 'water',
        element2_attack = 340,
        element_hidden = True,
        elderseal = 'low',
        sharpness = 'blue',
        sharpness_maxed = False,
        craftable = True,
        final = False,
        kinsect_bonus = 'heal',
        phial = 'power',
        phial_power = 120,
        shelling = 'long',
        shelling_level = 5,
        notes ='PYR',
        coating_close = 10,
        coating_power = 20,
        coating_paralysis = 30,
        coating_poison = 20,
        coating_sleep = 20,
        coating_blast = 20
    )
    commit()
    w3 = Weapon(
        order_id = 3,
        weapon_type = 'light-bowgun',
        damage_type = 'shot',
        rarity = 12,
        category = 'None',
        previous_weapon = 2,
        upgrade_items = [ri_1, ri_3],
        attack = 431,
        attack_true = 302,
        affinity = 15,
        defense = 100,
        slot_1 = 1,
        slot_2 = 1,
        slot_3 = 1,
        element1 = 'fire',
        element1_attack = 230,
        element2 = 'water',
        element2_attack = 340,
        element_hidden = True,
        elderseal = 'low',
        sharpness = 'blue',
        sharpness_maxed = False,
        craftable = True,
        final = False,
        kinsect_bonus = 'heal',
        phial = 'power',
        phial_power = 120,
        shelling = 'long',
        shelling_level = 5,
        notes ='PYR',
        coating_close = 10,
        coating_power = 20,
        coating_paralysis = 30,
        coating_poison = 20,
        coating_sleep = 20,
        coating_blast = 20
    )
    commit()
    w_a_1 = WeaponAmmo(
        weapon = w1
    )
    w_a_2 = WeaponAmmo(
        weapon = w2,
        deviation = 'high',
        special_ammo = 'wyvernblast',
        normal1_clip = 20,
        normal1_rapid = True,
        normal1_recoil = 1,
        normal1_reload = 'slow',
        normal2_clip = 10,
        normal2_rapid = False,
        normal2_recoil = 1,
        normal2_reload = 'slow',
        tranq_clip = 10,
        tranq_recoil = 1,
        tranq_reload = 'normal',
        wyvern_clip = 5,
        wyvern_reload = 'slow'
    )
    w_a_3 = WeaponAmmo(
        weapon = w3
    )

    wt_1_esp = WeaponText(
        weapon = w1,
        language = 1,
        name = 'cross 1',
    )
    wt_2_esp = WeaponText(
        weapon = w2,
        language = 1,
        name = 'cross 2',
    )
    wt_3_esp = WeaponText(
        weapon = w3,
        language = 1,
        name = 'cross 3',
    )
    wt_1_eng = WeaponText(
        weapon = w1,
        language = 2,
        name = 'cross 1',
    )
    wt_2_eng = WeaponText(
        weapon = w2,
        language = 2,
        name = 'cross 2',
    )
    wt_3_eng = WeaponText(
        weapon = w3,
        language = 2,
        name = 'cross 3',
    )
    commit()


def dummy_skill():
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()

    st = SkillTree(
        max_level=3,
        icon_color='red',
        secret=3,
    )
    commit()
    st_esp = SkillTreeText(
        skillTree=st,
        language = spanish,
        name='bonus punto debil',
        description='Aumenta la afinidad de ataques que aprovechan el punto débil de un monstruo.'
    )
    st_eng = SkillTreeText(
        skillTree=st,
        language = english,
        name='weakness exploit',
        description='Increases the affinity of attacks that exploit a monster weak spot.'
    )
    wex_1_esp = SkillLvlText(
        skillTree=st,
        language=spanish,
        level=1,
        description='Los ataques en puntos débiles tienen afinidad +10%, más un 5% adicional sobre partes heridas.'
    )
    wex_2_esp = SkillLvlText(
        skillTree=st,
        language=spanish,
        level=2,
        description='Los ataques en puntos débiles tienen afinidad +15%, más un 15% adicional sobre partes heridas.'
    )
    wex_3_esp = SkillLvlText(
        skillTree=st,
        language=spanish,
        level=3,
        description='Los ataques en puntos débiles tienen afinidad +30%, más un 20% adicional sobre partes heridas.'
    )
    wex_1_eng = SkillLvlText(
        skillTree=st,
        language=english,
        level=1,
        description='Attacks that hit weak spots have 10% increased affinity, with an extra 5% on wounded parts.'
    )
    wex_2_eng = SkillLvlText(
        skillTree=st,
        language=english,
        level=2,
        description='Attacks that hit weak spots have 15% increased affinity, with an extra 15% on wounded parts.'
    )
    wex_3_eng = SkillLvlText(
        skillTree=st,
        language=english,
        level=3,
        description='Attacks that hit weak spots have 30% increased affinity, with an extra 20% on wounded parts.'
    )


def dummy_decoration():
    st = SkillTree.select(lambda l: l.id == 1).first()
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()
    
    d1 = Decoration(
        slot=1,
        rarity=2,
        price=1000,
        skilltree=st,
        skill_level=1
    )
    d2 = Decoration(
        slot=1,
        rarity=3,
        price=2000,
        skilltree=st,
        skill_level=2
    )
    dt1_esp = DecorationText(
        decoration=d1,
        language=spanish,
        name='Joya ablandadora 1'
    )
    dt2_esp = DecorationText(
        decoration=d2,
        language=spanish,
        name='Joya ablandadora 2'
    )
    dt1_eng = DecorationText(
        decoration=d1,
        language=english,
        name='Tenderizer jewel 1'
    )
    dt2_eng = DecorationText(
        decoration=d2,
        language=english,
        name='Tenderizer Jewel 2'
    )


def dummy_talisman():
    st = SkillTree.select(lambda l: l.id == 1).first()
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()
    
    t = Talisman(
        order_id=1,
        rarity=12,
    )
    commit()
    ts = TalismanSkill(
        talisman=t,
        skilltree=st,
        level=4
    )
    t_esp = TalismanText(
        talisman=t,
        language=spanish,
        name= 'Talisman Provecho',
        description='Aumenta la afinidad de ataques que aprovechan el punto débil de un monstruo. '
    )
    t_eng = TalismanText(
        talisman=t,
        language=english,
        name= 'Exploiter Talisman',
        description='Increases the affinity of attacks that exploit a monster weak spot. '
    )


def dummy_armor():
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()
    monster = Monster.select(lambda l: l.id == 1).first()
    
    a_s = ArmorSet(
        rank = 'low',
        monster = monster,
    )
    as_t_esp = ArmorSetText(
        armorset=a_s,
        language=spanish,
        name='alatreon beta'
    )
    as_t_eng = ArmorSetText(
        armorset=a_s,
        language=english,
        name='alatreon beta english'
    )
    as_b = ArmorSetBonus(
        skilltree=1,
        armorset= a_s,
        pieces_required=3
    )
    as_b_esp = ArmorSetBonusText(
        armorset_bonus=as_b,
        language=spanish,
        name='Divinidad de alatreon',
        description='descripcion de armorset bonus'
    )
    as_b_eng = ArmorSetBonusText(
        armorset_bonus=as_b,
        language=english,
        name='Alatreon divinity',
        description='armorset bonus description'
    )

    head = Armor(
        order_id=1,
        rarity=10,
        rank='low',
        armor_type='head',
        armorset=a_s,
        armorset_bonus=as_b,
        male=True,
        female=True,
        slot_1=1,
        slot_2=1,
        slot_3=2,
        defense_base=200,
        defense_max=500,
        defense_augment_max=600,
        fire=10,
        water=-10,
        thunder=-5,
        ice=20,
        dragon=5
    )
    chest = Armor(
        order_id=1,
        rarity=10,
        rank='low',
        armor_type='chest',
        armorset=a_s,
        armorset_bonus=as_b,
        male=True,
        female=True,
        slot_1=1,
        slot_2=1,
        slot_3=2,
        defense_base=200,
        defense_max=500,
        defense_augment_max=600,
        fire=10,
        water=-10,
        thunder=-5,
        ice=20,
        dragon=5
    )
    arms = Armor(
        order_id=1,
        rarity=10,
        rank='low',
        armor_type='arms',
        armorset=a_s,
        armorset_bonus=as_b,
        male=True,
        female=True,
        slot_1=1,
        slot_2=1,
        slot_3=2,
        defense_base=200,
        defense_max=500,
        defense_augment_max=600,
        fire=10,
        water=-10,
        thunder=-5,
        ice=20,
        dragon=5
    )
    waist = Armor(
        order_id=1,
        rarity=10,
        rank='low',
        armor_type='waist',
        armorset=a_s,
        armorset_bonus=as_b,
        male=True,
        female=True,
        slot_1=1,
        slot_2=1,
        slot_3=2,
        defense_base=200,
        defense_max=500,
        defense_augment_max=600,
        fire=10,
        water=-10,
        thunder=-5,
        ice=20,
        dragon=5
    )
    legs = Armor(
        order_id=1,
        rarity=10,
        rank='low',
        armor_type='legs',
        armorset=a_s,
        armorset_bonus=as_b,
        male=True,
        female=True,
        slot_1=1,
        slot_2=1,
        slot_3=2,
        defense_base=200,
        defense_max=500,
        defense_augment_max=600,
        fire=10,
        water=-10,
        thunder=-5,
        ice=20,
        dragon=5
    )
    a_t1_esp = ArmorText(
        armor = head,
        language=spanish,
        name='cabeza alatreon'
    )
    a_t2_esp = ArmorText(
        armor = chest,
        language=spanish,
        name='pecho alatreon'
    )
    a_t3_esp = ArmorText(
        armor = arms,
        language=spanish,
        name='brazos alatreon'
    )
    a_t4_esp = ArmorText(
        armor = waist,
        language=spanish,
        name='faja alatreon'
    )
    a_t5_esp = ArmorText(
        armor = legs,
        language=spanish,
        name='piernas alatreon'
    )
    a_t1_eng = ArmorText(
        armor = head,
        language=english,
        name='cabeza alatreon'
    )
    a_t2_eng = ArmorText(
        armor = chest,
        language=english,
        name='pecho alatreon'
    )
    a_t3_eng = ArmorText(
        armor = arms,
        language=english,
        name='brazos alatreon'
    )
    a_t4_eng = ArmorText(
        armor = waist,
        language=english,
        name='faja alatreon'
    )
    a_t5_esp = ArmorText(
        armor = legs,
        language=english,
        name='piernas alatreon'
    )
    commit()
    sk_1 = SkillTree.select(lambda l: l.id == 1).first()
    a_s = ArmorSkill(
        armor=head,
        skilltree=sk_1,
        level=2
    )
    a_s2 = ArmorSkill(
        armor=chest,
        skilltree=sk_1,
        level=2
    )
    a_s3 = ArmorSkill(
        armor=arms,
        skilltree=sk_1,
        level=2
    )
    a_s4 = ArmorSkill(
        armor=waist,
        skilltree=sk_1,
        level=2
    )
    a_s5 = ArmorSkill(
        armor=legs,
        skilltree=sk_1,
        level=2
    )
    commit()
    ri1 = RequiredItem.select(lambda l: l.item.id == 1).first()
    ri2 = RequiredItem.select(lambda l: l.item.id == 2).first()
    ri3 = RequiredItem.select(lambda l: l.item.id == 3).first()

    head.craft_items = [ri1]
    chest.craft_items = [ri1, ri2]
    arms.craft_items = [ri1]
    waist.craft_items = [ri1, ri3]
    legs.craft_items = [ri1]
    commit()

@db_session
def dummy():
    print('Inserting dummy data....!!!!')
    dummy_item()
    dummy_monster()
    dummy_weapons()
    dummy_skill()
    dummy_decoration()
    dummy_talisman()
    dummy_armor()
    print('Dummy data done ....!!!!')

