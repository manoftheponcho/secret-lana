__author__ = 'Bernadette'

import pyglet

from TextBox import TextBox, BLUE
from Config import UP, DOWN, LEFT, RIGHT, BUTTON_A, BUTTON_B, SELECT, START

class SceneNewGame:
    def __init__(self, engine):
        self.engine = engine
        cursor_image = pyglet.image.load('./resources/cursor.png')
        pyglet.gl.glClearColor(0,0,0,1)
        self.move_sound = pyglet.media.load('./resources/move.wav', streaming=False)
        self.select_sound = pyglet.media.load('./resources/select.wav', streaming=False)
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=72, y=135)
        self.textboxes = [TextBox(80, 32, 88, 128),
                          TextBox(80, 32, 88, 88),
                          TextBox(128, 32, 64, 48)]
        self.block = BLUE.create_image(120, 16)
        self.labels = [pyglet.text.Label('CONTINUE', x=96, y=136, font_size=8),
                       pyglet.text.Label('NEW GAME', x=96, y=96, font_size=8),
                       pyglet.text.Label('RESPOND RATE', x=72, y=56, font_size=8),
                       pyglet.text.Label('C 1987 SQUARE', x=64, y=32, font_size=8),
                       pyglet.text.Label('C 1990 NINTENDO', x=64, y=24, font_size=8)]
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.on_key_press)

    def on_draw(self):
        self.engine.window.clear()
        self.block.blit(64, 24, 0)
        for box in self.textboxes:
            box.draw()
        for label in self.labels:
            label.draw()
        self.cursor.draw()
        rr = self.engine.respond_rate
        pyglet.text.Label('{}'.format(rr), x=176, y=56, font_size=8).draw()
        return pyglet.event.EVENT_HANDLED # so the default (blank) drawing doesn't take over

    def on_key_press(self, symbol, modifiers):
        if symbol in UP or symbol in DOWN:
            self.select_sound.play()
            self.cursor.y = 135 if self.cursor.y == 95 else 95
        elif symbol in LEFT:
            self.move_sound.play()
            self.engine.respond_rate = 8 if self.engine.respond_rate == 1 else self.engine.respond_rate - 1
        elif symbol in RIGHT:
            self.move_sound.play()
            self.engine.respond_rate = 1 if self.engine.respond_rate == 8 else self.engine.respond_rate + 1
        elif symbol in BUTTON_A:
            self.engine.scenes.pop()
            self.engine.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED


if __name__ == "__main__":
    from Engine import Engine, View
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneNewGame(engine))
    pyglet.app.run()
