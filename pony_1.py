import datetime
import pony.orm as pny

database = pny.Database("sqlite", "music.sqlite", create_db=True)

class Artist(database.Entity):
    """ Pony ORM модель для таблицы Artist """
    name = pny.Required('unicode')
    albums = pny.Set("Album")

class Album(database.Entity):
    """ Pony ORM модель для таблицы Album """
    artist = pny.Required(Artist)
    title = pny.Required('unicode')
    release_date = pny.Required(datetime.date)
    publisher = pny.Required('unicode')
    media_type = pny.Required('unicode')
