from pony import orm
from src.orm.models import (Guild, MonsterText, MonsterHabitat, MonsterHitzone, 
MonsterHitzoneText, MonsterBreak, MonsterBreakText, Location)
from src.orm.serializer import MonsterSerializer

class dbMonster():

    def __init__(self):
        self = self

    @orm.db_session
    def get_monster(self, guild_id: str, monster: str):
        guild_lang = orm.select(g.language.id for g in Guild if g.id == guild_id).first()
        m_q = orm.select((mt, mt.monster) for mt in MonsterText \
            if (mt.name == monster and mt.language.id == guild_lang)).first()
        
        if m_q is None:
            return None
        
        habitat = orm.select(l for h in MonsterHabitat for l in Location \
            if (h.monster == m_q[1] and l.language.id == guild_lang))
        hitzones = orm.select((hz, hzt) for hz in MonsterHitzone for hzt in MonsterHitzoneText \
            if (hz.monster == m_q[1] and hzt.hitzone == hz and hzt.language.id == guild_lang))
        breaks = orm.select((b, bt) for b in MonsterBreak for bt in MonsterBreakText \
            if (b.monster == m_q[1] and bt.monster_break == b and bt.language.id == guild_lang))
        
        return MonsterSerializer(m_q, list(habitat), list(hitzones), list(breaks), guild_lang).serialize()
    

db_monster = dbMonster()

        