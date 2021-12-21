import re 
from utils import *
from glob import glob
from dateutil.parser import parse

def safe_re(regex:str,string:str):
    res = re.findall(regex,string)
    if res: return res[0]


def get_sold_channel(sold_text:str):
    return safe_re(r'auction|private treaty|Auction|Private Treaty',sold_text)

def get_sold_date(string:str):
    text_split = string.split(" ")
    sold_date = text_split[-3] + ' ' + text_split[-2] + " " + text_split[-1]
    sold_date = str(parse(sold_date)).split(" ")[0]
    return sold_date


print('listing_id,property_type,suburb,state,postcode,bedrooms,bathrooms,parking,landsize,price,sold_date,sold_channel,domain_suburb,lat,lng')
for json_file in glob('/home/binihaiben05/data_study/.vscode/json_data/*.json'):
    data = read_json(json_file)
    for record in data['props']['listingsMap']:
        listing_id = data['props']['listingsMap'][record]['id']
        prop = data['props']['listingsMap'][record]['listingModel']
        suburb = prop['address']['suburb'].lower().replace(' ','-')
        state =  prop['address']['state'].lower()
        postcode = prop['address']['postcode']
        domain_suburb = f'{suburb}-{state}-{postcode}'
        lat = prop['address']['lat']
        lng = prop['address']['lng']
        bedrooms = prop['features']['beds'] if 'beds' in prop['features']  else None 
        bathrooms = prop['features']['baths'] if 'baths' in prop['features']  else None
        parking =  prop['features']['parking'] if 'parking' in prop['features']  else  None
        property_type =  prop['features']['propertyType'] if 'baths' in prop['features']  else  None
        landsize = prop['features']['landSize'] if 'landSize' in prop['features']  else  None
        price = prop['price'].replace('$','').replace(',','')
        sold_text = prop['tags']['tagText']
        sold_date = get_sold_date(sold_text)
        sold_channel = get_sold_channel(sold_text)
        print(f'{listing_id},{property_type},{suburb},{state},{postcode},{bedrooms},{bathrooms},{parking},{landsize},{price},{sold_date},{sold_channel},{domain_suburb},{lat},{lng}') 

