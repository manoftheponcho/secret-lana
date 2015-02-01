__author__ = 'Bernadette'

import pyglet


class Battler(object):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.status = set()
        self._hp = 1

    @property
    def incapacitated(self):
        if 'Dead' in self.status or 'Stone' in self.status:
            return True
        return False

    @property
    def unconscious(self):
        if self.incapacitated or 'Stun' in self.status or 'Sleep' in self.status:
            return True
        return False

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, other):
        self._hp = other
        self._hp = max(0, self._hp)
        if self._hp == 0:
            self.status.add('Dead')

class LightWarrior:
    images = pyglet.image.load('./resources/heroes.png')
    map_sprites = pyglet.image.load('./resources/mapheroes.png')

    def __init__(self):
        self.name = ''
        self.level = 1
        self.status = set()

    @property
    def unconscious(self):
        if 'DEAD' in self.status or 'STONE' in self.status or 'STUN' in self.status or 'SLEEP' in self.status:
            return True
        return False

class Fighter(LightWarrior):
    job_name = 'FIGHTER'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 35
        self.image = self.images.get_region(0, 0, 16, 24)
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.map_sprite = pyglet.sprite.Sprite(self.map_sprites.get_region(0, 0, 16, 16))

    def draw(self):
        self.sprite.draw()


class Thief(LightWarrior):
    job_name = 'THIEF'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 30
        self.image = self.images.get_region(16, 0, 16, 24)
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.map_sprite = pyglet.sprite.Sprite(self.map_sprites.get_region(32, 0, 16, 16))

    def draw(self):
        self.sprite.draw()


class BlackBelt(LightWarrior):
    job_name = 'Bl.BELT'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 33
        self.image = self.images.get_region(32, 0, 16, 24)
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.map_sprite = pyglet.sprite.Sprite(self.map_sprites.get_region(64, 0, 16, 16))

    def draw(self):
        self.sprite.draw()


class RedMage(LightWarrior):
    job_name = 'RedMAGE'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 30
        self.image = self.images.get_region(48, 0, 16, 24)
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.map_sprite = pyglet.sprite.Sprite(self.map_sprites.get_region(96, 0, 16, 16))

    def draw(self):
        self.sprite.draw()


class WhiteMage(LightWarrior):
    job_name = 'Wh.MAGE'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 28
        self.image = self.images.get_region(64, 0, 16, 24)
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.map_sprite = pyglet.sprite.Sprite(self.map_sprites.get_region(128, 0, 16, 16))

    def draw(self):
        self.sprite.draw()


class BlackMage(LightWarrior):
    job_name = 'Bl.MAGE'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 25
        self.image = self.images.get_region(80, 0, 16, 24)
        self.sprite = pyglet.sprite.Sprite(self.image)
        self.map_sprite = pyglet.sprite.Sprite(self.map_sprites.get_region(160, 0, 16, 16))

    def draw(self):
        self.sprite.draw()


class Engine:

    def __init__(self, window):
        self.window = window
        self.scenes = []
        # TODO: push everything that defines a save into its own Game class
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