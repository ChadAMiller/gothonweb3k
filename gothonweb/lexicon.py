directions = {'north', 'south', 'east', 'west', 'up', 'down'}
nouns = {'player', 'bear', 'princess', 'joke', 'bomb'}
verbs = {'go', 'kill', 'eat', 'tell', 'shoot', 'dodge', 'throw', 'place', 'set',
        'get', 'take', 'open'}
stops = {'the', 'in', 'of', 'a'}

# TODO: Decide if I want the engine to lowercase everything, or just leave as-is
# but still be case-insensitive

def lex(word):
    try:
        int(word)
        return 'number', int(word)
    except ValueError:
        testword = word.lower()
        if testword in directions: return 'direction', word
        if testword in nouns: return 'noun', word
        if testword in verbs: return 'verb', word
        if testword in stops: return 'stop', word
        return 'error', word
        

def scan(string):
    words = string.split()
    result = []
    for word in words:
        result.append(lex(word))
        
    return result
