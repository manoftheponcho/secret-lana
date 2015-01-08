__author__ = 'Bernadette'

import pyglet
from TextBox import TextBox
from NameSelect import SceneNameSelect
from Engine import Fighter, Thief, BlackBelt, RedMage, WhiteMage, BlackMage
from Config import UP, DOWN, LEFT, RIGHT, SELECT, START, BUTTON_A, BUTTON_B


class SceneJobSelect:

    def __init__(self, engine):
        self.engine = engine
        self.index_map = [(48, 159), (160, 159), (48, 63), (160, 63)]
        self.cycle = {Fighter:Thief, Thief:BlackBelt, BlackBelt:RedMage,
                      RedMage:WhiteMage, WhiteMage:BlackMage, BlackMage:Fighter}
        self.engine.heroes[0].sprite.x, self.engine.heroes[0].sprite.y = (64, 151)
        self.engine.heroes[1].sprite.x, self.engine.heroes[1].sprite.y = (176, 151)
        self.engine.heroes[2].sprite.x, self.engine.heroes[2].sprite.y = (64, 55)
        self.engine.heroes[3].sprite.x, self.engine.heroes[3].sprite.y = (176, 55)
        self.index = 0
        cursor_image = pyglet.image.load('./resources/cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=48, y=159)
        self.textboxes = [TextBox(80, 80, 32, 32),
                          TextBox(80, 80, 144, 32),
                          TextBox(80, 80, 32, 128),
                          TextBox(80, 80, 144, 128)]
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.on_key_press)

    def on_draw(self):
        self.engine.window.clear()
        for box in self.textboxes:
            box.draw()
        for hero in self.engine.heroes:
            hero.draw()
        pyglet.text.Label(self.engine.heroes[0].job_name, x=40, y=184, font_size=8).draw()
        pyglet.text.Label(self.engine.heroes[1].job_name, x=152, y=184, font_size=8).draw()
        pyglet.text.Label(self.engine.heroes[2].job_name, x=40, y=88, font_size=8).draw()
        pyglet.text.Label(self.engine.heroes[3].job_name, x=152, y=88, font_size=8).draw()
        self.cursor.x, self.cursor.y = self.index_map[self.index]
        self.cursor.draw()
        return pyglet.event.EVENT_HANDLED

    def on_key_press(self, symbol, modifiers):
        if symbol in [UP, DOWN, LEFT, RIGHT]:
            self.engine.heroes[self.index] = self.cycle[type(self.engine.heroes[self.index])]()
            self.engine.heroes[self.index].sprite.x = self.cursor.x + 15
            self.engine.heroes[self.index].sprite.y = self.cursor.y - 8
        elif symbol == BUTTON_A:
            self.index += 1
            self.engine.scenes.append(SceneNameSelect(self.engine, self.index-1))
        if symbol != pyglet.window.key.ESCAPE:
            return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    from Engine import Engine, View
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneJobSelect(engine))
    pyglet.app.run()