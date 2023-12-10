import pygame as pg
from random import choice


class ResultWorker:
    FONT_PATH = 'd_font.ttf'
    FONT_SIZE = 36

    def __init__(self, app):
        pg.init()

        self.app = app

        self.font = pg.font.Font(self.FONT_PATH, self.FONT_SIZE)
        self.char_size = self.font.render('Q', True, (0, 0, 0)).get_size()
        self.image = pg.Surface((10, 10))

    def create_image(self, info: dict, color=(255, 255, 255), bg=(0, 0, 0)):
        """
        info = {'char_light': self.CHARS,
                'img_light': light_coords,
                'counts': brick_count,
                'width': self.res_img_width}
        """
        new_w = self.char_size[0] * info['counts'][0]
        new_h = self.char_size[1] * info['counts'][1]
        self.image = pg.Surface((new_w, new_h))
        self.image.fill(bg)

        # draw chars
        levels = info['img_light']
        chars = info['char_light']
        for level in levels:
            for coord in levels[level]:
                x = coord[0] * self.char_size[0]
                y = coord[1] * self.char_size[1]

                char = choice(chars[level])
                temp = self.font.render(char, True, color)

                self.image.blit(temp, (x, y))

        # resize image
        scale = info['width'] / self.image.get_width()
        self.image = pg.transform.rotozoom(self.image, 0, scale)

    def save(self, path):
        pg.image.save(self.image, path)

