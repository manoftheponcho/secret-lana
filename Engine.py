__author__ = 'Bernadette'

import pyglet


class LightWarrior:
    images = pyglet.image.load('./resources/heroes.png')

    def __init__(self):
        self.name = ''
        self.level = 1


class Fighter(LightWarrior):
    job_name = 'FIGHTER'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 35
        self.image = self.images.get_region(0, 0, 16, 24)
        self.sprite = pyglet.sprite.Sprite(self.image)

    def draw(self):
        self.sprite.draw()


class Thief(LightWarrior):
    job_name = 'THIEF'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 30
        self.image = self.images.get_region(16, 0, 16, 24)
        self.sprite = pyglet.sprite.Sprite(self.image)

    def draw(self):
        self.sprite.draw()


class BlackBelt(LightWarrior):
    job_name = 'Bl.BELT'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 33
        self.image = self.images.get_region(32, 0, 16, 24)
        self.sprite = pyglet.sprite.Sprite(self.image)

    def draw(self):
        self.sprite.draw()


class RedMage(LightWarrior):
    job_name = 'RedMAGE'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 30
        self.image = self.images.get_region(48, 0, 16, 24)
        self.sprite = pyglet.sprite.Sprite(self.image)

    def draw(self):
        self.sprite.draw()


class WhiteMage(LightWarrior):
    job_name = 'Wh.MAGE'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 28
        self.image = self.images.get_region(64, 0, 16, 24)
        self.sprite = pyglet.sprite.Sprite(self.image)

    def draw(self):
        self.sprite.draw()


class BlackMage(LightWarrior):
    job_name = 'Bl.MAGE'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 25
        self.image = self.images.get_region(80, 0, 16, 24)
        self.sprite = pyglet.sprite.Sprite(self.image)

    def draw(self):
        self.sprite.draw()


class Engine:

    def __init__(self, window):
        self.window = window
        self.scenes = []
        self.respond_rate = 1
        self.heroes = [Fighter(), Thief(), BlackBelt(), RedMage()]
        self.gold = 400

    def push_handlers(self, *args, **kwargs):
        self.window.push_handlers(*args, **kwargs)

    def pop_handlers(self):
        self.window.pop_handlers()


class View(pyglet.window.Window):
    def __init__(self):
        super().__init__(256, 240)

    def on_draw(self):
        self.clear()

if __name__ == "__main__":
    view = View()
    engine = Engine(view)
    pyglet.app.run()