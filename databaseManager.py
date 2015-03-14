__author__ = 'paritosh'

from google.appengine.ext import ndb
import cgi
import urllib

DATABASE_NAME="Commands"

# def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
#     """Constructs a Datastore key for a Guestbook entity.
#
#     We use guestbook_name as the key.
#     """
#     return ndb.Key('Guestbook', guestbook_name)

class Entry(ndb.model):
    value = ndb.StringProperty()
    command = ndb.StringProperty(indexed=False)
    Description = ndb.StringProperty(indexed=False)

class Database():

    def __init__(self):
        temp="true";
    #
    # def put(key,value):
    #     entry = Entry(parent=guestbook_key(guestbook_name))
    # # def getCommand(value):


