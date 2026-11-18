class Chainsaw:
    def __init__(self, name="Unknown", power=0, rpm=0, color="Unknown", weight=0):
        self.__name = name
        self.__power = power
        self.__rpm = rpm
        self.color = color
        self.weight = weight

    def get_name(self):
        return f'Назва:{self.__name}'
    def get_power(self):
        return f'Потужність:{self.__power} Вт'
    def get_rpm(self):
        return f'кількість обертів:{self.__rpm} од/хв'
    def get_else(self):
        return f'Колір = {self.color}, Вага = {self.weight}'
    def __str__(self):
        return f'{self.__name}: {self.__power} Вт, {self.__rpm} од/хв'
    def __repr__(self):
        return f'Chainsaw(name = {self.__name}, power = {self.__power} Вт, rpm = {self.__rpm}, color = {self.color}, weight = {self.weight})'
    def __del__(self):
        print(f'Бензопилу {self.__name} видалено')
def main():
    chain_1 = Chainsaw("Bosch", 2, 12000, "black", 4.5)
    chain_2 = Chainsaw("Yamaha", 1.7, 11000, "blue", 4)
    chain_3 = Chainsaw("Husqvarna", 2.5, 13500, "gray", 5.5)

    print('1.',
        chain_1.get_name(),
        chain_1.get_power(),
        chain_1.get_rpm(),
        chain_1.get_else(),
        chain_1,
        repr(chain_1), sep = "\n"
    )

    print('2.',
        chain_2.get_name(),
        chain_2.get_power(),
        chain_2.get_rpm(),
        chain_2.get_else(),
        chain_2,
        repr(chain_2), sep = "\n"
    )
    print('3.',
        chain_3.get_name(),
        chain_3.get_power(),
        chain_3.get_rpm(),
        chain_3.get_else(),
        chain_3,
        repr(chain_3), sep = "\n"
    )
if __name__ == '__main__':
    main()

    