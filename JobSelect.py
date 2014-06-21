__author__ = 'Bernadette'

import pyglet
from TextBox import TextBox

class SceneJobSelect:

    class LightWarrior:
        images = pyglet.image.load('./resources/heroes.png')

    class Fighter(LightWarrior):
        job_name = 'FIGHTER'

        def __init__(self):
            super().__init__()
            self.image = super().images.get_region(0, 0, 16, 24)
            self.sprite = pyglet.sprite.Sprite(self.image)

        def draw(self):
            self.sprite.draw()

    class Thief(LightWarrior):
        job_name = 'THIEF'

        def __init__(self):
            super().__init__()
            self.image = super().images.get_region(16, 0, 16, 24)
            self.sprite = pyglet.sprite.Sprite(self.image)

        def draw(self):
            self.sprite.draw()

    def __init__(self, engine):
        self.engine = engine
        hero_image = pyglet.image.load('./resources/heroes.png')
        hero_grid = pyglet.image.ImageGrid(hero_image, 1, 6)
        hero_texs = hero_grid.get_texture_sequence()
        self.hero_sprites = [pyglet.sprite.Sprite(tex) for tex in hero_texs]
        self.current_heroes = [SceneJobSelect.Fighter(),
                               SceneJobSelect.Fighter(),
                               SceneJobSelect.Fighter(),
                               SceneJobSelect.Fighter()]
        self.current_heroes[0].sprite.x, self.current_heroes[0].sprite.y = (64, 151)
        self.current_heroes[1].sprite.x, self.current_heroes[1].sprite.y = (176, 151)
        self.current_heroes[2].sprite.x, self.current_heroes[2].sprite.y = (64, 55)
        self.current_heroes[3].sprite.x, self.current_heroes[3].sprite.y = (176, 55)
        cursor_image = pyglet.image.load('./resources/cursor.png')
        self.cursor = pyglet.sprite.Sprite(cursor_image, x=48, y=159)
        self.textboxes = [TextBox(80, 80, 32, 32),
                          TextBox(80, 80, 144, 32),
                          TextBox(80, 80, 32, 128),
                          TextBox(80, 80, 144, 128)]
        self.engine.push_handlers(on_draw=self.on_draw)

    def on_draw(self):
        self.engine.window.clear()
        for box in self.textboxes:
            box.draw()
        for hero in self.current_heroes:
            hero.draw()
        pyglet.text.Label(self.current_heroes[0].job_name, x=40, y=184, font_size=8).draw()
        pyglet.text.Label(self.current_heroes[1].job_name, x=152, y=184, font_size=8).draw()
        pyglet.text.Label(self.current_heroes[2].job_name, x=40, y=88, font_size=8).draw()
        pyglet.text.Label(self.current_heroes[3].job_name, x=152, y=88, font_size=8).draw()
        self.cursor.draw()
        return pyglet.event.EVENT_HANDLED

if __name__ == "__main__":
    from Engine import Engine, View
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneJobSelect(engine))
    pyglet.app.run()