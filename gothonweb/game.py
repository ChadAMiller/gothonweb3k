from gothonweb import map

class Game:
    def __init__(self):
        self.room = map.START
        
    def act(self, direction):
        self.room = self.room.go(direction)
        return self.room
        