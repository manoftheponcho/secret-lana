__author__ = 'DUDE'

import pyglet
from TextBox import TextBox

class SceneMagic:
    def __init__(self, engine, index):
        self.engine = engine
        cursor_image = pyglet.image.load('./resources/cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=16, y=79)
        self.textboxes = [TextBox(240,152,  8, 64),
                          TextBox( 64, 32,  8,200)]
        self.labels = [pyglet.text.Label('{}'.format(index),   x=16, y=208, font_size=8)]
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.on_key_press)

    def on_draw(self):
        self.engine.window.clear()
        for box in self.textboxes:
            box.draw()
        for label in self.labels:
            label.draw()
        return pyglet.event.EVENT_HANDLED

    def on_key_press(self, symbol, modifiers):
        self.engine.scenes.pop()
        self.engine.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:
            return pyglet.event.EVENT_HANDLED  # the only keyboard event we want propagating up the stack

if __name__ == "__main__":
    from Engine import Engine, View
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneMagic(engine, 0))
    pyglet.app.run()
