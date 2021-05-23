class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.position_name = name
        self.position_surname = surname
        self._position = position
        self.position_income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.position_name + ' ' + self.position_surname

    def get_total_income(self):
        return self.position_income["wage"] + self.position_income["bonus"]


start = Position('Pavel', 'Mamaev', 'Director', 30000, 250000)
print(start.get_full_name(), start.get_total_income())
