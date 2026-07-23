class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def introduce(self):
        print(f"Hi! My name is {self.name}. I am {self.age} years old and I am {self.color}.")

cat1 = Cat("Mira", 3, "orange")
cat2 = Cat("Luma", 5, "white")
cat3 = Cat("Verda", 2, "black")
cat1.introduce()
cat2.introduce()
cat3.introduce()