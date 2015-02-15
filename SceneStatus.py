__author__ = 'DUDE'

import pyglet
from TextBox import TextBox


class SceneStatus:
    def __init__(self, engine, index):
        self.engine = engine
        next_level = [z for z in self.engine.heroes[index].exp_levels if z > self.engine.heroes[index].exp][0]
        self.fixed = pyglet.graphics.Batch()
        self.bg = pyglet.graphics.OrderedGroup(0)
        self.text = pyglet.graphics.OrderedGroup(1)
        self.objects = [TextBox(112,104,  8,  8, batch=self.fixed, group=self.bg),
                        TextBox(112,104,120,  8, batch=self.fixed, group=self.bg),
                        TextBox(184, 56, 32,120, batch=self.fixed, group=self.bg),
                        TextBox( 64, 40,  8,176, batch=self.fixed, group=self.bg),
                        TextBox(112, 40, 72,176, batch=self.fixed, group=self.bg),
                        TextBox( 64, 40,184,176, batch=self.fixed, group=self.bg),
                        pyglet.text.Label('STR.', x=24, y=88, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(self.engine.heroes[index].strength),
                                          x=88, y=88, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('AGL.', x=24, y=72, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(self.engine.heroes[index].agility),
                                          x=88, y=72, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('INT.', x=24, y=56, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(self.engine.heroes[index].intelligence),
                                          x=88, y=56, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('VIT.', x=24, y=40, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(self.engine.heroes[index].vitality),
                                          x=88, y=40, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('LUCK', x=24, y=24, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(self.engine.heroes[index].luck),
                                          x=88, y=24, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('DAMAGE', x=136, y=88, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(self.engine.heroes[index].attack),
                                          x=200, y=88, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('HIT %', x=136, y=72, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(self.engine.heroes[index].accuracy),
                                          x=200, y=72, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('ABSORB', x=136, y=56, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(self.engine.heroes[index].defense),
                                          x=200, y=56, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('EVADE %', x=136, y=40, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:3}'.format(self.engine.heroes[index].evasion),
                                          x=200, y=40, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('EXP.POINTS', x=48, y=152, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:6}'.format(self.engine.heroes[index].exp),
                                          x=160, y=152, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('FOR LEV UP', x=48, y=136, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('{:6}'.format(next_level - self.engine.heroes[index].exp),
                                          x=160, y=136, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label(self.engine.heroes[index].name,
                                          x=16, y=192, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label(self.engine.heroes[index].job_name,
                                          x=120, y=192, font_size=8, batch=self.fixed, group=self.text),
                        pyglet.text.Label('LEV{:3}'.format(self.engine.heroes[index].level),
                                          x=200, y=192, font_size=8, batch=self.fixed, group=self.text)]
        self.hero_sprite = pyglet.sprite.Sprite(self.engine.heroes[index].image,
                                                x=88, y=184, batch=self.fixed, group=self.text)
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.on_key_press)

    def on_draw(self):
        self.engine.window.clear()
        self.fixed.draw()
        return pyglet.event.EVENT_HANDLED # so the default (blank) drawing doesn't take over

    def on_key_press(self, symbol, modifiers):
        self.engine.scenes.pop()
        self.engine.pop_handlers()
        if symbol != pyglet.window.key.ESCAPE:  # the only keyboard event we want propagating up the stack
            return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    from Engine import Engine, View
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneStatus(engine, 0))
    pyglet.app.run()
