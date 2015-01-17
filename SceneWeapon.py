__author__ = 'DUDE'

import pyglet
from TextBox import TextBox

class SceneWeapon:
    def __init__(self, engine):
        self.engine = engine
        cursor_image = pyglet.image.load('./resources/cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=16, y=79)
        self.fixed = pyglet.graphics.Batch()
        bg = pyglet.graphics.OrderedGroup(0)
        fg = pyglet.graphics.OrderedGroup(1)
        text = pyglet.graphics.OrderedGroup(2)
        self.objects = [TextBox(184, 48, 64,  8, batch=self.fixed, group=bg),
                        TextBox(184, 48, 64, 56, batch=self.fixed, group=bg),
                        TextBox(184, 48, 64,104, batch=self.fixed, group=bg),
                        TextBox(184, 48, 64,152, batch=self.fixed, group=bg),
                        TextBox(184, 32, 64,200, batch=self.fixed, group=bg),
                        TextBox( 64, 32,  8, 24, batch=self.fixed, group=fg),
                        TextBox( 64, 32,  8, 72, batch=self.fixed, group=fg),
                        TextBox( 64, 32,  8,120, batch=self.fixed, group=fg),
                        TextBox( 64, 32,  8,168, batch=self.fixed, group=fg),
                        TextBox( 56, 32,  8,200, batch=self.fixed, group=fg),
                        pyglet.text.Label('WEAPON', x=16, y=208, font_size=8, batch=self.fixed, group=text),
                        pyglet.text.Label('EQUIP',  x=88, y=208, font_size=8, batch=self.fixed, group=text),
                        pyglet.text.Label('TRADE', x=144, y=208, font_size=8, batch=self.fixed, group=text),
                        pyglet.text.Label('DROP',  x=200, y=208, font_size=8, batch=self.fixed, group=text)]
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
    engine.scenes.append(SceneWeapon(engine))
    pyglet.app.run()
