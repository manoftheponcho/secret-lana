__author__ = 'Bernadette'

import pyglet


class Engine:
    def __init__(self, window):
        self.window = window
        self.scenes = []

    def push_handlers(self, *args, **kwargs):
        self.window.push_handlers(*args, **kwargs)

    def pop_handlers(self):
        self.window.pop_handlers()


class View(pyglet.window.Window):
    def __init__(self):
        super().__init__(256, 240)

    def on_draw(self):
        self.clear()


class SceneIntro:

    class FadeInLabel(pyglet.text.Label):

        def __init__(
                self, text='', font_name=None, font_size=8,
                bold=False, italic=False, color=(255, 255, 255, 255),
                x=0, y=0, width=None, height=None,
                anchor_x='left', anchor_y='baseline', halign='left',
                multiline=False, dpi=None, batch=None, group=None, delay=0):
            self.final_color = color
            super().__init__(text, font_name, font_size, bold, italic, color,
                             x, y, width, height, anchor_x, anchor_y, halign,
                             multiline, dpi, batch, group)
            #everything starts out invisible
            self.scale_alpha(0, 0)
            #then fades in over the course of a second after (delay) seconds
#            pyglet.clock.schedule_once(self.scale_alpha, delay, scale=0)
            pyglet.clock.schedule_once(self.scale_alpha, delay + .25, scale=.25)
            pyglet.clock.schedule_once(self.scale_alpha, delay + .5, scale=.5)
            pyglet.clock.schedule_once(self.scale_alpha, delay + .75, scale=.75)
            pyglet.clock.schedule_once(self.scale_alpha, delay + 1, scale=1)

        def scale_alpha(self, dt, scale):
            self.color = (self.final_color[0], self.final_color[1],
                          self.final_color[2], int(self.final_color[3]*scale))

    def __init__(self, engine):
        self.engine = engine
        self.labels = [SceneIntro.FadeInLabel('The world is veiled in darkness.',
                                              x=128, anchor_x='center',
                                              y=216, anchor_y='top'),
                       SceneIntro.FadeInLabel('The wind stops,',
                                              x=128, anchor_x='center',
                                              y=200, anchor_y='top', delay=1),
                       SceneIntro.FadeInLabel('the sea is wild,',
                                              x=128, anchor_x='center',
                                              y=184, anchor_y='top', delay=2),
                       SceneIntro.FadeInLabel('and the earth begins to rot.',
                                              x=128, anchor_x='center',
                                              y=168, anchor_y='top', delay=3),
                       SceneIntro.FadeInLabel('The people wait,',
                                              x=128, anchor_x='center',
                                              y=152, anchor_y='top', delay=4),
                       SceneIntro.FadeInLabel('their only hope, a prophecy...',
                                              x=128, anchor_x='center',
                                              y=136, anchor_y='top', delay=5),
                       SceneIntro.FadeInLabel('"When the world is in darkness,',
                                              x=128, anchor_x='center',
                                              y=104, anchor_y='top', delay=7),
                       SceneIntro.FadeInLabel('Four Warriors will come..."',
                                              x=128, anchor_x='center',
                                              y=88, anchor_y='top', delay=8),
                       SceneIntro.FadeInLabel('After a long journey,',
                                              x=128, anchor_x='center',
                                              y=56, anchor_y='top', delay=9),
                       SceneIntro.FadeInLabel('four young warriors arrive,',
                                              x=128, anchor_x='center',
                                              y=40, anchor_y='top', delay=10),
                       SceneIntro.FadeInLabel('each holding an ORB.',
                                              x=128, anchor_x='center',
                                              y=24, anchor_y='top', delay=11)]
        self.engine.push_handlers(on_draw=self.on_draw)

    def on_draw(self):
        bg = pyglet.image.SolidColorImagePattern((0, 0, 255, 255))
        bg_image = bg.create_image(self.engine.window.width,
                                   self.engine.window.height)
        bg_image.blit(0, 0)
        for label in self.labels:
            label.draw()
        return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneIntro(engine))
    pyglet.app.run()