from os import EX_CANTCREAT
from pony import orm
from src.orm.models import Tip
from src.orm.serializer import TipSerializer


class dbTip():

    def __init__(self):
        self = self
    
    @orm.db_session
    def get_tips(self):
        query = orm.select(t for t in Tip)
        if query is None:
            return None
        return TipSerializer(list(query)).serialize_list()

    @orm.db_session
    def create(self, name:str, link:str):
        try:
            tip = Tip(
                name=name,
                link=link
            )
            orm.commit()
        except Exception as e:
            return { 'status':False }
        return { 'status':True, 'name':name }

    @orm.db_session
    def delete(self, name:str):
        try:
            tip = Tip[name].delete()
            orm.commit()
        except Exception as e:
            return { 'status':False, 'name':name }
        return { 'status':True, 'name':name }

db_tip = dbTip()
    

        