__author__ = 'DUDE'

import pyglet
from Keys import UP, DOWN, LEFT, RIGHT, BUTTON_A, BUTTON_B, SELECT, START
from TextBox import TextBox
from SceneItem import SceneItem
from SceneMagic import SceneMagic
from SceneWeapon import SceneWeapon
from SceneArmor import SceneArmor
from SceneStatus import SceneStatus

class SceneMenu:
    def __init__(self, engine):
        self.engine = engine
        cursor_image = pyglet.image.load('./resources/cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=16, y=79)
        self.textboxes = [TextBox( 64, 64, 16,160),
                          TextBox( 80, 40,  8,120),
                          TextBox( 64,112, 16,  8),
                          TextBox( 80,112, 88,  8),
                          TextBox( 80,112, 88,120),
                          TextBox( 80,112,168,  8),
                          TextBox( 80,112,168,120)]
        self.labels = [pyglet.text.Label('ITEM',   x=32, y=88, font_size=8),
                       pyglet.text.Label('MAGIC',  x=32, y=72, font_size=8),
                       pyglet.text.Label('WEAPON', x=32, y=56, font_size=8),
                       pyglet.text.Label('ARMOR',  x=32, y=40, font_size=8),
                       pyglet.text.Label('STATUS', x=32, y=24, font_size=8),
                       pyglet.text.Label('G', x=72, y=136, font_size=8),
                       pyglet.text.Label('L', x=96, y=192, font_size=8),
                       pyglet.text.Label('L', x=176, y=192, font_size=8),
                       pyglet.text.Label('L', x=96, y=80, font_size=8),
                       pyglet.text.Label('L', x=176, y=80, font_size=8),
                       pyglet.text.Label('HP', x=96, y=176, font_size=8),
                       pyglet.text.Label('HP', x=176, y=176, font_size=8),
                       pyglet.text.Label('HP', x=96, y=64, font_size=8),
                       pyglet.text.Label('HP', x=176, y=64, font_size=8)]
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.menu_select)

    def on_draw(self):
        self.engine.window.clear()
        for box in self.textboxes:
            box.draw()
        for label in self.labels:
            label.draw()
        self.cursor.draw()
        return pyglet.event.EVENT_HANDLED

    def menu_select(self, symbol, modifiers):
        if symbol == UP:
            self.cursor.y = 15 if self.cursor.y == 79 else self.cursor.y + 16
        elif symbol == DOWN:
            self.cursor.y = 79 if self.cursor.y == 15 else self.cursor.y - 16
        elif symbol == BUTTON_A:
            if self.cursor.y == 79:#ITEM
                self.engine.scenes.append(SceneItem(engine))
            elif self.cursor.y == 63:#MAGIC
                self.cursor.x, self.cursor.y = (72, 209)
                self.engine.push_handlers(on_key_press=self.magic_select)
            elif self.cursor.y == 47:#WEAPON
                self.engine.scenes.append(SceneWeapon(engine))
            elif self.cursor.y == 31:#ARMOR
                self.engine.scenes.append(SceneArmor(engine))
            elif self.cursor.y == 15:#STATUS
                self.cursor.x, self.cursor.y = (72, 209)
                self.engine.push_handlers(on_key_press=self.status_select)
        elif symbol == BUTTON_B:
            self.engine.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:
            return pyglet.event.EVENT_HANDLED

    def magic_select(self, symbol, modifiers):
        if symbol in [UP, DOWN]:
            #if it's one, make it the other
            self.cursor.y = {95:209, 209:95}[self.cursor.y]
        elif symbol in [LEFT, RIGHT]:
            #same idea
            self.cursor.x = {72:152, 152:72}[self.cursor.x]
        elif symbol == BUTTON_A:
            #map cursor location to hero array index
            index = {(72,209):0, (152,209):1, (72,95):2, (152,95):3}[(self.cursor.x, self.cursor.y)]
            self.engine.scenes.append(SceneMagic(engine, index))
        elif symbol == BUTTON_B:
            self.cursor.x, self.cursor.y = (16,63)
            self.engine.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:
            return pyglet.event.EVENT_HANDLED

    def status_select(self, symbol, modifiers):
        if symbol in [UP, DOWN]:
            #if it's one, make it the other
            self.cursor.y = {95:209, 209:95}[self.cursor.y]
        elif symbol in [LEFT, RIGHT]:
            #same idea
            self.cursor.x = {72:152, 152:72}[self.cursor.x]
        elif symbol == BUTTON_A:
            #map cursor location to hero array index
            index = {(72,209):0, (152,209):1, (72,95):2, (152,95):3}[(self.cursor.x, self.cursor.y)]
            self.engine.scenes.append(SceneStatus(engine, index))
        elif symbol == BUTTON_B:
            self.cursor.x, self.cursor.y = (16,15)
            self.engine.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:
            return pyglet.event.EVENT_HANDLED


if __name__ == "__main__":
    from Engine import Engine, View
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneMenu(engine))
    pyglet.app.run()
