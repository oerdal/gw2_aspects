import json

armor_json = []

with open('items.json', 'r') as f:
    items = json.load(f)

for item in items:
    if (item['type'] == 'Armor' and
        item['rarity'] == 'Exotic' and
        'NoSalvage' not in item['flags'] and 
        'suffix_item_id' in item['details']):
        armor_json.append(item)

filename = 'armor.json'
print(f'writing to file {filename}')

with open(filename, 'w') as f:
    json.dump(armor_json, f)

print('finished writing to file')