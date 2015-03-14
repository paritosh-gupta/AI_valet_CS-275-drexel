from google.appengine.ext import ndb

DATABASE_NAME="Commands"

def command_key(Command_name=DATABASE_NAME):
    """Constructs a Datastore key for a Guestbook Command.

    """
    return ndb.Key('CommandList', Command_name)#guestbook is  CommandList


class Command(ndb.Model):
    name = ndb.StringProperty()
    webpage = ndb.StringProperty(indexed=False)
    parameters = ndb.StringProperty(indexed=False)

class Database():

    def insert(self,name,webpage,parameters):
        print name +webpage +parameters
        entry = Command(parent=command_key(DATABASE_NAME))
        entry.name=name
        entry.webpage=webpage
        entry.parameters=parameters
        entry.put()

    def search(self,query):
        command_search= Command.query(ancestor=command_key(DATABASE_NAME))
        commands = command_search.fetch(100)

        for element in commands:
            if( element.name.lower() ==  query.lower()):
                return element
            else:
                return "NULL"

    def searchList(self,query):
        command_search= Command.query(ancestor=command_key(DATABASE_NAME))
        commands = command_search.fetch(20)
        elements=[];
        for element in commands:
            if( element.value.lower()[0] ==  query.lower()[0]):
                elements.append(query)
            else:
                return "NULL"

        return elements

