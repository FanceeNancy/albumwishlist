import discogs_client
import csv
import pprint
from airtable_data import AtDataManager
from barcode_sandbox import BarcodeSandbox

at_data = AtDataManager()
barcode_sandbox = BarcodeSandbox()

current_barcodes = at_data.get_barcodes()
current_albums = at_data.get_album_and_artist()
look_into_these = at_data.get_look_into_these()
# print(f"Barcodes: {current_barcodes}")
# print(f"Albums: {current_albums}")
# print(f"Extras: {look_into_these}")

# d = discogs_client.Client('ExampleApplication/1.0', user_token='nsCPnrovJpBJHqgIEyeNhZpeJBfEZkvKukxBaOVm')

# for i in current_albums:
#     results = d.search(query=i[0], type='release', artist=i[1])
#     print(results.page(1))


# for i in test_album_and_artist:
#     #print(i[0])
#     album = i[0]
#     artist = i[1]
#     test_type = 'release'
#     print(f"query={album}, type={test_type}, artist={artist}")
print(current_barcodes)

# what_i_have = barcode_sandbox.get_barcode_data(current_barcodes)