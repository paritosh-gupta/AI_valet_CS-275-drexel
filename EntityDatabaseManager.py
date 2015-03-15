__author__ = 'paritosh'

from google.appengine.ext import ndb

DATABASE_NAME="entity"

def command_key(entity_name=DATABASE_NAME):
    """Constructs a Datastore key for a Guestbook entity.

    """
    return ndb.Key('EntityList', entity_name)#guestbook is  CommandList


class Entry(ndb.Model):
    command = ndb.StringProperty()
    action = ndb.StringProperty(indexed=False)
    parameters = ndb.StringProperty(indexed=False)
    description = ndb.StringProperty(indexed=False)

class Database():

    def insert(self,command,action,parameters,description):
        # command_name = self.request.get('CommandList',DATABASE_NAME)
        if(self.search(command)!="NULL"):
            print "here"
            return
        else:
            print "not here"

        entry = Entry(parent=command_key(DATABASE_NAME))
        entry.command=command
        entry.action=action

        if(len(parameters)!=0 and parameters[len(parameters)-1]!=";" ):
            parameters+=";"
        entry.parameters=parameters

        entry.description=description
        entry.put()

    def search(self,query):

        command_search= Entry.query(ancestor=command_key(DATABASE_NAME))
        commands = command_search.fetch(100)

        for element in commands:
            if( element.command.lower() ==  query.lower()):
                return element
            else:
                return "NULL"

        return "NULL"

