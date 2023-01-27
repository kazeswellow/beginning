from guizero import *
from random import randint
from math import sqrt, pow

SIDE = 300
CENTER_X = CENTER_Y = int(SIDE / 2)
SHOTS = 100_000


def main():
    def initialize():
        dwg.clear()
        dwg.oval(0, 0, SIDE, SIDE, color="tan",
                 outline=True, outline_color="red")

    def shoot():
        total_hits = 0
        for i in range(SHOTS):
            x = randint(0, SIDE - 1)
            y = randint(0, SIDE - 1)

            x1, y1 = (x - 2, y - 2)
            x2, y2 = (x + 2, y + 2)

            distance = sqrt(pow(x - CENTER_X, 2) + pow(y - CENTER_Y, 2))
            if distance < SIDE / 2:
                dwg.oval(x1, y1, x2, y2, color="blue")
                total_hits += 1
            else:
                dwg.oval(x1, y1, x2, y2)
        print(total_hits / SHOTS * 4)

    app = App(title="monte carlo simulation", width=500, height=550)
    app.text_size = 16

    Box(app, height=20, width=99)
    dwg = Drawing(app, width=SIDE, height=SIDE)
    dwg.bg = "tan"

    initialize()
    shoot()
    app.display()


if __name__ == '__main__':
    main()
