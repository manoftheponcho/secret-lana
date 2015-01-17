__author__ = 'DUDE'

import pyglet
from TextBox import TextBox

class SceneStatus:
    def __init__(self, engine, index):
        self.engine = engine
        self.fixed = pyglet.graphics.Batch()
        self.bg = pyglet.graphics.OrderedGroup(0)
        self.text = pyglet.graphics.OrderedGroup(1)
        self.objects = [TextBox(112,104,  8,  8, batch=self.fixed, group=self.bg),
                        TextBox(112,104,120,  8, batch=self.fixed, group=self.bg),
                        TextBox(184, 56, 32,120, batch=self.fixed, group=self.bg),
                        TextBox( 64, 40,  8,176, batch=self.fixed, group=self.bg),
                        TextBox(112, 40, 72,176, batch=self.fixed, group=self.bg),
                        TextBox( 64, 40,184,176, batch=self.fixed, group=self.bg),
                        pyglet.text.Label('STR.', x=24, y=88, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('AGL.', x=24, y=72, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('INT.', x=24, y=56, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('VIT.', x=24, y=40, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('LUCK', x=24, y=24, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('DAMAGE', x=136, y=88, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('HIT %', x=136, y=72, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('ABSORB', x=136, y=56, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('EVADE %', x=136, y=40, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('EXP.POINTS', x=48, y=152, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('FOR LEV UP', x=48, y=136, font_size=8, batch=self.fixed, group=self.text)]
        self.labels = [pyglet.text.Label('{}'.format(index),   x=16, y=192, font_size=8)]
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.on_key_press)

    def on_draw(self):
        self.engine.window.clear()
        self.fixed.draw()
        return pyglet.event.EVENT_HANDLED # so the default (blank) drawing doesn't take over

    def on_key_press(self, symbol, modifiers):
        self.engine.scenes.pop()
        self.engine.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    from Engine import Engine, View
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneStatus(engine, 0))
    pyglet.app.run()
