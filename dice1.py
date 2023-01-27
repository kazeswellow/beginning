from guizero import *
from random import choice

"""
roll a pair of dice and show the total
"""

SPOTS = 1, 2, 3, 4, 5, 6


def main():
    def roll():
        die_1 = choice(SPOTS)
        die_2 = choice(SPOTS)
        total = die_1 + die_2
        left_die.image = f"images/dice{die_1}.png"
        right_die.image = f"images/dice{die_2}.png"
        txt_total.value = f"total roll = {total}"

    app = App(title="roll the dice", bg="dark green")
    app.text_size = 24

    Box(app, height=20, width=20)
    box_dice = Box(app, height=200, width=400, border=20)

    Box(app, height=20, width=20)
    pb_roll = PushButton(app, text="ROLL", command=roll)
    pb_roll.bg = "tan"
    pb_roll.text_color = "red"

    Box(app, height=20, width=20)
    txt_total = Text(app, color="cyan")

    left_die = Picture(box_dice, width=150, height=150, align="left")

    right_die = Picture(box_dice, width=150, height=150, align="right")

    app.display()


if __name__ == '__main__':
    main()