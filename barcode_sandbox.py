import discogs_client
import pprint
import csv
from datetime import datetime


class BarcodeSandbox:
    def __init__(self):
        self.album_info_dictionary = {}

    # BARCODE = "687051938492"
    # #BARCODE = "793888106475"
    #
    # BARCODES = ["793888106475", "656605322216", "687051938492"]
    def get_barcode_data(self, barcodes):
        """
        Parses record data from the Discogs API and puts it into a dictionary, then a CSV.
        :param barcode:
        :return:
        """
        d = discogs_client.Client('ExampleApplication/1.0', user_token='REDACTED')

        # results_two = d.search(query=BARCODE, type='barcode')
        # album_info_dictionary = {}

        for bar in barcodes:
            results_three = d.search(query=bar, type='barcode')

            if "artists" not in dir(results_three.page(1)[0]):
                release = results_three.page(1)[1]
            else:
                release = results_three.page(1)[0]

            artist_name = release.artists[0].name
            album_title = release.title
            image_url = release.images[0]["uri"]

            self.all_albums_dictionary = {}
            self.tracks_on_album = []
            for track in release.tracklist:
                self.tracks_on_album.append(f"{track.position}: {track.title}")

            styles_on_album = ''
            for style in release.styles:
                styles_on_album += style + ' '

            if image_url:
                self.all_albums_dictionary.update(
                    {f"{barcodes.index(bar) + 1}":
                        {"Album Info": {
                            "Artist Name": artist_name,
                            "Album Title": album_title,
                            "Genre": release.genres[0],
                            "Style": styles_on_album,
                            "Format": release.formats[0]['name'],
                            "Lowest Price": f"${release.marketplace_stats.lowest_price.value}",
                            "Release Year": release.year,
                            "Tracklist": self.tracks_on_album,
                            "Discogs ID": release.id,
                            "Art URL": release.images[0]["uri"]
                        }}}
                )
            else:
                self.all_albums_dictionary.update(
                    {f"{barcodes.index(bar) + 1}":
                        {"Album Info": {
                            "Artist Name": artist_name,
                            "Album Title": album_title,
                            "Genre": release.genres[0],
                            "Style": styles_on_album,
                            "Format": release.formats[0]['name'],
                            "Lowest Price": f"${release.marketplace_stats.lowest_price.value}",
                            "Release Year": release.year,
                            "Tracklist": self.tracks_on_album,
                            "Discogs ID": release.id,
                        }}}
                )

            self.album_info_dictionary.update(self.all_albums_dictionary)

            #pprint.pprint(album_info_dictionary)
        self.album_info_dictionary.update(self.all_albums_dictionary)
        #pprint.pprint(self.album_info_dictionary)

        today = datetime.today().strftime('%m_%d_%Y')
        with open(f'on_the_shelf/albums_i_have_{today}.csv', 'a', newline='') as csvfile:
            fieldnames = ['Artist Name', 'Album Name', 'Genre', 'Style', 'Format', 'Lowest Price', 'Tracklist',
                          'Art URL',
                          'Discogs ID', 'Release Year']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for album in self.album_info_dictionary:
                writer.writerow({'Artist Name': self.album_info_dictionary[album]["Album Info"]['Artist Name'],
                                 'Album Name': self.album_info_dictionary[album]["Album Info"]["Album Title"],
                                 'Genre': self.album_info_dictionary[album]["Album Info"]["Genre"],
                                 'Style': self.album_info_dictionary[album]["Album Info"]["Style"],
                                 'Format': self.album_info_dictionary[album]["Album Info"]["Format"],
                                 'Lowest Price': self.album_info_dictionary[album]["Album Info"]["Lowest Price"],
                                 'Tracklist': self.album_info_dictionary[album]["Album Info"]["Tracklist"],
                                 'Art URL': self.album_info_dictionary[album]["Album Info"]["Art URL"],
                                 'Discogs ID': self.album_info_dictionary[album]["Album Info"]["Discogs ID"],
                                 'Release Year': self.album_info_dictionary[album]["Album Info"]["Release Year"]})
#
#
# list_of_tracks = album_info_dictionary[album]["Album Info"]["Tracklist"]

# results_four = d.search(query=BARCODE, type='barcode')
# release = results_four.page(1)[0]
#
# # print(release)
# # print(f"Tracklist: {release.tracklist}")
# # print(f"Tracklist: {dir(release.tracklist)}")
#
# tracks_on_album = []
# for track in release.tracklist:
#     #print(dir(track))
#     tracks_on_album.append(f"{track.position}: {track.title}")
#     #tracks_on_album.append(track)
#
# print(tracks_on_album)
#
# # cost = release.marketplace_stats.lowest_price
# # print(dir(cost))
# cost = release.marketplace_stats.lowest_price.value
# print(cost)
