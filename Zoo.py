import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return f"{self.name} молчит."

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def make_sound(self):
        return f"{self.name} говорит Чирик!"

class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} говорит Гав!"

class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} говорит Шшш!"

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

    def save_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            data = {"animals": [{"name": a.name, "age": a.age, "type": a.__class__.__name__} for a in self.animals],
                    "staff": [{"name": s.name, "role": s.__class__.__name__} for s in self.staff]}
            json.dump(data, file, ensure_ascii=False, indent=4)

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

# Пример использования
zoo = Zoo()
zoo.add_animal(Bird("Чижик", 2))
zoo.add_animal(Mammal("Бобик", 5))
zoo.add_animal(Reptile("Гектор", 4))

keeper = ZooKeeper("Иван")
vet = Veterinarian("Мария")

zoo.add_staff(keeper)
zoo.add_staff(vet)

animal_sound(zoo.animals)  # Демонстрация полиморфизма
keeper.feed_animal(zoo.animals[1])  # Смотритель кормит животное
vet.heal_animal(zoo.animals[2])  # Ветеринар лечит животное

zoo.save_to_json('zoo_data.json')  # Сохранение данных зоопарка в файл JSON
