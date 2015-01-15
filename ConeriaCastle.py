__author__ = 'DUDE'

import pyglet


class ConeriaCastle:

    def __init__(self, engine):
        self.map = pyglet.image.load('./resources/coneria.png')
        self.x, self.y = (-224, -16)
        self.engine = engine
        self.tiles = {(-224, -32) : self.on_walk, (-224, -16) : self.on_walk, (-224, 0) : self.on_warp}
        hero_images = pyglet.image.load('./resources/mapheroes.png')
        hero_image = pyglet.image.ImageDataRegion(0, 0, 16, 16, hero_images)
        self.hero_sprite = pyglet.sprite.Sprite(hero_image)
        self.hero_sprite.x, self.hero_sprite.y = (112, 120)
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.on_key_press)

    def on_draw(self):
        pyglet.gl.glClear(0)
        self.engine.window.clear()
        self.map.blit(self.x, self.y)
        self.hero_sprite.draw()
        return pyglet.event.EVENT_HANDLED

    def on_key_press(self, symbol, modifiers):
        dx, dy = (0, 0)
        if symbol == pyglet.window.key.LEFT:
            dx = 16
        elif symbol == pyglet.window.key.RIGHT:
            dx = -16
        if symbol == pyglet.window.key.UP:
            dy = -16
        elif symbol == pyglet.window.key.DOWN:
            dy = 16
        if (self.x + dx, self.y + dy) in self.tiles and (dx, dy) != (0, 0):
            self.tiles[(self.x + dx, self.y + dy)](dx, dy)
        if symbol != pyglet.window.key.ESCAPE:
            return pyglet.event.EVENT_HANDLED

    def on_walk(self, dx, dy):
        self.x, self.y = self.x + dx, self.y + dy

    def on_warp(self, dx, dy):
        self.engine.pop_handlers()

if __name__ == "__main__":
    from Engine import View, Engine
    view = View()
    engine = Engine(view)
    engine.scenes.append(ConeriaCastle(engine))
    pyglet.app.run()
