__author__ = 'DUDE'

import pyglet
from TextBox import TextBox

class SceneStatus:
    def __init__(self, engine, index):
        self.engine = engine
        cursor_image = pyglet.image.load('./resources/cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=16, y=79)
        self.textboxes = [TextBox(112,104,  8,  8),
                          TextBox(112,104,120,  8),
                          TextBox(184, 56, 32,120),
                          TextBox( 64, 40,  8,176),
                          TextBox(112, 40, 72,176),
                          TextBox( 64, 40,184,176)]
        self.labels = [pyglet.text.Label('{}'.format(index),   x=16, y=192, font_size=8)]
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
            return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    from Engine import Engine, View
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneStatus(engine, 0))
    pyglet.app.run()
