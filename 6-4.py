class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'\nАвтомобиль {self.name} начал движение.'

    def stop(self):
        return f'\nАвтомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):

        if self.speed > 60:
            return f'\nВы превысили рекомендуемую скорость! Ваша скорость {self.speed}'
        else:
            return f'Скорость {self.name} в пределах рекомендуемых значений'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы превысили рекомендуемую скорость! Ваша скорость {self.speed}'
        else:
            return f'Скорость {self.name} в пределах рекомендуемых значений'


class PoliceCar(Car):
    pass


town = TownCar('KIA', 80, 'black', False)
print(town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('FERRARI', 220, 'red', False)
print(sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop())

work = WorkCar('ZAZ', 30, 'yellow', False)
print(work.go(), work.show_speed(), work.turn('налево'), work.stop())

police = PoliceCar('TOYOTA', 100, 'white', True)
print(police.go(), police.show_speed(), police.turn('налево'), police.stop())