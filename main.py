import random

class House:
    def __init__(self):
        self.food = 50
        self.money = 100

    def __str__(self):
        return f"У будинку залишилось: Їжі - {self.food}, Грошей - {self.money}"

class Person:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50  # ситість
        self.happiness = 100  # щастя
        self.house = house

    def eat(self):
        if self.house.food >= 10:
            self.satiety += 10
            self.house.food -= 10
            print(f"{self.name} поїв. Ситість: {self.satiety}")
        else:
            print(f"{self.name} не зміг поїсти — їжі немає!")

    def work(self):
        self.house.money += 50
        self.satiety -= 10
        print(f"{self.name} попрацював. Грошей у будинку: {self.house.money}")

    def play(self):
        self.happiness += 10
        self.satiety -= 5
        print(f"{self.name} пограв у гру. Щастя: {self.happiness}")

    def shopping(self):
        if self.house.money >= 20:
            self.house.food += 20
            self.house.money -= 20
            print(f"{self.name} сходив у магазин. Приніс їжу: 20")
        else:
            print(f"{self.name} не зміг купити їжу — недостатньо грошей!")

    def live_day(self):
        action = random.choice(["eat", "work", "play", "shopping"])
        if action == "eat":
            self.eat()
        elif action == "work":
            self.work()
        elif action == "play":
            self.play()
        elif action == "shopping":
            self.shopping()

        # Зниження щастя і ситості з кожним днем
        self.satiety -= 2
        self.happiness -= 1

    def __str__(self):
        return f"{self.name} — Ситість: {self.satiety}, Щастя: {self.happiness}"

# Симуляція
home = House()
sim = Person("Олексій", home)

for day in range(1, 11):
    print(f"\nДень {day}")
    sim.live_day()
    print(sim)
    print(home)
