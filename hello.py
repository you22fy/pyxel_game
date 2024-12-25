import pyxel
from dataclasses import dataclass


@dataclass
class AppConst:
    WIDTH = 160
    HEIGHT = 120
    TITLE = "Hello Pyxel"


class App:
    def __init__(self):
        pyxel.init(AppConst.WIDTH, AppConst.HEIGHT, title=AppConst.TITLE)
        self.x, self.y = 0, 0
        self.speed = 2

        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(7)
        pyxel.rect(self.x, self.y, 10, 10, 2)

    def update(self):
        if pyxel.btn(pyxel.KEY_W):
            self.y = max(0, self.y - self.speed)
        if pyxel.btn(pyxel.KEY_S):
            self.y = min(pyxel.height - 10, self.y + self.speed)
        if pyxel.btn(pyxel.KEY_A):
            self.x = max(0, self.x - self.speed)
        if pyxel.btn(pyxel.KEY_D):
            self.x = min(pyxel.width - 10, self.x + self.speed)


if __name__ == "__main__":
    App()
