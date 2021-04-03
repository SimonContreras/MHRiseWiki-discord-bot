import os
import sys
sys.path.insert(0,os.getcwd())
import csv
from pony.orm import *
from src.orm.models import *

def str_to_bool(s:str):
    if s == 'TRUE':
        return True
    return False


@db_session
def load_languages(filename):
    with open(filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for r in csv_reader:
            #id,name,initials
            print(r)
            language = Language(
                id=r[0],
                name=r[1],
                initials=r[2]
            )
            commit()

@db_session
def load_locations(filename):
    with open(filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for r in csv_reader:
            #id,language,name
            print(r)
            location = Location(
                id=r[0],
                language=r[1],
                name=r[2]
            )
            commit()

@db_session
def load_monster_stats(filename):
    with open(filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for r in csv_reader:
            print(r)
            m = Monster(
                id=int(r[0]), 
                size=r[1], 
                icon=r[2],
                danger_level=r[3],
                pitfall_trap=str_to_bool(r[4]),
                shock_trap=str_to_bool(r[5]),
                has_weakness=str_to_bool(r[6]), 
                has_alt_weakness=str_to_bool(r[7]), 
                weakness_fire=int(r[8]), 
                weakness_water=int(r[9]), 
                weakness_ice=int(r[10]), 
                weakness_thunder=int(r[11]), 
                weakness_dragon=int(r[12]), 
                weakness_poison=int(r[13]), 
                weakness_sleep=int(r[14]), 
                weakness_paralysis=int(r[15]), 
                weakness_blast=int(r[16]), 
                weakness_stun=int(r[17]), 
                weakness_exhaust=int(r[18]), 
                plague_fire=int(r[19]), 
                plague_water=int(r[20]), 
                pague_thunder=int(r[21]), 
                plague_ice=int(r[22]), 
                alt_weakness_fire=int(r[23]), 
                alt_weakness_water=int(r[24]), 
                alt_weakness_ice=int(r[25]), 
                alt_weakness_thunder=int(r[26]),
                alt_weakness_dragon=int(r[27]), 
                alt_weakness_poison=int(r[28]), 
                alt_weakness_sleep=int(r[29]), 
                alt_weakness_paralysis=int(r[30]), 
                alt_weakness_blast=int(r[31]), 
                alt_weakness_stun=int(r[32]), 
                alt_weakness_exhaust=int(r[33]), 
                alt_plague_fire=int(r[34]), 
                alt_plague_water=int(r[35]), 
                alt_pague_thunder=int(r[36]), 
                alt_plague_ice=int(r[37]), 
                ailment_roar=r[38],
                ailment_wind=r[39],
                ailment_tremor=r[40],
                ailment_defensedown=str_to_bool(r[41]),
                ailment_fireblight=str_to_bool(r[42]),
                ailment_waterblight=str_to_bool(r[43]),
                ailment_thunderblight=str_to_bool(r[44]),
                ailment_iceblight=str_to_bool(r[45]),
                ailment_dragonblight=str_to_bool(r[46]),
                ailment_blastblight=str_to_bool(r[47]),
                ailment_poison=str_to_bool(r[48]),
                ailment_sleep=str_to_bool(r[49]),
                ailment_paralysis=str_to_bool(r[50]),
                ailment_bleed=str_to_bool(r[51]),
                ailment_stun=str_to_bool(r[52]),
                ailment_mud=str_to_bool(r[53]),
                ailment_bubbleblight=str_to_bool(r[54]),
                ailment_dung=str_to_bool(r[55]),
                ailment_hellfireblight=str_to_bool(r[56]), 
                ailment_webbed=str_to_bool(r[57]), 
            )
            commit()

@db_session
def load_monster_esp_text(filename):
    with open(filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for r in csv_reader:
            print(r)
            mt = MonsterText(
                monster=int(r[0]),
                language=int(r[1]),
                name=r[2],
                species=r[3],
                description=r[4],
                hzv_img=r[5],
                drops_low_rank_img=r[6], 
                drops_high_rank_img=r[7], 
                drops_g_rank_img=r[8], 
                alt_state_description=r[9],
            )
            commit()

@db_session
def load_monsters_habitats(filename):
    with open(filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for r in csv_reader:
            print(r)
            mt = MonsterHabitat(
                    monster=int(r[0]),
                    location=(r[1],r[2]),
                    start_area=int(r[3]),
                    move_area=int(r[4]),
                    rest_area=int(r[5]),
                )
            commit()
@db_session
def load_guild():
    g1 = Guild(
        id='807761997285818378',
        prefix='?',
        language=1
        )
    g2 = Guild(
        id='766821892031119361',
        prefix='?',
        language=1
        )
    commit()



        