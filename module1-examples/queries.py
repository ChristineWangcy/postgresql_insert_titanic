total_characters = 'SELECT COUNT(DISTINCT(name)) FROM \
    charactercreator_character'

total_subclass = 'SELECT COUNT(*) FROM charactercreator_necromancer'

total_items = 'SELECT COUNT(*) FROM armory_item'

weapons = 'SELECT COUNT(*) FROM armory_weapon'

character_items = '''SELECT cc.character_id, 
    COUNT(cci.item_id) as items_count 
    FROM charactercreator_character cc
    LEFT JOIN charactercreator_character_inventory cci 
    ON cc.character_id = cci.character_id
    GROUP BY cc.character_id'''

character_weapons = '''
    SELECT cc.character_id, COUNT(w.item_ptr_id) as weapons_count
    FROM charactercreator_character cc LEFT JOIN (
        charactercreator_character_inventory cci
        INNER JOIN armory_weapon w ON cci.item_id = w.item_ptr_id 
    )
    GROUP BY cc.character_id
'''
