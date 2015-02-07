__author__ = 'DUDE'

import pyglet
from Config import UP, DOWN, LEFT, RIGHT, BUTTON_A, BUTTON_B, SELECT, START
from TextBox import TextBox
from SceneItem import SceneItem
from SceneMagic import SceneMagic
from SceneWeapon import SceneWeapon
from SceneArmor import SceneArmor
from SceneStatus import SceneStatus

class SceneMenu:
    def __init__(self, engine):
        self.engine = engine
        self.fixed = pyglet.graphics.Batch()
        self.bg = pyglet.graphics.OrderedGroup(0)
        self.text = pyglet.graphics.OrderedGroup(1)
        cursor_image = pyglet.image.load('./resources/cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=16, y=79)
        self.engine.heroes[0].sprite.x, self.engine.heroes[0].sprite.y = (136, 191)
        self.engine.heroes[1].sprite.x, self.engine.heroes[1].sprite.y = (216, 191)
        self.engine.heroes[2].sprite.x, self.engine.heroes[2].sprite.y = (136,  79)
        self.engine.heroes[3].sprite.x, self.engine.heroes[3].sprite.y = (216,  79)
        self.objects = [TextBox( 64, 64, 16,160, batch=self.fixed, group=self.bg),
                        TextBox( 80, 40,  8,120, batch=self.fixed, group=self.bg),
                        TextBox( 64,112, 16,  8, batch=self.fixed, group=self.bg),
                        TextBox( 80,112, 88,  8, batch=self.fixed, group=self.bg),
                        TextBox( 80,112, 88,120, batch=self.fixed, group=self.bg),
                        TextBox( 80,112,168,  8, batch=self.fixed, group=self.bg),
                        TextBox( 80,112,168,120, batch=self.fixed, group=self.bg)]
        HP_FORMAT = '{:3}/{:3}'
        GOLD_FORMAT = '{:6} G'
        LEVEL_FORMAT = 'L{:2}'
        self.labels = [pyglet.text.Label(self.engine.heroes[0].name,
                                         x=96,  y=208, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(self.engine.heroes[1].name,
                                         x=176, y=208, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(self.engine.heroes[2].name,
                                         x=96,  y=96,  font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(self.engine.heroes[3].name,
                                         x=176, y=96,  font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(HP_FORMAT.format(self.engine.heroes[0].hp, self.engine.heroes[0].max_hp),
                                         x=96,  y=168, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(HP_FORMAT.format(self.engine.heroes[1].hp, self.engine.heroes[1].max_hp),
                                         x=176, y=168, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(HP_FORMAT.format(self.engine.heroes[2].hp, self.engine.heroes[2].max_hp),
                                         x=96,  y=56,  font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(HP_FORMAT.format(self.engine.heroes[3].hp, self.engine.heroes[3].max_hp),
                                         x=176, y=56,  font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(GOLD_FORMAT.format(self.engine.gold),
                                         x=16,  y=136, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(LEVEL_FORMAT.format(self.engine.heroes[0].level),
                                         x=96,  y=192, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(LEVEL_FORMAT.format(self.engine.heroes[1].level),
                                         x=176, y=192, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(LEVEL_FORMAT.format(self.engine.heroes[2].level),
                                         x=96,  y=80,  font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label(LEVEL_FORMAT.format(self.engine.heroes[3].level),
                                         x=176, y=80,  font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('ITEM',   x=32, y=88, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('MAGIC',  x=32, y=72, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('WEAPON', x=32, y=56, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('ARMOR',  x=32, y=40, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('STATUS', x=32, y=24, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('HP', x=96, y=176, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('HP', x=176, y=176, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('HP', x=96, y=64, font_size=8, batch=self.fixed, group=self.text),
                       pyglet.text.Label('HP', x=176, y=64, font_size=8, batch=self.fixed, group=self.text)]
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.menu_select)

    def on_draw(self):
        self.engine.window.clear()
        self.fixed.draw()
        for hero in self.engine.heroes:
            hero.draw()
        self.cursor.draw()
        return pyglet.event.EVENT_HANDLED # so the default (blank) drawing doesn't take over

    def menu_select(self, symbol, modifiers):
        if symbol in UP:
            self.cursor.y = 15 if self.cursor.y == 79 else self.cursor.y + 16
        elif symbol in DOWN:
            self.cursor.y = 79 if self.cursor.y == 15 else self.cursor.y - 16
        elif symbol in BUTTON_A:
            if self.cursor.y == 79:#ITEM
                self.engine.scenes.append(SceneItem(self.engine))
            elif self.cursor.y == 63:#MAGIC
                self.cursor.x, self.cursor.y = (72, 209)
                self.engine.push_handlers(on_key_press=self.magic_select)
            elif self.cursor.y == 47:#WEAPON
                self.engine.scenes.append(SceneWeapon(self.engine))
            elif self.cursor.y == 31:#ARMOR
                self.engine.scenes.append(SceneArmor(self.engine))
            elif self.cursor.y == 15:#STATUS
                self.cursor.x, self.cursor.y = (72, 209)
                self.engine.push_handlers(on_key_press=self.status_select)
        elif symbol in BUTTON_B:
            self.engine.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED

    def magic_select(self, symbol, modifiers):
        if symbol in UP + DOWN:
            #if it's one, make it the other
            self.cursor.y = {95:209, 209:95}[self.cursor.y]
        elif symbol in LEFT + RIGHT:
            #same idea
            self.cursor.x = {72:152, 152:72}[self.cursor.x]
        elif symbol in BUTTON_A:
            #map cursor location to hero array index
            index = {(72,209):0, (152,209):1, (72,95):2, (152,95):3}[(self.cursor.x, self.cursor.y)]
            self.engine.scenes.append(SceneMagic(self.engine, index))
        elif symbol in BUTTON_B:
            self.cursor.x, self.cursor.y = (16,63)
            self.engine.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED

    def status_select(self, symbol, modifiers):
        if symbol in UP + DOWN:
            #if it's one, make it the other
            self.cursor.y = {95:209, 209:95}[self.cursor.y]
        elif symbol in LEFT + RIGHT:
            #same idea
            self.cursor.x = {72:152, 152:72}[self.cursor.x]
        elif symbol in BUTTON_A:
            #map cursor location to hero array index
            index = {(72,209):0, (152,209):1, (72,95):2, (152,95):3}[(self.cursor.x, self.cursor.y)]
            self.engine.scenes.append(SceneStatus(self.engine, index))
        elif symbol in BUTTON_B:
            self.cursor.x, self.cursor.y = (16,15)
            self.engine.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED


if __name__ == "__main__":
    from Engine import Engine, View, Fighter, Thief, BlackBelt, RedMage
    view = View()
    engine = Engine(view)
    engine.heroes = [Fighter(), Thief(), BlackBelt(), RedMage()]
    engine.scenes.append(SceneMenu(engine))
    pyglet.app.run()
