import cherrypy
from mako.template import Template
from gothonweb import gothons, sessions

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
        session.set('game', gothons.newgame())
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
        except AttributeError:
            self.newgame()
            
        if room is not None:
            return self.layout.render(self.show_room, room)
        else:
            # i.e. no savegame exists
            self.newgame()
            

    @cherrypy.expose
    def pl_action(self, action):
        if action == 'new game' or action == 'newgame':
            seeother('/newgame')            
        try:
            game = session.get('game')
            game.act(action)
            return self.gamestate()
            
        except Exception:
            # TODO: consider having this post an error of some sort
            seeother('/game')
            
            
    @cherrypy.expose
    def gamestate(self):
        game = session.get('game')
        return game.stateJSON()
        
    
    @cherrypy.expose
    def noscript_form(self, action):
        self.pl_action(action)
        seeother('/game')
            
            
    @cherrypy.expose
    def default(self):
        # TODO: make an actual 404 page
        seeother('/game')
        
        
        
if __name__ == '__main__':
    # cherrypy session syntax is weird so I factored it out
    session = sessions.session
    
    conf = "config.txt"
    cherrypy.quickstart(MainPage(), config=conf)