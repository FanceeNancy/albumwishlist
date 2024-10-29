import discogs_client
import csv

#
# ARTIST_NAME = "Brandi Carlile"
#
# d = discogs_client.Client('ExampleApplication/1.0', user_token='REDACTED')
#
# # Run search query for artist to get the artist ID
# results = d.search(query=ARTIST_NAME, type='artist')
#
# artist_id = results[0].id
# # print(artist_id)
#
# artist = d.artist(artist_id)
#
#
# # ⏹️ TODO 1: Put everything into a dictionary
# # ATTEMPT TO SAVE IMAGE TO A FILE FAILED BECAUSE API FORBIDS IT => deferring to collecting the image urls
# # This is not quite right because the album names should be inside another dictionary
#
# artist_dictionary = {"Artist Name": artist.name}
# album_info_dictionary = {}
#
# for release in artist.releases.page(1):
#     if release.images:
#         album_info_dictionary.update(
#             {f"{release.title}":
#                 {"Album Info": {
#                     "Release Year": release.year,
#                     "Discogs ID": release.id,
#                     "Art URL": release.images[0]["uri"]
#                 }}}
#         )
#     else:
#         album_info_dictionary.update(
#             {f"{release.title}":
#                 {"Album Info": {
#                     "Release Year": release.year,
#                     "Discogs ID": release.id,
#                 }}}
#         )
#
# artist_dictionary.update({"Albums": album_info_dictionary})
# pprint.pprint(artist_dictionary)
#
# # TODO 2: Put the dictionary into a CSV
#
# with open(f'artist_dictionaries/{ARTIST_NAME}_artist_and_albums.csv', 'a', newline='') as csvfile:
#     fieldnames = ['Artist Name', 'Album Name', 'Art URL', 'Discogs ID', 'Release Year']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for album in artist_dictionary['Albums']:
#         writer.writerow({'Artist Name': ARTIST_NAME, 'Album Name': album,
#                          'Art URL': artist_dictionary['Albums'][album]['Album Info']['Art URL'],
#                          'Discogs ID': artist_dictionary['Albums'][album]['Album Info']['Discogs ID'],
#                          'Release Year': artist_dictionary['Albums'][album]['Album Info']['Release Year']})
#
# # TODO 3: Question: does it make sense to get the barcode of a release to check it which ones I have?
# #  Is that how I should check my collection?
#
# # TODO 4: what info can I get from the Discogs ID? Make a list of IDs! (probably could have done this earlier)
#
# discog_ids_lst = []
# for album in artist_dictionary['Albums']:
#     discog_ids_lst.append(artist_dictionary['Albums'][album]['Album Info']['Discogs ID'])
#
# print(discog_ids_lst)








# print(d.release(15928801).formats)
# print(d.release(15928801).images[0])

# Parameters for a search query:
# /database/search?q={query}&{?type,title,release_title,credit,artist,anv,label,genre,style,country,year,format,
# catno,barcode,track,submitter,contributor}
