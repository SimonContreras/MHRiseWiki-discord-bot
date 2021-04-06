info_item_sql = '''SELECT 
                    it.name AS "name",
                    it.description AS "description", 
                    it.category AS "category", 
                    i.rarity AS "rarity", 
                    i.buy_price AS "buy_price", 
                    i.sell_price AS "sell_price", 
                    i.carry_limit AS "carry_limit", 
                    i.craftable AS "craftable", 
                    i.points AS "points", 
                    i.icon AS "icon", 

                    ic.quantity_first AS "quantity_first", 
                    ic.quantity_second AS "quantity_second", 
                    ic.quantity_result AS "quantity_result",
                    it2.name AS "first_name",
                    it3.name AS "second_name"
                    FROM ItemText AS it
                    JOIN Item AS i ON i.id = it.item  AND it.language = $guild_lang AND it.name LIKE $item
                    LEFT JOIN ItemCombination ic ON ic.result = i.id
                    LEFT JOIN ItemText it2 ON it2.item = ic.first AND it2.language = $guild_lang
                    LEFT JOIN ItemText it3 ON it3.item = ic.second AND it3.language = $guild_lang'''


create_items_sql = '''SELECT
                        it.name AS "name",
                        ri.requireditem_quantity AS "quantity"
                        FROM WeaponText AS wt
                        JOIN Weapon AS w ON wt.weapon = w.id
                        JOIN ItemText AS it ON it.language = $guild_lang
                        JOIN RequiredItem_Weapon AS ri ON ri.weapon = w.id AND ri.requireditem_item = it.item
                        WHERE wt.name = $weapon and wt.language = $guild_lang'''

upgrade_items_sql = '''SELECT
                        it.name AS "name",
                        ri.requireditem_quantity AS "quantity"
                        FROM WeaponText AS wt
                        JOIN Weapon AS w ON wt.weapon = w.id
                        JOIN ItemText AS it ON it.language = $guild_lang
                        JOIN RequiredItem_Weapon_2 AS ri ON ri.weapon = w.id AND ri.requireditem_item = it.item
                        WHERE wt.name = $weapon and wt.language = $guild_lang'''


craft_items_armor_sql = '''SELECT
                        a.armor_type AS "armor_type",
                        a_ri.requiredItem_quantity AS "quantity",
                        i_t.name AS "name"
                        FROM  Armor as a
                        JOIN Armor_RequiredItem as a_ri ON a_ri.armor = a.id
                        JOIN ItemText as i_t ON i_t.item = a_ri.requiredItem_item AND i_t.language = $guild_lang 
                        WHERE a.armorset = $armorset_id'''


skill_armor_sql = '''SELECT
                            a.armor_type AS "armor_type",
                            st_t.name AS "skill",
                            a_s.level AS "level"
                            FROM  Armor as a
                            JOIN ArmorSkill as a_s ON a_s.armor = a.id
                            JOIN SkillTreeText AS st_t ON st_t.language = $guild_lang AND a_s.skilltree = st_t.skillTree
                            WHERE a.armorset = $armorset_id'''


habitats_sql = '''SELECT 
                        l.name AS "location"
                        FROM monsterhabitat AS mh
                        JOIN location AS l ON l.id = mh.location_id AND l.language = $guild_lang
                        WHERE mh.monster = $monster_id'''
