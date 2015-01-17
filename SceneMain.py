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
        self.engine.push_handlers(on_draw=self.on_draw)
        self.engine.scenes.append(self.scene_order.pop(0)(self.engine))

    def on_draw(self):
        if len(self.scene_order) > 0:
            self.engine.scenes.append(self.scene_order.pop(0)(self.engine))

if __name__ == "__main__":
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneMain(engine))
    pyglet.app.run()