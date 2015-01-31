__author__ = 'DUDE'

import pyglet
from TextBox import TextBox, BLACK
from Engine import Engine, View

class SceneBattle:
    def __init__(self, engine, formation):
        self.engine = engine
        self.fixed = pyglet.graphics.Batch()
        self.layer_1 = pyglet.graphics.OrderedGroup(0)
        self.layer_2 = pyglet.graphics.OrderedGroup(1)
        self.layer_3 = pyglet.graphics.OrderedGroup(2)
        self.layer_4 = pyglet.graphics.OrderedGroup(3)
        self.text = pyglet.graphics.OrderedGroup(4)
        self.objects = [TextBox(128, 144,   8,  88, BLACK, self.fixed, self.layer_1),
                        TextBox( 64, 144, 136,  88, BLACK, self.fixed, self.layer_1),
                        TextBox( 48,  56, 200,  16, BLACK, self.fixed, self.layer_1),
                        TextBox( 88,  80,   8,  16, BLACK, self.fixed, self.layer_2),
                        TextBox(104,  80,  96,  16, BLACK, self.fixed, self.layer_2),
                        TextBox( 48,  56, 200,  64, BLACK, self.fixed, self.layer_2),
                        TextBox( 48,  56, 200, 112, BLACK, self.fixed, self.layer_3),
                        TextBox( 48,  56, 200, 160, BLACK, self.fixed, self.layer_4),
                        pyglet.text.Label('HP', x=208,  y=32, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('HP', x=208,  y=80, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('HP', x=208, y=128, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('HP', x=208, y=176, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label(self.engine.heroes[3].name,
                                          x=208,  y=48, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label(self.engine.heroes[2].name,
                                          x=208,  y=96, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label(self.engine.heroes[1].name,
                                          x=208, y=144, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label(self.engine.heroes[0].name,
                                          x=208, y=192, font_size=8, batch=self.fixed, group=self.text)]
        self.engine.push_handlers(on_draw=self.on_draw)

    def on_draw(self):
        self.engine.window.clear()
        self.fixed.draw()
        return pyglet.event.EVENT_HANDLED  # so the default (blank) drawing doesn't take over

    def draw_menu(self):
        pyglet.text.Label('FIGHT', x=112, y=72, font_size=8, batch=self.fixed, group=self.text),
        pyglet.text.Label('MAGIC', x=112, y=56, font_size=8, batch=self.fixed, group=self.text),
        pyglet.text.Label('DRINK', x=112, y=40, font_size=8, batch=self.fixed, group=self.text),
        pyglet.text.Label('ITEM',  x=112, y=24, font_size=8, batch=self.fixed, group=self.text),
        pyglet.text.Label('RUN',   x=160, y=72, font_size=8, batch=self.fixed, group=self.text),

if __name__ == "__main__":
    view = View()
    engine = Engine(view)
    engine.heroes[3].name = 'AAAA'
    engine.scenes.append(SceneBattle(engine, None))
    pyglet.app.run()
