import os
import sys
sys.path.insert(0,os.getcwd())
from fixture.initial_data import *
from fixture.csv_loaders import *
from src.orm.models import db

@db_session
def populate_database():
    print('III: 1/18 -> Inserting Available languages.')
    load_languages('./fixture/csv/language.csv')
    load_guild()
    print('III: 2/18 -> Inserting languages headers/titles.')
    language_errors_headers()
    print('III: 3/18 -> Inserting Default guild.')
    print('III: 4/18 -> Inserting common headers/titles.')
    common_errors_headers()
    print('III: 5/18 -> Inserting help command arguments headers/titles.')
    insert_help_commands_and_args()
    print('III: 6/18 -> Inserting not found headers/titles.')
    command_not_found_errors_headers()
    print('III: 7/18 -> Inserting footer headers/titles.')
    footers_headers()
    print('III: 8/18 -> Inserting prefix command headers/titles.')
    prefix_commands_and_headers()
    print('III: 9/18 -> Inserting monster command headers/titles.')
    monster_command_headers()
    more_monster_headers()
    print('III: 10/18 -> Inserting item command headers/titles.')
    item_command_headers()
    more_item_headers()
    print('III: 11/18 -> Inserting weapon command headers/titles')
    weapon_command_headers()
    print('III: 12/18 -> Inserting skill command headers/titles.')
    skill_command_headers()
    print('III: 13/18 -> Inserting armor command headers/titles.')
    armor_command_headers()
    print('III: 14/18 -> Inserting armor command headers/titles.')
    load_locations('./fixture/csv/location.csv')
    print('III: 15/18 -> Inserting monster data.')
    load_monster_stats('./fixture/csv/monster.csv')
    load_monster_text('./fixture/csv/monsterText.csv')
    load_monsters_habitats('./fixture/csv/monsterHabitat.csv')
    print('III: 16/18 -> Inserting items data.')
    load_items('./fixture/csv/item.csv')
    load_item_combination('./fixture/csv/itemCombination.csv')
    load_item_text('./fixture/csv/itemText.csv')
    load_item_location('./fixture/csv/locationItem.csv')
    print('III: 17/18 -> Inserting skills data.')
    load_skilltrees('./fixture/csv/skilltree.csv')
    load_skilltreeText('./fixture/csv/skilltreeText.csv')
    load_skilllvlText('./fixture/csv/skilllvlText.csv')
    print('III: 18/18 -> Inserting Decorations data.')
    load_decorations('./fixture/csv/decoration.csv')
    load_decorationsText('./fixture/csv/decorationText.csv')
    print('III: Initial data done!!')
    

if __name__ == "__main__":
    print('I: -> Creating tables...')
    db.create_tables(check_tables=True)
    print('II: -> Inserting data...')
    populate_database()
    