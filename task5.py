class Stationery:

    def __init__(self, name):
        self.title = name
        self.text = f'«Запуск отрисовки» при помощи предмета -'

    def draw(self):
        return self.text


class Pen(Stationery):
    def draw(self):
        return f'{self.text} {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'{self.text} {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'{self.text} {self.title}'


def check(something_stationery):
    print(something_stationery.draw())


test = [Pen('Ручка'), Pencil('Карандаш'), Handle('Маркер')]

for some_stationery in test:
    check(some_stationery)
