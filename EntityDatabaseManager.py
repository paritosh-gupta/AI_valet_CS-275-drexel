__author__ = 'paritosh'

from google.appengine.ext import ndb
from CommandDatabaseManager import Command

DATABASE_NAME="entity"

def command_key(entity_name=DATABASE_NAME):
    """Constructs a Datastore key for a Guestbook entity.

    """
    return ndb.Key('EntityList', entity_name)#guestbook is  CommandList


class Entry(ndb.Model):
    value = ndb.StringProperty()
    command = ndb.StringProperty(indexed=False)
    description = ndb.StringProperty(indexed=False)

class Database():

    def insert(self,value,command,description):
        # command_name = self.request.get('CommandList',DATABASE_NAME)
        print value +command +description
        entry = Entry(parent=command_key(DATABASE_NAME))
        if Command.query(command)!="NULL":
            entry.command=command
        else:
            print "Didnt enter anything the entity databse"
            return
        entry.value=value

        entry.description=description;
        entry.put()

    def search(self,query):
        command_search= Entry.query(ancestor=command_key(DATABASE_NAME))
        commands = command_search.fetch(100)

        for element in commands:
            if( element.value.lower() ==  query.lower()):
                return element
            else:
                return "NULL"


