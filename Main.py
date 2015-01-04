__author__ = 'DUDE'

import pyglet
from Engine import Engine, View
from Intro import SceneIntro
from NewGame import SceneNewGame

class SceneMain:
    def __init__(self, engine):
        self.engine = engine
        self.engine.scenes.append(SceneIntro(self.engine))

if __name__ == "__main__":
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneIntro(engine))
    def transition(symbol, modifiers):
        if symbol == pyglet.window.key.ENTER:
            engine.pop_handlers()
            engine.pop_handlers()
            engine.scenes.pop()
            engine.scenes.append(SceneNewGame(engine))
            engine.push_handlers(on_key_press=transition)
    engine.push_handlers(on_key_press=transition)
    pyglet.app.run()