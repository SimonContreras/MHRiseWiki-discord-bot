from pony import orm
from src.orm.models import (Decoration, DecorationText, Guild, SkillLvlText, 
SkillTree, SkillTreeText, TalismanText, Talisman, TalismanSkill)
from src.orm.serializer import SkillSerializer

class dbSkill():

    def __init__(self):
        self = self

    @orm.db_session
    def get(self, guild_id: str, skill: str):
        guild_lang = orm.select(g.language.id for g in Guild if g.id == guild_id).first()
        st_q = list(orm.select((st_t, st) \
                for st_t in SkillTreeText for  st in SkillTree \
                if (st_t.name == skill and st_t.language.id == guild_lang and st == st_t.skillTree)))
        
        if len(st_q) < 1:
            return None

        decorations = list(orm.select((dt, d) \
                for dt in DecorationText for  d in Decoration \
                if (dt.decoration == d and dt.language.id == guild_lang and d.skilltree == st_q[0][1])))
        
        levels = list(orm.select( sk_t \
                for sk_t in SkillLvlText  \
                if (sk_t.skillTree == st_q[0][1] and sk_t.language.id == guild_lang)))
        
        talisman = list(orm.select((ts, tt, t) \
                for ts in TalismanSkill for  tt in TalismanText for t in Talisman \
                if (ts.skilltree == st_q[0][1] and tt.language.id == guild_lang \
                    and tt.talisman == ts.talisman and tt.talisman == t)))

        return SkillSerializer(st_q[0][0], st_q[0][1], decorations, levels, talisman[0]).serialize()

db_skill = dbSkill()

        