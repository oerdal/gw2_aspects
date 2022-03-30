import re
import requests
import json

def scrape_dw():
    endpt = 'https://api.datawars2.ie/gw2/v1/items/json/new'

    res = requests.get(endpt)

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