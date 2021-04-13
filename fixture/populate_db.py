import os
import sys
sys.path.insert(0,os.getcwd())
from fixture.initial_data import *
from fixture.csv_loaders import *
from src.orm.models import db

@db_session
def populate_database():
    print('III: 1/16 -> Inserting Available languages.')
    load_languages('./fixture/csv/languages.csv')
    load_guild()
    print('III: 2/16 -> Inserting languages headers/titles.')
    language_errors_headers()
    print('III: 3/16 -> Inserting Default guild.')
    print('III: 4/16 -> Inserting common headers/titles.')
    common_errors_headers()
    print('III: 5/16 -> Inserting help command arguments headers/titles.')
    insert_help_commands_and_args()
    print('III: 6/16 -> Inserting not found headers/titles.')
    command_not_found_errors_headers()
    print('III: 7/16 -> Inserting footer headers/titles.')
    footers_headers()
    print('III: 8/16 -> Inserting prefix command headers/titles.')
    prefix_commands_and_headers()
    print('III: 9/16 -> Inserting monster command headers/titles.')
    monster_command_headers()
    more_monster_headers()
    print('III: 10/16 -> Inserting item command headers/titles.')
    item_command_headers()
    more_item_headers()
    print('III: 11/16 -> Inserting weapon command headers/titles')
    weapon_command_headers()
    print('III: 12/16 -> Inserting skill command headers/titles.')
    skill_command_headers()
    print('III: 13/16 -> Inserting armor command headers/titles.')
    armor_command_headers()
    print('III: 14/16 -> Inserting armor command headers/titles.')
    load_locations('./fixture/csv/locations.csv')
    print('III: 15/16 -> Inserting monster data.')
    load_monster_stats('./fixture/csv/monsters-stats.csv')
    load_monster_esp_text('./fixture/csv/monsters-esp-text.csv')
    load_monsters_habitats('./fixture/csv/monsters-habitats.csv')
    print('III: 16/16 -> Inserting items data.')
    load_items('./fixture/csv/items.csv')
    load_item_combination('./fixture/csv/item-combination.csv')
    load_item_text('./fixture/csv/items-text-esp.csv')
    load_item_location('./fixture/csv/location-items.csv')
    load_skilltrees('./fixture/csv/skilltrees.csv')
    load_skilltreeText('./fixture/csv/skilltreetext-esp.csv')
    load_skilllvlText('./fixture/csv/skilllvltext-esp.csv')
    load_decorations('./fixture/csv/decorations.csv')
    load_decorationsText('./fixture/csv/decorationtext-esp.csv')
    print('III: Initial data done!!')
    

if __name__ == "__main__":
    print('I: -> Creating tables...')
    db.create_tables(check_tables=True)
    print('II: -> Inserting data...')
    populate_database()
    