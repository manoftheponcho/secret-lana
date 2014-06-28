__author__ = 'Bernadette'

import pyglet
from TextBox import TextBox


class SceneJobSelect:

    class LightWarrior:
        images = pyglet.image.load('./resources/heroes.png')

    class Fighter(LightWarrior):
        job_name = 'FIGHTER'

        def __init__(self):
            super().__init__()
            self.image = self.images.get_region(0, 0, 16, 24)
            self.sprite = pyglet.sprite.Sprite(self.image)

        def draw(self):
            self.sprite.draw()

    class Thief(LightWarrior):
        job_name = 'THIEF'

        def __init__(self):
            super().__init__()
            self.image = self.images.get_region(16, 0, 16, 24)
            self.sprite = pyglet.sprite.Sprite(self.image)

        def draw(self):
            self.sprite.draw()

    class BlackBelt(LightWarrior):
        job_name = 'Bl.BELT'

        def __init__(self):
            super().__init__()
            self.image = self.images.get_region(32, 0, 16, 24)
            self.sprite = pyglet.sprite.Sprite(self.image)

        def draw(self):
            self.sprite.draw()

    class RedMage(LightWarrior):
        job_name = 'RedMAGE'

        def __init__(self):
            super().__init__()
            self.image = self.images.get_region(48, 0, 16, 24)
            self.sprite = pyglet.sprite.Sprite(self.image)

        def draw(self):
            self.sprite.draw()

    class WhiteMage(LightWarrior):
        job_name = 'Wh.MAGE'

        def __init__(self):
            super().__init__()
            self.image = self.images.get_region(64, 0, 16, 24)
            self.sprite = pyglet.sprite.Sprite(self.image)

        def draw(self):
            self.sprite.draw()

    class BlackMage(LightWarrior):
        job_name = 'Bl.MAGE'

        def __init__(self):
            super().__init__()
            self.image = self.images.get_region(80, 0, 16, 24)
            self.sprite = pyglet.sprite.Sprite(self.image)

        def draw(self):
            self.sprite.draw()

    def __init__(self, engine):
        self.engine = engine
        self.current_heroes = [SceneJobSelect.Fighter(),
                               SceneJobSelect.Fighter(),
                               SceneJobSelect.Fighter(),
                               SceneJobSelect.Fighter()]
        self.current_heroes[0].sprite.x, self.current_heroes[0].sprite.y = (64, 151)
        self.current_heroes[1].sprite.x, self.current_heroes[1].sprite.y = (176, 151)
        self.current_heroes[2].sprite.x, self.current_heroes[2].sprite.y = (64, 55)
        self.current_heroes[3].sprite.x, self.current_heroes[3].sprite.y = (176, 55)
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
        for hero in self.current_heroes:
            hero.draw()
        pyglet.text.Label(self.current_heroes[0].job_name, x=40, y=184, font_size=8).draw()
        pyglet.text.Label(self.current_heroes[1].job_name, x=152, y=184, font_size=8).draw()
        pyglet.text.Label(self.current_heroes[2].job_name, x=40, y=88, font_size=8).draw()
        pyglet.text.Label(self.current_heroes[3].job_name, x=152, y=88, font_size=8).draw()
        self.cursor.draw()
        return pyglet.event.EVENT_HANDLED

    def on_key_press(self, symbol, modifiers):
        def handle_arrows():
            index = 0
            if self.cursor.x == 48:
                if self.cursor.y == 159:
                    index = 0
                elif self.cursor.y == 63:
                    index = 2
            elif self.cursor.x == 160:
                if self.cursor.y == 159:
                    index = 1
                elif self.cursor.y == 63:
                    index = 3

            if isinstance(self.current_heroes[index], SceneJobSelect.Fighter):
                self.current_heroes[index] = SceneJobSelect.Thief()
            elif isinstance(self.current_heroes[index], SceneJobSelect.Thief):
                self.current_heroes[index] = SceneJobSelect.BlackBelt()
            elif isinstance(self.current_heroes[index], SceneJobSelect.BlackBelt):
                self.current_heroes[index] = SceneJobSelect.RedMage()
            elif isinstance(self.current_heroes[index], SceneJobSelect.RedMage):
                self.current_heroes[index] = SceneJobSelect.WhiteMage()
            elif isinstance(self.current_heroes[index], SceneJobSelect.WhiteMage):
                self.current_heroes[index] = SceneJobSelect.BlackMage()
            elif isinstance(self.current_heroes[index], SceneJobSelect.BlackMage):
                self.current_heroes[index] = SceneJobSelect.Fighter()
            self.current_heroes[index].sprite.x = self.cursor.x + 15
            self.current_heroes[index].sprite.y = self.cursor.y - 8

        if (symbol == pyglet.window.key.UP
                or symbol == pyglet.window.key.DOWN
                or symbol == pyglet.window.key.LEFT
                or symbol == pyglet.window.key.RIGHT):
            handle_arrows()

        elif symbol == pyglet.window.key.ENTER:
            if self.cursor.x == 48:
                self.cursor.x = 160
            elif self.cursor.y == 159:
                self.cursor.x, self.cursor.y = (48, 63)

if __name__ == "__main__":
    from Engine import Engine, View
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneJobSelect(engine))
    pyglet.app.run()