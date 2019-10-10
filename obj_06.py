# -*- coding: utf-8 -*-

class Home:
    __s = None
    __pets = None

    def __init__(self, pets):
        self.__s = 100
        self.__pets = pets
        self.__foods = 200

    @staticmethod
    def get_s(self): return self.__s

    @staticmethod
    def get_pets(self): return self.__pets

    @staticmethod
    def get_foods(self): return self.__foods

    @staticmethod
    def set_foods(self,foods):
        self.__foods = foods
        return self.__foods

class Pets():
    pets = []
    def __init__(self):
        self.angry = "yes"

    @classmethod
    def get_pets(cls): return cls.pets

    @classmethod
    def set_pets(cls, val): cls.pets = val

    def add_pet(self, pet):
        pets = self.get_pets()
        pets.append(pet)
        self.set_pets(pets)

    def del_pet(self, pet):
        pets = self.get_pets()

        for i in range(len(pets)):
            if pets[i].vid == pet.vid:
                pets.pop(i)
                break

            self.set_pets(pets)

class Cat():
    def __init__(self):
        self.vid = 'cat'
        self.s = 20
        self.food = 10
        self.price = 20

class Hamster():
    def __init__(self):
        self.vid = 'hamster'
        self.s = 10
        self.food = 2
        self.price = 3

class Master(Home):
    def __init__(self, pets):
        super(Master, self).__init__(pets)
        self.cash = 100
        self.name = "Vasia"

    def buy_Pets(self, pet):
        s = aval_s = 0

        money = self.cash - pet.price
        pets = super(Master, self).get_pets(self)

        for pt in pets.get_pets():
            s = s + pt.s

        aval_s = super(Master, self).get_s(self) - s

        if money < 0: return
        elif aval_s <= 0: return
        else:
            super(Master, self).get_pets(self).add_pet(pet)   #но ведь адд пет в классе петс, а не хоум?
            self.cash = money

    def Food_pets(self):
        pets = self.get_pets(self)
        food = self.get_foods(self)
        print("angry=", pets.angry)

        for pt in pets.get_pets():
            food = food - pt.food

        self.set_foods(self, food)
        pets.angry = "No"

        print("cash =", self.cash)
        print("pets =", pets.get_pets())
        print("food =", food)
        print("angry =", pets.angry)

m = Master(Pets())
m.buy_Pets(Cat())
m.buy_Pets(Hamster())
m.buy_Pets(Cat())
m.buy_Pets(Cat())
m.buy_Pets(Hamster())
m.Food_pets()

#дз:
#перестроить иерархию чтобы кэт и хамстер наследовались от петс
#если еды не хватает, то кошки могут съесть хомячков