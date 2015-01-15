__author__ = 'Bernadette'

import pyglet


class Map:

    class Obstacle:
        def on_walk(self):
            return False

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = None
        self.tiles = {}


    def on_draw(self):
        self.image.blit(self.x, self.y)

    def on_walk(self, dx=0, dy=0):
        if (self.x + dx, self.y + dy) in self.tiles:
            return self.tiles[self.x + dx, self.y + dy].on_walk()
        else:
            self.x, self.y = (self.x + dx, self.y + dy)
            return True

class World(Map):

    def __init__(self, scene):
        super().__init__(-2336, -1304)
        self.image = pyglet.image.load('./resources/overworld.png')
        self.tiles = {(-2320, -1240) : Map.Obstacle()}


class SceneMap:

    def __init__(self, engine):
        self.engine = engine
        hero_images = pyglet.image.load('./resources/mapheroes.png')
        hero_image = pyglet.image.ImageDataRegion(0, 0, 16, 16, hero_images)
        self.hero_sprite = pyglet.sprite.Sprite(hero_image)
        self.hero_sprite.x, self.hero_sprite.y = (112, 120)
        self.map = pyglet.image.load('./resources/overworld.png')
        self.x, self.y = (-2336, -1304)
        self.tiles = {}
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.on_key_press)

    def on_draw(self):
        pyglet.gl.glClear(0)
        self.engine.window.clear()
        self.map.blit(self.x, self.y)
        self.hero_sprite.draw()
        return pyglet.event.EVENT_HANDLED

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.LEFT:
            self.on_walk(16, 0)
        elif symbol == pyglet.window.key.RIGHT:
            self.on_walk(-16, 0)
        if symbol == pyglet.window.key.UP:
            self.on_walk(0, -16)
        elif symbol == pyglet.window.key.DOWN:
            self.on_walk(0, 16)

    def on_walk(self, dx, dy):
        if (self.x + dx, self.y + dy) in self.tiles:
            self.tiles[self.x + dx, self.y + dy].on_walk()
        else:
            self.x, self.y = self.x + dx, self.y + dy

if __name__ == "__main__":
    from Engine import View, Engine
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneMap(engine))
    pyglet.app.run()