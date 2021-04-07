from pony import orm
from src.orm.models import Guild, db
from src.orm.serializer import ItemSerializer
from src.orm.queries.raw_sql import info_item_sql, location_item_sql

class dbItem():

    def __init__(self):
        self.__db = db

    @orm.db_session
    def get_item(self, guild_id: str, item: str):
        guild_lang = orm.select(g.language.id for g in Guild if g.id == guild_id).first()
        query = self.__db.select(info_item_sql)
        if len(query) < 1:
            return None
        
        item_id = query[0].id
        locations = self.__db.select(location_item_sql)

        return ItemSerializer(query[0], locations).serialize()
    
db_item = dbItem()

        