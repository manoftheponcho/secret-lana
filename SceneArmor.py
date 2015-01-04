__author__ = 'DUDE'

import pyglet
from TextBox import TextBox

class SceneArmor:
    def __init__(self, engine):
        self.engine = engine
        cursor_image = pyglet.image.load('./resources/cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=16, y=79)
        self.textboxes = [TextBox(184, 48, 64,  8),
                          TextBox(184, 48, 64, 56),
                          TextBox(184, 48, 64,104),
                          TextBox(184, 48, 64,152),
                          TextBox(184, 32, 64,200),
                          TextBox( 64, 32,  8, 24),
                          TextBox( 64, 32,  8, 72),
                          TextBox( 64, 32,  8,120),
                          TextBox( 64, 32,  8,168),
                          TextBox( 56, 32,  8,200)]
        self.labels = [pyglet.text.Label('ARMOR',   x=16, y=208, font_size=8),
                       pyglet.text.Label('EQUIP', x=88, y=208, font_size=8),
                       pyglet.text.Label('TRADE', x=144, y=208, font_size=8),
                       pyglet.text.Label('DROP', x=200, y=208, font_size=8)]
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
    engine.scenes.append(SceneArmor(engine))
    pyglet.app.run()