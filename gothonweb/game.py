import json


class Game:
    def __init__(self, start, title, instructions):
        self.room = start
        # TODO: Implement correctly
        # self.name = title
        self.gametext = instructions
        self.name = start.name
        self.gametext += '-'*10 + '\n'
        self.gametext += start.description
        self.hint = start.hint
        self.gameover = start.gameover
        
    
    def act(self, direction):
        if self.gameover:
            self.gametext += 'The game is over.  Restart the game to try again.\n'
            return
        self.room = self.room.go(direction)
        self.gametext += (
'''> {}

{}

{}
'''.format(direction, self.room.name, self.room.description))
        self.hint = self.room.hint
        self.gameover = self.room.gameover
        self.name = self.room.name
        
        
    def stateJSON(self):
        outtext = self.gametext if self.gametext else self.room.description
        self.gametext = ''
        return json.dumps({'gametext': outtext,
                            'name': self.name,
                            'hint': self.hint,
                            'gameover': self.gameover,
                            })
                            
  
class Room:
    def __init__(self, name, description, gameover=False):
        self.name = name
        self.description = description
        self.gameover = gameover
        # generic_death is a Room.  Watch for infinite recursion if redefining things.
        self.paths = {} if gameover else {'*': generic_death}
        self.hint = None
        
    def go(self, direction):
        default = self.paths['*']
        return self.paths.get(direction, default)
        
        
    def add_paths(self, paths):
        self.paths.update(paths)
        

generic_death = Room('Game Over', 'You died.', gameover=True)