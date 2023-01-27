from guizero import *
from random import randint

IDX_COUNTER = 0
IDX_HIDE_TIME = 1
IDX_OUT_TIME = 2

MAX_HIDE_TIME = 10
MIN_HIDE_TIME = 5
MAX_OUT_TIME = 10
MIN_OUT_TIME = 5

ROWS = 4
COLUMNS = 5


def main():
    def popup():
        if timers[IDX_COUNTER] >= 0:
            waf_field[0, 0].color = "tan"
        else:
            waf_field[0, 0].color = "black"

        timers[IDX_COUNTER] += 1
        if timers[IDX_COUNTER] > timers[IDX_OUT_TIME]:
            reset_time = -randint(MIN_HIDE_TIME, MAX_HIDE_TIME)
            out_time = randint(MIN_OUT_TIME, MAX_OUT_TIME)

            timers[IDX_COUNTER] = reset_time
            timers[IDX_HIDE_TIME] = reset_time
            timers[IDX_OUT_TIME] = out_time
        print(timers)

    app = App(title="Whack A Mole", bg="green")

    """
    timer array
    index 0 = counter
    index 1 = reset value
    index 2 = max value
    """
    timers = [-MAX_HIDE_TIME, -MAX_HIDE_TIME, MAX_OUT_TIME]

    waf_field = Waffle(app, height=ROWS, width=COLUMNS, dim=50, pad=20, color="black", dotty=True)

    app.repeat(1000, popup)
    app.display()


if __name__ == '__main__':
    main()