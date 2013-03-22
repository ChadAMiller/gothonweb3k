import cherrypy

class Session:
    '''Wrapper I made because I don't like cherrypy's session syntax'''
    def __init__(self):
        pass
        
    def set(self, name, value):
        cherrypy.session[name] = value
        
    def get(self, name, default=None):
        return cherrypy.session.get(name, default)

        
session = Session()