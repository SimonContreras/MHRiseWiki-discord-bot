from pony import orm
from src.orm.models import (Guild, Weapon, WeaponText, WeaponAmmo, db)
from src.orm.serializer import WeaponSerializer
from src.orm.queries.raw_sql import create_items_sql, upgrade_items_sql

class dbWeapon():

    def __init__(self):
        self.__db = db

    @orm.db_session
    def get(self, guild_id: str, weapon: str):
        guild_lang = orm.select(g.language.id for g in Guild if g.id == guild_id).first()
        w_q = list(orm.select((wt, w, wa, w.melodies, w.armorset_bonus, w.skills) \
                for wt in WeaponText for  wa in WeaponAmmo for w in Weapon \
                if (wt.name == weapon and wt.language.id == guild_lang and w == wt.weapon and wa.weapon == wt.weapon)))
        
        if len(w_q) < 1:
            return None

        prev_wp = None
        if w_q[0][1].previous_weapon != 0:
            prev_wp = orm.select(wt for wt in WeaponText \
                if (wt.language.id == guild_lang and wt.weapon.id == w_q[0][1].previous_weapon)).first()

        next_wp =  orm.select(wt for w in Weapon for wt in WeaponText  \
            if ( w.previous_weapon == w_q[0][1].id and wt.language.id == guild_lang and wt.weapon == w)).first()

        create_items = self.__db.select(create_items_sql)
        upgrade_items = self.__db.select(upgrade_items_sql)

        return WeaponSerializer(w_q[0][0], w_q[0][1], w_q[0][2], prev_wp, next_wp, create_items, \
                                upgrade_items, w_q[0][3], w_q[0][4], w_q[0][5]).serialize()
    

db_weapon = dbWeapon()

        