class Vehicle:
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    __COLOR_VARIANTS = {'blue', 'green', 'yellow', 'red', 'black', 'white'}

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, engine_power, color)
        if color not in Sedan.__COLOR_VARIANTS:
            raise ValueError(f"Цвет должен быть одним из: {Sedan.__COLOR_VARIANTS}")

    def print_info(self):
        print(f"Модель: {self.get_model()}")
        print(f"Мощность двигателя: {self.get_horsepower()}")
        print(f"Цвет: {self.get_color()}")
        print(f"Владелец: {self.owner}")

    def change_owner(self, new_owner):
        self.owner = new_owner

    def set_color(self, new_color):
        if new_color not in Sedan.__COLOR_VARIANTS:
            print(f"Нельзя сменить цвет на {new_color}")
        else:

            self._Vehicle__color = new_color


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Pink')

vehicle1.change_owner('Vasyok')

vehicle1.set_color('black')

vehicle1.print_info()
