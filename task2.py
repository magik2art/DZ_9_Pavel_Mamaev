class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def mass_of_asphalt(self):
        mass_of_asphalt = self._length * self._width * self.weight * self.height / 1000
        print(f'Масса асфальта необходимая для покрытия одного кв. метра дороги асфальтом, '
              f'толщиной в 1 см для покрытия всего дорожного полотна = {round(mass_of_asphalt)} тонн')


length = 5000
width = 20

Road(length, width).mass_of_asphalt()
