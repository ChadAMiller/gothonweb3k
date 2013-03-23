import os
import cherrypy
from mako.template import Template
from gothonweb import game, map, sessions

class Layout:
    # TODO: Figure out mako inheritance or consider another templating language
    def __init__(self, filename):
        self.layout = Template(filename=filename)
        
    def render(self, filename, *args):
        return self.layout.render(Template(filename=filename).render(*args))


def seeother(url):
    raise cherrypy.HTTPRedirect(url, 303)


class MainPage:
    
    def __init__(self):
        self.layout = Layout(filename='templates/layout.html')
        self.show_room = 'templates/show_room.html'
        
    @cherrypy.expose
    def newgame(self):
        session.set('game', game.Game())
        seeother('/game')        
    
    @cherrypy.expose
    def index(self):
        if session.get('game') is not None:
            seeother('/game')
        else:
            self.newgame()
    
    @cherrypy.expose
    def game(self):        
        try:
            room = session.get('game').room
            return self.layout.render(self.show_room, room)
        except AttributeError:
            # i.e. no savegame exists
            self.newgame()

    @cherrypy.expose
    def pl_action(self, action):
        if action == 'new game' or action == 'newgame':
            seeother('/newgame')            
        try:
            room = session.get('game').act(action)
            return room.json()
        except Exception:
            # TODO: consider having this post an error of some sort
            seeother('/game')
            
            
    @cherrypy.expose
    def default(self):
        # TODO: make an actual 404 page
        seeother('/game')
        
        
        
if __name__ == '__main__':
    # cherrypy session syntax is weird so I factored it out
    session = sessions.session
    conf = "config.txt"
    host = 'localhost' if os.getcwd().startswith('/home/chad') else '0.0.0.0'
    cherrypy.config.update({'server.socket_host': host})
    cherrypy.quickstart(MainPage(), config=conf)