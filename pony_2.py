import datetime
import pony.orm as pny

from pony_1 import Album, Artist

#----------------------------------------
@pny.db_session
def add_data():
    """"""

    new_artist = Artist(name=u"Newboys")
    bands = [u"MXPX", u"Kutless", u"Thousand Foot Krutch"]
    for band in bands:
        artist = Artist(name=band)

    album = Album(artist = new_artist,
                  title = u"Read All About It",
                  release_date=datetime.date(1998,12,01),
                  publisher = u"Refuge",
                  media_type=u"CD")

    albums = [

            
