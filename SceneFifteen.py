__author__ = 'root'

import random, copy
import pyglet
from Config import UP, DOWN, LEFT, RIGHT, BUTTON_A, BUTTON_B

class SceneFifteen:
    screen_map = [
        (72, 176), (88, 176), (104, 176), (120, 176),
        (72, 160), (88, 160), (104, 160), (120, 160),
        (72, 144), (88, 144), (104, 144), (120, 144),
        (72, 128), (88, 128), (104, 128), (120, 128)]
    bright_map = [None,
        (0, 48, 16, 16), (16, 48, 16, 16), (32, 48, 16, 16), (48, 48, 16, 16),
        (0, 32, 16, 16), (16, 32, 16, 16), (32, 32, 16, 16), (48, 32, 16, 16),
        (0, 16, 16, 16), (16, 16, 16, 16), (32, 16, 16, 16), (48, 16, 16, 16),
        (0,  0, 16, 16), (16,  0, 16, 16), (32,  0, 16, 16), (48,  0, 16, 16)]
    dim_map = [None,
        (64, 48, 16, 16), (80, 48, 16, 16), (96, 48, 16, 16), (112, 48, 16, 16),
        (64, 32, 16, 16), (80, 32, 16, 16), (96, 32, 16, 16), (112, 32, 16, 16),
        (64, 16, 16, 16), (80, 16, 16, 16), (96, 16, 16, 16), (112, 16, 16, 16),
        (64,  0, 16, 16), (80,  0, 16, 16), (96,  0, 16, 16), (112,  0, 16, 16)]
    mid_map = [None,
        (128, 48, 16, 16), (144, 48, 16, 16), (160, 48, 16, 16), (176, 48, 16, 16),
        (128, 32, 16, 16), (144, 32, 16, 16), (160, 32, 16, 16), (176, 32, 16, 16),
        (128, 16, 16, 16), (144, 16, 16, 16), (160, 16, 16, 16), (176, 16, 16, 16),
        (128,  0, 16, 16), (144,  0, 16, 16), (160,  0, 16, 16), (176,  0, 16, 16)]

    class Puzzle:
        solved = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

        def __init__(self):
            self.state = copy.deepcopy(self.solved)
            random.shuffle(self.state)
            while self.parity():
                random.shuffle(self.state)

        def parity(self):  # shame on me for o(n²)
            inversions = 0
            blank_index = self.state.index(16)
            puzzle_order = copy.deepcopy(self.state)
            row, column = blank_index // 4, blank_index % 4
            if column != 3:
                selected_index = row * 4 + 3  # move the blank to the end of the row
                rotated_row = puzzle_order[blank_index + 1:selected_index + 1] + [16]
                puzzle_order[blank_index:selected_index + 1] = rotated_row
                blank_index = puzzle_order.index(16)
            if row != 3:
                selected_index = 15  # then to the bottom of the column
                rotated_column = puzzle_order[blank_index + 4:selected_index + 4:4] + [16]
                puzzle_order[blank_index:selected_index + 1:4] = rotated_column
            for i in puzzle_order:
                for j in puzzle_order[puzzle_order.index(i):]:
                    if i > j:
                        inversions += 1
            return inversions % 2

    def __init__(self, engine):
        self.engine = engine
        self.puzzle = SceneFifteen.Puzzle()
        self.frames = 0
        self.image_map = self.bright_map
        self.selected_index = 0 if self.puzzle.state[0] != 16 else 1
        self.show_selected = True
        self.puzzle_image = pyglet.image.load('./resources/fifteen.png')
        self.puzzle_bg = pyglet.image.load('./resources/fifteenbg.png')
        self.music_player = pyglet.media.Player()
        self.puzzle_music = pyglet.media.load('./resources/prologue.wav')
        self.music_group = pyglet.media.SourceGroup(self.puzzle_music.audio_format, None)
        self.music_group.queue(self.puzzle_music)
        self.music_group.loop = True
        self.music_player.queue(self.music_group)
        self.music_player.play()
        pyglet.clock.schedule_interval(self.flicker, 1/24)
        self.engine.push_handlers(on_draw=self.on_draw,
                                  on_key_press=self.on_key_press)

    def flicker(self, dt):
        self.show_selected = not self.show_selected
    def glow(self, dt):
        self.frames += 1
        if self.frames % 4 == 0:
            self.image_map = self.dim_map
        elif self.frames % 4 == 1:
            self.image_map = self.mid_map
        else:
            self.image_map = self.bright_map

    def on_draw(self):
        self.engine.window.clear()
        self.puzzle_bg.blit(0, 0)
        for i in range(len(self.puzzle.state)):
            img = self.puzzle_image.get_region(*self.image_map[self.puzzle.state[i]])
            img.blit(*self.screen_map[i])
        if not self.show_selected:
            img = self.puzzle_image.get_region(*self.image_map[16])
            img.blit(*self.screen_map[self.selected_index])
        return pyglet.event.EVENT_HANDLED

    def on_key_press(self, symbol, modifiers):
        # for all of the directional buttons, if we move onto the blank we just move again to fix it
        if symbol in LEFT:
            self.selected_index -= 1
            self.selected_index %= 16
            if self.puzzle.state[self.selected_index] == 16:
                self.selected_index -= 1
                self.selected_index %= 16
        if symbol in RIGHT:
            self.selected_index += 1
            self.selected_index %= 16
            if self.puzzle.state[self.selected_index] == 16:
                self.selected_index += 1
                self.selected_index %= 16
        if symbol in UP:
            self.selected_index -= 4
            self.selected_index %= 16
            if self.puzzle.state[self.selected_index] == 16:
                self.selected_index -= 4
                self.selected_index %= 16
        if symbol in DOWN:
            self.selected_index += 4
            self.selected_index %= 16
            if self.puzzle.state[self.selected_index] == 16:
                self.selected_index += 4
                self.selected_index %= 16
        if symbol in BUTTON_B:  # quit
            self.engine.pop_handlers()
            self.engine.scenes.pop()
        if symbol in BUTTON_A:
            blank_index = self.puzzle.state.index(16)
            if blank_index // 4 == self.selected_index // 4:  # same row
                if blank_index > self.selected_index:
                    rotated_row = [16] + self.puzzle.state[self.selected_index:blank_index]
                    self.puzzle.state[self.selected_index:blank_index + 1] = rotated_row
                else:
                    rotated_row = self.puzzle.state[blank_index + 1:self.selected_index + 1] + [16]
                    self.puzzle.state[blank_index:self.selected_index + 1] = rotated_row
            elif blank_index % 4 == self.selected_index % 4:  # same column
                if blank_index > self.selected_index:
                    rotated_column = [16] + self.puzzle.state[self.selected_index:blank_index:4]
                    self.puzzle.state[self.selected_index:blank_index + 1:4] = rotated_column
                else:
                    rotated_column = self.puzzle.state[blank_index + 4:self.selected_index + 4:4] + [16]
                    self.puzzle.state[blank_index:self.selected_index + 1:4] = rotated_column
            else:
                return
            self.selected_index = blank_index
        if self.puzzle.state == self.puzzle.solved:
            pyglet.clock.schedule_interval(self.glow, 1/8)
            self.engine.set_handlers(on_draw=self.win_draw,
                                     on_key_press=self.win_key_press)

    def win_draw(self):
        self.engine.window.clear()
        self.puzzle_bg.blit(0, 0)
        for i in range(len(self.puzzle.state)):
            img = self.puzzle_image.get_region(*self.image_map[self.puzzle.state[i]])
            img.blit(*self.screen_map[i])
        return pyglet.event.EVENT_HANDLED

    def win_key_press(self, symbol, modifiers):
        if symbol != pyglet.window.key.ESCAPE:
            self.engine.pop_handlers()
            self.engine.scenes.pop()


if __name__ == "__main__":
    from Engine import Engine, View
    view = View()
    engine = Engine(view)
    engine.scenes.append(SceneFifteen(engine))
    pyglet.app.run()