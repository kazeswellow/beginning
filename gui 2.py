from guizero import *


def main():
    def calculate():
        try:
            base = float(tbx_base.value)
            power = float(tbx_power.value)
            answer = f'{base**power}'
            text_answer.value = answer
        except ValueError:
            error(title='calculator', text='both entries must be numeric')

    app = App()
    app.text_size = 20

    Box(app, height=20, width=10)
    box_1=Box(app, height=50, width=250)
    Text(box_1, text='base', align='left')

    tbx_base = TextBox(box_1, align='left')
    Box(app, height=20, width=10)

    Text(app, text='power')

    tbx_power = TextBox(app)
    Box(app, height=20, width=10)

    text_answer = Text(app)
    Box(app, height=20, width=10)

    PushButton(app, text='calculate', command=calculate)

    app.display()


if __name__ == '__main__':
    main()
