__author__ = 'Bernadette'

import pyglet
from TextBox import TextBox
from SceneMenu import SceneMenu
from Config import UP, DOWN, LEFT, RIGHT, BUTTON_A, BUTTON_B, SELECT, START


class Map:
    class Special(pyglet.sprite.Sprite):
        def __init__(self):
            super(Map.Special, self).__init__(img=pyglet.image.create(16,16))
        def can_walk(self):
            return True

    class Warp(Special):
        def __init__(self, target_map, target_x=None, target_y=None):
            super(Map.Warp, self).__init__()
            self.target_map = target_map
            self.target_x, self.target_y = (target_x, target_y)

        def on_walk(self, scene):
            scene.engine.pop_handlers()
            if self.target_x is not None:
                if self.target_y is not None:
                    scene.map = self.target_map(scene, self.target_x, self.target_y)
                else:
                    scene.map = self.target_map(scene, self.target_x)
            else:
                scene.map = self.target_map(scene)

    def __init__(self, scene, x=0, y=0):
        self.bg = None
        self.x, self.y = (x, y)
        self.scene = scene
        self.specials = {}
        self.scene.engine.push_handlers(on_draw=self.on_draw,
                                        on_key_press=self.on_key_press)

    def can_walk(self, x, y):
        if (x, y) in self.specials:
            return self.specials[(x, y)].can_walk()
        else:
            return True

    def on_draw(self):
        self.scene.engine.window.clear()
        self.bg.blit(self.x, self.y)
        hero_sprite = self.scene.engine.heroes[0].map_sprite
        hero_sprite.x, hero_sprite.y = (112, 123)
        hero_sprite.draw()
        return pyglet.event.EVENT_HANDLED  # so the default (blank) drawing doesn't take over

    def on_walk(self):
        if (self.x, self.y) in self.specials:
            self.specials[(self.x, self.y)].on_walk(self.scene)

    def on_talk(self):
        pass

    def on_key_press(self, symbol, modifiers):
        dx, dy = (0, 0)
        if symbol in LEFT:
            dx = 16
        elif symbol in RIGHT:
            dx = -16
        if symbol in UP:
            dy = -16
        elif symbol in DOWN:
            dy = 16
        if self.can_walk(self.x + dx, self.y + dy) and (dx, dy) != (0, 0):
            self.x, self.y = self.x + dx, self.y + dy
            self.on_walk()
        if symbol in BUTTON_A:
            self.on_talk()
        if symbol in START:
            self.scene.engine.scenes.append(SceneMenu(self.scene.engine))
        if symbol != pyglet.window.key.ESCAPE:
            return pyglet.event.EVENT_HANDLED


class ConeriaCastle1(Map):

    def __init__(self, scene, x=-224, y=-16):
        super(ConeriaCastle1, self).__init__(scene, x, y)
        self.bg = pyglet.image.load('./resources/coneria.png')
        self.specials = {(-224, 0): Map.Warp(WorldMap, -2336, -1400),
                         (-224, -512): Map.Warp(WorldMap, -2336, -1400)}

    def on_talk(self):
        def show_talkbox():
            self.on_draw()
            TextBox(224, 88, 16, 144).draw()
            return pyglet.event.EVENT_HANDLED

        def grab_input(symbol, modifiers):
            self.scene.engine.pop_handlers()
            if symbol != pyglet.window.key.ESCAPE:
                return pyglet.event.EVENT_HANDLED

        self.scene.engine.push_handlers(on_draw=show_talkbox,
                                        on_key_press=grab_input)

class WorldMap(Map):

    def __init__(self, scene, x=-2336, y=-1304):
        super(WorldMap, self).__init__(scene, x, y)
        self.bg = pyglet.image.load('./resources/overworld.png')
        self.specials = {(-2336, -1400): Map.Warp(ConeriaCastle1)}


class SceneMap:
    def __init__(self, engine):
        self.engine = engine
        self.map = WorldMap(self)

if __name__ == "__main__":
    from Engine import View, Engine
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneMap(engine))
    pyglet.app.run()