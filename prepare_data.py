import pygame as pg
from numpy import mean
from string import ascii_letters as asc, punctuation as pnc


# prepare pygame font. It uses to render all chars
pg.init()
FONT = pg.font.Font('d_font.ttf', 24)


class Char:
    def __init__(self, char):
        self.char = char
        self.render = FONT.render(self.char, True,
                                  (255, 255, 255), (0, 0, 0))
        self.light_rating = self.get_light()

    def get_light(self):
        arr = pg.surfarray.array3d(self.render)
        return mean(arr)


if __name__ == '__main__':
    strings = asc + pnc
    chars = [Char(i) for i in strings]
    chars = sorted(chars, key=lambda x: x.light_rating, reverse=True)

    # choosing the brightness separation levels
    step_lights = 10

    step = int(len(chars) / step_lights)

    res_dict = dict()

    for i in range(step_lights):
        res_dict[i] = chars[:step]
        chars = chars[step:]

    # prepare data to print
    for k in res_dict:
        temp = res_dict[k]
        temp = [i.char for i in temp]
        temp = ''.join(temp)
        res_dict[k] = temp

    print(res_dict)

    pg.quit()
