import re
import requests
import json

DW_ITEMS_ENDPOINT = 'https://api.datawars2.ie/gw2/v1/items/json/new'

'''
Scrapes Silver's DataWars2 API for TP data.
'''
def scrape_dw():
    res = requests.get(DW_ITEMS_ENDPOINT)

    if res.ok:
        items = res.json()
        print('request successful')
    else:
        print('request failed')
        exit

    dw_items = {item['id']: item for item in items}

    filename = 'dw_items.json'
    print(f'writing to file {filename}')

    with open(filename, 'w') as f:
        json.dump(dw_items, f)

    print('finished writing to file')

def main():
    scrape_dw()

if __name__ == '__main__':
    main()