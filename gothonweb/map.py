import json, random

class Room:
    def __init__(self, name, description, gameover=False):
        self.name = name
        self.description = description
        self.gameover = gameover
        self.paths = {'*': generic_death} if not gameover else {}
        self.hint = None
        
    def go(self, direction):
        default = self.paths['*']
        return self.paths.get(direction, default)
        
        
    def add_paths(self, paths):
        self.paths.update(paths)
        
    def json(self):
        message =   {
                    'description': self.description,
                    'name': self.name,
                    'gameover': self.gameover,
                    'hint': self.hint,
                    }
        return json.dumps(message)
        

generic_death = Room('Game Over', 'You died.', gameover=True)
        

central_corridor = Room('Central Corridor',
'''
The Gothons of Planet Percal #25 have invaded your ship and destroyed your
entire crew.  You are the last surviving member and your last mission is to get
the neutron destruct bomb from the Weapons Armory, put it in the bridge, and
blow the ship up after getting into an escape pod.

You're running down the central corridor to the Weapons Armory when a Gothon
jumps out, red scaly skin, dark grimy teeth, and evil clown costume flowing
around his hate filled body.  He's blocking the door to the Armory and about to
pull a weapon to blast you.
''')
central_corridor.hint = '"shoot", "dodge", or "tell a joke"'

corridor_shoot = Room('Wow, Already?',
'''
You try to draw your weapon but the Gothon is faster.  You collapse to the
ground while the Gothons continue their invasion.
''',
gameover=True)

corridor_dodge = Room('Wow, Already?',
'''
You're in an empty corridor; where were you dodging to?  You run into the
nearest wall, then the Gothon unceremoniously kills you.
''',
gameover=True)

laser_weapon_armory = Room('Laser Weapon Armory',
'''
Lucky for you they made you learn Gothon insults in the academy.  You tell the
one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur
ubhfr.
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head putting him
down, then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room for more
Gothons that might be hiding.  It's dead quiet, too quiet.  You stand up and run
to the far side of the room and find the neutron bomb in its container.  There's
a keypad lock on the box and you need the code to get the bomb out.  If you get
the code wrong 10 times then the lock closes forever and you can't get the bomb.
The code is 3 digits.
''')

laser_weapon_armory.bomb_code = ''.join(str(random.randint(0,9)) for i in range(3))
laser_weapon_armory.hint = 'The bomb code is {}'.format(laser_weapon_armory.bomb_code)

armory_death = Room('Game Over',
'''
You have triggered the bomb's auto-lock sequence!  The lock closes, ending all
hope for your victory today.  It is only a matter of time before you are
overwhelmed and killed.
''',
gameover=True)


the_bridge = Room('The Bridge',
'''
The container clicks open and the seal breaks, letting gas out.  You grab the
neutron bomb and run as fast as you can to the bridge where you must place it in
the right spot.

You burst onto the Bridge with the neutron destruct bomb under your arm and
surprise 5 Gothons who are trying to take control of the ship.  Each of them has
an even uglier clown costume than the last.  They haven't pulled their weapons
out yet, as they see the active bomb under your arm and don't want to set it
off.
''')
the_bridge.hint = '"throw the bomb" or "slowly place the bomb"'

bridge_death = Room('The Bridge...of Death!',
'''
The Gothons decide to damn the consequences and fire upon you.  One of them sets
off the bomb, killing you and everyone else on the ship.  You live exactly long
enough to recognize that a human victory was secured.
''',
gameover=True)


escape_pod = Room('Escape Pod',
'''
You point your blaster at the bomb under your arm and the Gothons put their
hands up and start to sweat.  You inch backward to the door, open it, and then
carefully place the bomb on the floor, pointing your blaster at it.  You then
jump back through the door, punch the close button and blast the lock so the
Gothons can't get out.  Now that the bomb is placed you run to the escape pod to
get off this tin can.

You rush through the ship desperately trying to make it to the escape pod before
the whole ship explodes.  It seems like hardly any Gothons are on the ship, so
your run is clear of interference.  You get to the chamber with the escape pods,
and now need to pick one to take.  Some of them could be damaged but you don't
have time to look.  There's 5 pods, which one do you take?
''')


escape_pod.correct_pod = str(random.randint(1,5))
escape_pod.hint = 'The correct pod is {}'.format(escape_pod.correct_pod)

the_end_winner = Room('The End',
'''
You jump into pod {} and hit the eject button.  The pod easily slides out into
space heading to the planet below.  As it flies to the planet, you look back and
see your ship implode then explode like a bright star, taking out the Gothon
ship at the same time.  You won!
'''.format(escape_pod.correct_pod),
gameover=True)


the_end_loser = Room('The End',
'''
You jump into a random pod and hit the eject button.  The pod escapes out into
the void of space, then implodes as the hull ruptures, crushing your body into
jam jelly.
''',
gameover=True)

the_bridge.add_paths({
    'throw the bomb': bridge_death,
    'slowly place the bomb': escape_pod,
    })

central_corridor.add_paths({
    'shoot': corridor_shoot,
    'dodge': corridor_dodge,
    'tell a joke': laser_weapon_armory
    })


laser_weapon_armory.add_paths({
     laser_weapon_armory.bomb_code: the_bridge,
    '*': armory_death,    
    })

escape_pod.add_paths({
    escape_pod.correct_pod: the_end_winner,
    '*': the_end_loser,
    })


START = central_corridor
