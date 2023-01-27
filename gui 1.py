from guizero import *


def main():
    def click():
        if txt_greeting.value == 'hello':
            txt_greeting.value = 'bye'
        else:
            txt_greeting.value = 'hello'

    app = App()

    txt_greeting = Text(app, text='hello')

    PushButton(app, text='click', command=click)

    app.display()


if __name__ == '__main__':
    main()
