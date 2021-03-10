/*
Retrieves info for Item embed
*/
SELECT 
it.name AS 'name',
it.description AS 'description', 
i.category AS 'category', 
i.subcategory AS 'subcategory', 
i.rarity AS 'rarity', 
i.buy_price AS 'buy_price', 
i.sell_price AS 'sell_price', 
i.carry_limit AS 'carry_limit', 
i.craftable AS 'craftable', 
i.points AS 'points', 
i.icon_name AS 'icon_name', 
i.icon_color AS 'icon_color',
ic.quantity_first AS 'quantity_first', 
ic.quantity_second AS 'quantity_second', 
ic.quantity_result AS 'quantity_result',
it2.name AS 'first_name',
it3.name AS 'second_name'
FROM ItemText AS it
JOIN Item AS i ON i.id = it.item  AND it.language = 1 AND it.name = 'pocion' 
LEFT JOIN ItemCombination ic ON ic.result = i.id
LEFT JOIN ItemText it2 ON it2.item = ic.first AND it2.language = 1
LEFT JOIN ItemText it3 ON it3.item = ic.second AND it3.language = 1


/*
Retrieve error message for exceptions related to commands
*/
SELECT
h.translation AS 'translation',
h.name AS 'name'
FROM Header as h 
JOIN Command as c ON h.command = c.id
JOIN Guild as g ON g.id = '807761997285818378' and c.language = g.language
WHERE h.type = 'command_not_found'

/*
Retrieve commands related to certain scope and language
*/
SELECT
c.name AS 'name',
c.description AS 'description',
a.name AS 'argument'
FROM Command AS c 
JOIN Argument AS a ON a.command = c.id
JOIN Guild AS g ON g.id = '807761997285818378' AND c.language = g.language
WHERE c.name != 'ayuda' AND c.scope = 'anyone'

/*
Retrieve name and quantity of items required to create certain weapon
*/
SELECT
it.name AS 'name',
ri.requireditem_quantity AS 'quantity'
FROM WeaponText AS wt
JOIN Weapon AS w ON wt.weapon = w.id
JOIN ItemText AS it ON it.language == 1
JOIN RequiredItem_Weapon AS ri ON ri.weapon == w.id AND ri.requireditem_item == it.item
WHERE wt.name == 'cross 1' and wt.language == 1

/*
Retrieve name and quantity of items required to upgrade certain weapon
*/
SELECT
it.name AS 'name',
ri.requireditem_quantity AS 'quantity'
FROM WeaponText AS wt
JOIN Weapon AS w ON wt.weapon = w.id
JOIN ItemText AS it ON it.language == 1
JOIN RequiredItem_Weapon_2 AS ri ON ri.weapon == w.id AND ri.requireditem_item == it.item
WHERE wt.name == 'cross 1' and wt.language == 1

/*
Retrieve items for crafting armor piece based on armorset piece id and language
*/
SELECT
a.armor_type AS 'armor_type',
a_ri.requiredItem_quantity AS 'quantity',
i_t.name AS 'name'
FROM  Armor as a
JOIN Armor_RequiredItem as a_ri ON a_ri.armor = a.id
JOIN ItemText as i_t ON i_t.item == a_ri.requiredItem_item AND i_t.language = 1 
WHERE a.armorset = 1

/*
Retrieve skills related to armor pieces based on armorset id and language
*/
SELECT
a.armor_type AS 'armor_type',
st_t.name AS 'skill',
a_s.level AS 'level'
FROM  Armor as a
JOIN ArmorSkill as a_s ON a_s.armor = a.id
JOIN SkillTreeText AS st_t ON st_t.language = 1 AND a_s.skilltree = st_t.skillTree
WHERE a.armorset = 1


