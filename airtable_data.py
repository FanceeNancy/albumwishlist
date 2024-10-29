import requests
from airtable import airtable
from pyairtable import Api
import os
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_TOKEN = os.getenv('AIRTABLE_TOKEN')
#  ✅ Input data from Records table to get a list of barcodes
# TODO: ⏹️ Turn this into OOP to be used in main.py

# ✅ Put AIRTABLE_TOKEN into .env file.

# Base Forty-Five / 2024
BASE_ID = "appUDvN2sOYn5YR73"
# Table 🎶Records; using the table id ensures that renaming the table won't affect this code
TABLE_ID = "tblfihYNdWFnwu3Ct"

api = Api(AIRTABLE_TOKEN)
table = api.table(BASE_ID, TABLE_ID)

airtable_endpoint = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_ID}"

view_name = "With Barcodes"
field_names = ["fldkU7NzZu5ny8NQ"]

headers = {"Authorization": f"Bearer {AIRTABLE_TOKEN}"}

query_params = {
    "view": view_name,
    #"fields": field_names
}


# This class is responsible for gathering data from Airtable

class AtDataManager:
    def __init__(self):
        self.barcodes = []
        self.album_and_artist = []
        self.look_into_these = []

    def get_barcodes(self):
        at_response = requests.get(airtable_endpoint, headers=headers, data=query_params)
        at_data = at_response.json()
        # ✅ Add list of album names with no barcode for separate search
        # ✅ Add exception for TypeError that comes up during: print(i['fields']['Barcode']['text']) after barcode
        # 098787055016
        for i in at_data['records']:
            try:
                self.barcodes.append(i['fields']['Barcode']['text'])
            except KeyError:
                self.album_and_artist.append((i['fields']['Album'], i['fields']['Artist']))
            except TypeError as message:
                print(f'{message} at line {i}')
                self.look_into_these.append(i)
        return self.barcodes

    def get_album_and_artist(self):
        return self.album_and_artist

    def get_look_into_these(self):
        return self.look_into_these

# TEST
# test_album_and_artist = [('Mind, Man, Medicine', 'Secret Sisters'), ('Live at San Quentin', 'Johnny Cash'),
#                          ('Young Mountain (10th Anniv. Edition)', 'This Will Destroy You'),
#                          ('Live in Reykjavik, Iceland', 'This Will Destroy You'), ('Jingle Bell Rock', 'Bobby Helms'),
#                          ('Blue', 'Joni Mitchell'), ('how strange, innocence', 'Explosions in the Sky'),
#                          ('Diamonds In The Rough', 'John Prine'), ('Are We There', 'Sharon Van Etten'),
#                          ('Remind Me Tomorrow', 'Sharon Van Etten'), ('Tapestry ', 'Carole King'),
#                          ('Elvis Sings the Wonderful World of Christmas', 'Elvis Presley'),
#                          ('Every New Beginning ', 'Kim Richey'), ('Greatest Hits', 'The White Stripes'),
#                          ("Ramblin' on My Mind", 'Lucinda Williams'), ('By Blood', 'Shovels & Rope'),
#                          ('Mingus', 'Joni Mitchell'), ('Father Christmas', 'The Kinks'),
#                          ('Weathervanes', 'Jason Isbell'), ('I Am Easy to Find', 'The National'),
#                          ('Drunkards Prayer', 'Over the Rhine'), ('A Christmas Carol', 'Charles Dickens'),
#                          ('Four Concertos', 'J.S. Bach'), ('For the Roses', 'Joni Mitchell'),
#                          ('Laugh Track', 'The National'), ('Southeastern', 'Jason Isbell'),
#                          ('End', 'Explosions In The Sky'), ("I Don't Want To Let You Down", 'Sharon Van Etten'),
#                          ('Entering Heaven Alive', 'Jack White '), ('Prince Avalanche', 'Explosions in the Sky'),
#                          ("Handel's Messiah", 'Handel'), ('First Two Pages of Frankenstein ', 'The National'),
#                          ('Fear of the Dawn', 'Jack White')]

# for i in test_album_and_artist:
#     #print(i[0])
#     album = i[0]
#     artist = i[1]
#     test_type = 'release'
#     print(f"query={album}, type={test_type}, artist={artist}")
