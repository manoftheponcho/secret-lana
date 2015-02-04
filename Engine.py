__author__ = 'Bernadette'

import pyglet
import random


class LightWarrior:
    images = pyglet.image.load('./resources/heroes.png')
    map_sprites = pyglet.image.load('./resources/mapheroes.png')

    def __init__(self):
        self.name = ''
        self.level = 1
        self.status = set()
        self.weapons = []
        self.armor = []

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
    def defense(self):
        return sum([z.absorb for z in self.armor], 0)
    @property
    def evasion(self):
        return 48 + self.agility - sum([z.weight for z in self.armor], 0)

    def fight(self, target):
        if self.incapacitated:
            return
        damage = 0
        attack = sum([z.attack for z in self.weapons], int(self.strength / 2))
        hit_chance = sum([z.accuracy for z in self.weapons], 168 + self.accuracy - target.evasion)
        hits = int(1 + sum([z.accuracy for z in self.weapons], self.accuracy) / 32)
        for i in range(hits):
            if random.randint(0, 201) <= hit_chance:
                hit_damage = random.randint(attack, 2 * attack + 1) - target.defense
                damage += max(hit_damage, 1)
        target.hp -= damage

class Fighter(LightWarrior):
    job_name = 'FIGHTER'

    def __init__(self):
        super().__init__()
        self.max_hp = self.hp = 35
        self.strength = 20
        self.agility = 5
        self.intelligence = 1
        self.vitality = 10
        self.luck = 5
        self.accuracy = 10
        self.mdefense = 15
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
        self.strength = 5
        self.agility = 10
        self.intelligence = 5
        self.vitality = 5
        self.luck = 15
        self.accuracy = 5
        self.mdefense = 15
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
        self.strength = 5
        self.agility = 5
        self.intelligence = 5
        self.vitality = 20
        self.luck = 5
        self.accuracy = 5
        self.mdefense = 10
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
        self.strength = 10
        self.agility = 10
        self.intelligence = 10
        self.vitality = 5
        self.luck = 5
        self.accuracy = 7
        self.mdefense = 20
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
        self.strength = 5
        self.agility = 5
        self.intelligence = 15
        self.vitality = 10
        self.luck = 5
        self.accuracy = 5
        self.mdefense = 20
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
        self.strength = 1
        self.agility = 10
        self.intelligence = 20
        self.vitality = 1
        self.luck = 10
        self.accuracy = 5
        self.mdefense = 20
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