__author__ = 'DUDE'

import pyglet
from pyglet.gl import *
from SceneMenu import SceneMenu
from Config import RIGHT, UP, LEFT, DOWN, BUTTON_A, BUTTON_B, SELECT, START


class SceneMap:
    FPS = 48
    hero_sprites = pyglet.image.load('./resources/mapheroes.png')

    class Wall(pyglet.sprite.Sprite):
        def __init__(self, start_x, start_y, end_x, end_y):
            super().__init__(img=pyglet.image.create(end_x-start_x, end_y-start_y,
                                                     pyglet.image.SolidColorImagePattern((255,0,255,255))))
            self.start_x, self.start_y, self.end_x, self.end_y = start_x, start_y, end_x, end_y
            self.x, self.y = start_x, start_y

        def __contains__(self, item):
            return (self.start_x <= item[0] <= self.end_x) and (self.start_y <= item[1] <= self.end_y)

    def __init__(self, engine):
        self.engine = engine
        self._x, self._y = (0, 0)
        self.moving = {LEFT: False, RIGHT: False, UP: False, DOWN: False}
        self.bg = pyglet.image.load('./resources/coneria.png')
        self.objects = [SceneMap.Wall(112, 168, 128, 632)]
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.on_key_press,
                                  on_key_release=self.on_key_release,
                                  on_mouse_press=self.on_mouse_press)

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, other):
        dx = other - self._x
        for object in self.objects:
            object.x += dx
        self._x = other

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, other):
        dy = other - self._y
        for object in self.objects:
            object.y += dy
        self._y = other

    def on_draw(self):
        self.engine.window.clear()
        self.bg.blit(self.x, self.y)
        for object in self.objects:
            object.draw()
        hero_sprite = pyglet.sprite.Sprite(SceneMap.hero_sprites.get_region(0,0,16,16))
        hero_sprite.x, hero_sprite.y = (112, 123)
        hero_sprite.draw()
        return pyglet.event.EVENT_HANDLED

    def on_key_press(self, symbol, modifiers):
        already_moving = [key for key in self.moving if self.moving[key]]  # non-empty if moving in any direction
        try:
            direction = tuple(button for button in self.moving if symbol in button)[0]  # translate key to button press
        except IndexError:
            direction = None
        if direction in self.moving and not already_moving:
            self.moving[direction] = True
            pyglet.clock.schedule_interval_soft(self.move, 1/SceneMap.FPS)
        if symbol in START:
            self.engine.scenes.append(SceneMenu(self.engine))
        if symbol != pyglet.window.key.ESCAPE:
            return pyglet.event.EVENT_HANDLED

    def on_key_release(self, symbol, modifiers):
        try:
            direction = tuple(button for button in self.moving if symbol in button)[0]  # translate key to button press
        except IndexError:
            direction = None
        if direction in self.moving:
            pyglet.clock.unschedule(self.move)
            pyglet.clock.schedule_interval_soft(self.finish_moving, 1/SceneMap.FPS)

    def on_mouse_press(self, x, y, button, modifiers):
        print('(x, y) = ({}, {})'.format(self.x, self.y))

    def move(self, dt=1/16):
        if self.moving[LEFT]:
            for object in self.objects:
                if (self.x+128, 128 - self.y) in object:  # transform to world coordinates
                    return
            self.x += 1
        elif self.moving[RIGHT]:
            for object in self.objects:
                if (self.x+112, 128 - self.y) in object:  # transform to world coordinates
                    return
            self.x -= 1
        elif self.moving[UP]:
            for object in self.objects:
                if (self.x+120, 136 - self.y) in object:  # transform to world coordinates
                    return
            self.y -= 1
        elif self.moving[DOWN]:
            for object in self.objects:
                if (self.x+120, 120 - self.y) in object:  # transform to world coordinates
                    return
            self.y += 1

    def finish_moving(self, dt=1/16):
        if (self.x % 16 != 0) or (self.y % 16 != 0):
            self.move()
        else:
            for key in self.moving:
                self.moving[key] = False
            pyglet.clock.unschedule(self.finish_moving)


if __name__ == "__main__":
    from Engine import Engine, View
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneMap(engine))
    pyglet.app.run()