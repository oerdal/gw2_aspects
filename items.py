import requests
import json
from util import batch_ids

ITEMS_ENDPOINT = 'https://api.guildwars2.com/v2/items'

'''
Get the list of all item IDs from the GW2 API.
@return the list of item IDs and None if request was unsuccessful
'''
def get_item_ids():
    res = requests.get(ITEMS_ENDPOINT)

    print('requesting item ids from {ITEMS_ENDPOINT}')
    if res.ok:
        item_ids = res.json()
    else:
        print('request failed')
        return None
    return item_ids

'''
Get the item info for the list of item IDs from the GW2 API.
Format of items is different depending on the item type.
Information on the output format: https://wiki.guildwars2.com/wiki/API:2/items#Response
@param item_ids - the list of IDs to query the API with
@return a json object containing the request item(s) information
'''
def get_item_info(item_ids):
    if not item_ids:
        return None

    # batch the ids into groups so api can handle the request
    batched_endpts = batch_ids(ITEMS_ENDPOINT, item_ids)
    num_batches = len(batched_endpts)

    all_items = []

    print(f'begin item collection - {len(item_ids)} items')
    for batch_num, endpt in enumerate(batched_endpts):
        print(f'batch ({batch_num+1}/{num_batches})')
        res = requests.get(endpt)

        if res.ok:
            items = res.json()
        else:
            print('request failed')
            exit
        
        all_items += items
    return all_items

'''
Writes the entire information of the /v2/items API endpoint to a JSON file.
Output file is called "items.json" if successful.
'''
def main():
    item_ids = get_item_ids()
    all_items = get_item_info(item_ids)

    if not all_items:
        print('exiting program')
        exit

    filename = 'items.json'
    print(f'writing to file {filename}')

    with open(filename, 'w') as f:
        json.dump(all_items, f)

    print('finished writing to file')


if __name__ == '__main__':
    main()