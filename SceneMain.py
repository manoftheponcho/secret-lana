__author__ = 'DUDE'

import pyglet

from Engine import Engine, View
from SceneIntro import SceneIntro
from SceneNewGame import SceneNewGame
from SceneJobSelect import SceneJobSelect
from SceneMap import SceneMap


class SceneMain:
    def __init__(self, engine):
        self.engine = engine
        self.scene_order = [SceneIntro, SceneNewGame, SceneJobSelect, SceneMap]
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.on_key_press)

    def on_draw(self):
        if len(self.scene_order) > 0:
            self.engine.scenes.append(self.scene_order.pop(0)(self.engine))
            self.engine.window.flip()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            print(self.engine.scenes)

if __name__ == "__main__":
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneMain(engine))
    pyglet.app.run()