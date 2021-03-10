from pony import orm
from src.orm.models import (Guild, ArmorSetText, ArmorSet, Armor, ArmorText, ArmorSkill, db)
from src.orm.serializer import ArmorSerializer
from src.orm.queries.raw_sql import skill_armor_sql, craft_items_armor_sql

class dbArmor():

    def __init__(self):
        self.__db = db
  
    @orm.db_session
    def get(self, guild_id: str, armor: str):
        guild_lang = orm.select(g.language.id for g in Guild if g.id == guild_id).first()
        a_q = list(orm.select((as_t, a_s) \
                for a_t in ArmorText for as_t in ArmorSetText for  a_s in ArmorSet for a in Armor \
                if (a_t.name == armor and as_t.language.id == guild_lang and a_t.armor == a )))
        
        if len(a_q) < 1:
            return None
        
        pieces_details = list(orm.select((a_t, a) \
                for a_t in ArmorText for a in Armor for a_s in ArmorSkill \
                if (a_t.language.id == guild_lang and a.armorset == a_q[0][1] and a_t.armor == a \
                    and a_s.armor == a)))
        
        armorset_id = a_q[0][1].id
        skills = self.__db.select(skill_armor_sql)
        craft_items = self.__db.select(craft_items_armor_sql)
        
        
        return ArmorSerializer(a_q[0][0], a_q[0][1], pieces_details, skills, craft_items).serialize()

db_armor = dbArmor()

        