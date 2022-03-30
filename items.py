import requests
import json
from util import batch_ids

items_endpt = 'https://api.guildwars2.com/v2/items'

res = requests.get(items_endpt)

if res.ok:
    item_ids = res.json()
    print('request successful')
else:
    print('request failed')
    exit

# batch the ids into groups so api can handle the request
batched_endpts = batch_ids(items_endpt, item_ids)

all_items = []

for endpt in batched_endpts:
    res = requests.get(endpt)

    if res.ok:
        items = res.json()
        print('request successful')
    else:
        print('request failed')
        exit
    
    all_items += items

filename = 'items.json'
print(f'writing to file {filename}')

with open(filename, 'w') as f:
    json.dump(all_items, f)

print('finished writing to file')
