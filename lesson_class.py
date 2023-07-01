
class Poultry:
    def __init__(self, color, sound, specy):
        self.color = color
        self.sound = sound
        self.specy = specy

    def make_some_noise(self):
        print(f"{self.specy} is making some noise !! {self.sound * 3}")

    def move(self):
        print(f"{self.specy}  move.")

    def eat(self):
        print(f"{self.specy}  eat.")

    def hatch(self):
        print(f"{self.specy}  hatch zzz.")

class Duck(Poultry):
    def __init__(self, color, sound):
        super().__init__(color, sound, 'Duck')

    def swim(self):
        print(f"{self.specy}  swim ~")

class Chicken(Poultry):
    def __init__(self, color, sound):
        super().__init__(color, sound, "Chicken")

    def moring_call(self, time):
        print(f"{self.sound *3}, It's {time} a.m. now")


if __name__ == '__main__':
    duck_1 = Duck('yellow', "ba")
    duck_2 = Duck('black', "ga")
    duck_3 = Duck("White", "gua")

    duck_2.make_some_noise()
    print(duck_2.sound)






# poultry
# Goose 鵝