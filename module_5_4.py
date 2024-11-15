class House:
    houses_history = []
    def __new__(cls, *args):
        cls.houses_history.append(args[0])

        return object.__new__(cls)
    def __init__(self,name, number_of_floors):
        self.name = name
        self.number = number_of_floors

    def go_to(self, new_floor):

        if int(new_floor) < 1 or int(new_floor) > int(self.number):
            print("Такого этажа не существует")
        else:
            i = 1
            while i <= int(new_floor):
                print(i)
                i += 1
    def __len__(self):
        return self.number
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number}"
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number==other.number
        elif  isinstance(other, int):
            return self.number == other
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number < other.number
        elif isinstance(other, int):
            return self.number < other
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)
    def __gt__(self, other):
        return not self.__le__(other)
    def __ge__(self, other):
        return not self.__lt__(other)
    def __ne__(self, other):
        return not self.__eq__(other)
    def __add__(self, other):
        if isinstance(other, int):
            self.number += other
        elif isinstance(other, House):
            self.number += other.number
        return self
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        return self.__add__(other)
    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)
