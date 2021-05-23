class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'\n{self.name} поехала'

    def stop(self):
        return f'\n{self.name} остановилась'

    def turn(self, direction):
        if self.name == 'Porshe' and direction == "назад":
            return (f'\n(Анекдот бонус от разработчика) Комментатор: — Да—а, гонки уже подходят к концу, а российский гонщик '
                    f'все никак не догоняет... Не догоняет, что надо ехать в другую сторону! =)')
            pass
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость машины {self.name} - {self.speed} км/ч ВЫШЕ допустимой'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class PoliceCar(Car):
    pass


street_town_car = TownCar('Kia-rio', 80, 'Белый', False)
street_sport_car = SportCar('Porshe', 190, 'Чёрный', False)
street_work_car = WorkCar('Lada', 39, 'Бежевый', False)
street_police_car = PoliceCar('Hammer', 200, 'Синий', True)
check = [street_town_car, street_sport_car, street_work_car, street_police_car]

for test in check:
    print(test.go(), test.show_speed(), test.turn('налево'),
          test.turn('направо'), test.turn('назад'), test.stop())
