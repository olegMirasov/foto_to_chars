from image_worker import ImageWorker
from result_worker import ResultWorker


class Main:
    IMG_PATH = 'image/'
    RES_PATH = 'result/'
    CHARS = {0: '@B#%WDQR',
             1: 'GMgNO&mP',
             2: 'HEqpdbZ$',
             3: 'KUSeXAaw',
             4: 'FhVkCyou',
             5: 'nzTsfYxL',
             6: '_|[]{}*v',
             7: 'ctjJ=?)(',
             8: 'r\\/lI+<>',
             9: '!i-"~^;,'}
    '''CHARS = {0: '@B#%WDQRGMgNO&mPHEqpdbZ$KUSeXAawFhVkCyounz',
             1: 'TsfYxL_|[]{}*vctjJ=?)(r/lI+<>!i-"~^;,`:.'}'''
    '''CHARS = {0: '@B#%WDQRGMgNO&mPHEqpd',
             1: 'bZ$KUSeXAawFhVkCyounz',
             2: 'TsfYxL_|[]{}*vctjJ=?)',
             3: '(r/lI+<>!i-"~^;,`:.'}'''

    def __init__(self, img_name: str,
                 w_char_count: int,
                 res_img_width: int):
        self.name = img_name
        self.img_name = self.IMG_PATH + img_name
        self.w_char_count = w_char_count
        self.h_char_count = None
        self.res_img_width = res_img_width

        self.image_worker = ImageWorker(self, self.img_name)
        self.result_worker = ResultWorker(self)

    def run(self):
        # Определим уровни для изображения
        # Нужны данные для разделения изображения на полигоны
        img_size = self.image_worker.size
        char_size = self.result_worker.char_size

        # Найдем пропорции изображения с учетом размера букв
        img_x = int(img_size[0] / self.w_char_count)
        img_y = int(img_x * char_size[1] / char_size[0])

        # Получим координаты с учетом яркости изображения
        brick_count = self.image_worker.split_image(img_x, img_y)
        self.h_char_count = brick_count[-1]
        light_coords = self.image_worker.get_light_level(self.levels)

        # Создаем изображение из букв
        info = {'char_light': self.CHARS,
                'img_light': light_coords,
                'counts': brick_count,
                'width': self.res_img_width}
        self.result_worker.create_image(info)
        self.result_worker.save(self.RES_PATH + self.name)

    @property
    def levels(self):
        return len(self.CHARS)


if __name__ == '__main__':
    app = Main(img_name='mm.png', w_char_count=100, res_img_width=2000)
    app.run()
