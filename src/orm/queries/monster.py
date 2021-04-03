from pony import orm
from src.orm.models import (Guild, MonsterText, MonsterBreak, MonsterBreakText, db)
from src.orm.queries.raw_sql import habitats_sql
from src.orm.serializer import MonsterSerializer

class dbMonster():

    def __init__(self):
        self = self
        self.__db = db

    @orm.db_session
    def get_monster(self, guild_id: str, monster: str):
        guild_lang = orm.select(g.language.id for g in Guild if g.id == guild_id).first()
        m_q = orm.select((mt, mt.monster) for mt in MonsterText \
            if (mt.name == monster and mt.language.id == guild_lang)).first()
        
        if m_q is None:
            return None

        monster_id = m_q[1].id
        habitat = self.__db.select(habitats_sql)
        breaks = orm.select((b, bt) for b in MonsterBreak for bt in MonsterBreakText \
            if (b.monster == m_q[1] and bt.monster_break == b and bt.language.id == guild_lang))
        
        return MonsterSerializer(m_q, list(habitat), list(breaks), guild_lang).serialize()
    
    @orm.db_session
    def get_hzv(self, guild_id: str, monster: str):
        guild_lang = orm.select(g.language.id for g in Guild if g.id == guild_id).first()
        m_t = orm.select(mt for mt in MonsterText \
            if (mt.name == monster and mt.language.id == guild_lang)).first()
        
        if m_t is None:
            return None
        
        return {'name': m_t.name, 'img-url': m_t.hzv_img}
    
    @orm.db_session
    def get_drops(self, guild_id: str, monster: str, rank:str):
        guild_lang = orm.select(g.language.id for g in Guild if g.id == guild_id).first()
        m_t = orm.select(mt for mt in MonsterText \
            if (mt.name == monster and mt.language.id == guild_lang)).first()
        
        if m_t is None:
            return None
        elif rank in ['low', 'bajo']:
            return {'name': m_t.name, 'img-url': m_t.drops_low_rank_img, 'language':guild_lang }
        elif rank in ['high', 'alto']:
            return {'name': m_t.name, 'img-url': m_t.drops_high_rank_img, 'language':guild_lang }
        elif rank in ['master', 'g', 'maestro']:
            return {'name': m_t.name, 'img-url': m_t.drops_g_rank_img, 'language':guild_lang }
        else:
            return None
    

db_monster = dbMonster()

        