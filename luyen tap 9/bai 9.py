import random

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Động vật đang tạo ra âm thanh...")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        sounds = ["Gâu gâu!", "Ẳng ẳng!", "Wof wof!"]
        print(f"Chó {self.name} sủa: {random.choice(sounds)}")
cho_con = Dog("Cậu Vàng")
cho_con.sound()