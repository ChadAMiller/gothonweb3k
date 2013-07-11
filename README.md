# gothonweb3k

This is an implementation of the final chapter of Zed Shaw's "Learn Python the Hard Way". It's not only mostly finished because I remembered I don't actually like text adventure games.

I didn't like web.py. As a result, I ended up trying other frameworks, then decided to write the thing in Python 3 instead of Python 2. Then it turns out that I wrote bilingual code; I've tested the codebase on 2.7 and 3.2 with no problems.

The site runs on CherryPy with Mako templates, and uses Javascript+Bootstrap for the UI. I also tried to make it work without JavaScript (this is probably where the weirdest parts of the program flow come from)

At some point the idea creeped into my head that Colossal Cave and similar games would have been improved by a decent hint system. You can see the beginnings of this in my project; the idea was that those Bootstrap alerts would be a lot less frequent, and just lead the player toward correct solutions without giving the answer away.

The parser is ported and has some unit tests but isn't actually implemented. That's the next thing I would work on if I felt like continuing this later.

I didn't set up nose, instead opting to use the builtin unittest module.

I have a [working demo](http://sleepy-meadow-1529.herokuapp.com/) running on Heroku. I left my tools in the repository for if you want to try the same (as it's pretty easy to get a free dyno running)

### Usage

`python app.py` from top level

Browse to localhost:5000 to test.

`python -m unittest` for tests

### Python Dependencies

*   CherryPy
*   Mako

### Files you can delete if you don't use Heroku

*   Procfile
*   requirements.txt

