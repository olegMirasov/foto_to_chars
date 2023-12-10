from PIL import Image
from numpy import mean, array


class ImageWorker:
    def __init__(self, app, path):
        self.app = app
        self.path = path

        self.image = Image.open(self.path).convert('L')
        self.arr = array(self.image)

        self.parts = []
        self.light_levels = dict()

    @property
    def size(self):
        return self.image.size

    def split_image(self, wx, wy):
        size = self.size
        x = int(size[0] / wx)
        y = int(size[1] / wy)
        self.parts = []
        for i in range(x):
            ii = i * wx
            for j in range(y):
                jj = j * wy
                temp = self.arr[jj: jj + wy, ii: ii + wx]
                self.parts.append(Part(i, j, temp))
        return x, y

    def get_light_level(self, count_levels: int):
        if not self.parts:
            return
        self.light_levels = dict()
        self.parts = sorted(self.parts, key=lambda x: x.light, reverse=True)

        step = int(len(self.parts) / count_levels)

        temp = self.parts
        for i in range(count_levels):
            self.light_levels[i] = temp[:step]
            temp = temp[step:]

        # prepare data for draw chars
        for k in self.light_levels:
            temp = [(part.x, part.y) for part in self.light_levels[k]]
            self.light_levels[k] = temp
        return self.light_levels


class Part:
    def __init__(self, x: int, y: int, arr: array):
        self.x = x
        self.y = y
        self.light = mean(arr)
        self.level = 0

    @property
    def pos(self):
        return self.x, self.y
