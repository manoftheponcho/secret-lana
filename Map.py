__author__ = 'Bernadette'

import pyglet
import numpy


class Map:

    class Tile:
        tileset = pyglet.image.load('./resources/tileset.png')

    class Grass(Tile):

        def __init__(self, x, y):
            self.x, self.y = x, y
            self.image = pyglet.image.ImageDataRegion(0, 32, 16, 16, self.tileset)

        def draw(self, dx=0, dy=0):
            self.image.blit(self.x + dx, self.y + dy)

    def __init__(self, x, y, tiles):
        self.x, self.y = x, y
        self.tiles = numpy.array(tiles)

    def draw(self):
        for tile in self.tiles.flatten():
            tile.draw(self.x, self.y)

    def move(self, dx=0, dy=0):
        self.x, self.y = (self.x + dx, self.y + dy)


class SceneMap:

    def __init__(self, engine):
        self.engine = engine
        hero_images = pyglet.image.load('./resources/mapheroes.png')
        hero_image = pyglet.image.ImageDataRegion(0, 0, 16, 16, hero_images)
        self.hero_sprite = pyglet.sprite.Sprite(hero_image)
        self.map = Map(0, 0, [[Map.Grass(16 * x, 16 * y) for x in range(16)] for y in range(16)])
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.on_key_press)

    def on_draw(self):
        self.engine.window.clear()
        self.map.draw()
        self.hero_sprite.draw()
        return pyglet.event.EVENT_HANDLED

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.LEFT:
            pyglet.gl.gl.glTranslatef(16, 0, 0)
            self.hero_sprite.x -= 16
        elif symbol == pyglet.window.key.RIGHT:
            pyglet.gl.gl.glTranslatef(-16, 0, 0)
            self.hero_sprite.x += 16
        if symbol == pyglet.window.key.UP:
            pyglet.gl.gl.glTranslatef(0, -16, 0)
            self.hero_sprite.y += 16
        elif symbol == pyglet.window.key.DOWN:
            pyglet.gl.gl.glTranslatef(0, 16, 0)
            self.hero_sprite.y -= 16

if __name__ == "__main__":
    from Engine import View, Engine
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneMap(engine))
    pyglet.app.run()