__author__ = 'Bernadette'

import pyglet


class Engine:
    def __init__(self, window):
        self.respond_rate = 1
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

if __name__ == "__main__":
    view = View()
    engine = Engine(view)
    pyglet.app.run()