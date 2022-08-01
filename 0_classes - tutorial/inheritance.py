class Dog:
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self):
        return True
    
    def bark(self):
        return 'woof!'

class Samoyed(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def bark(self):
        return 'Arf! Arf!'

class Poodle(Dog): 
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def shedding_amount(self):
        return 0

class GoldenRetriever(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)
    
    def fetch_ability(self):
        if self.age < 2:
            return 8
        elif self.age < 10:
            return 10
        else:
            return 7
    
    def bark(self):
        return 'AROOOOOO!'

# multiple inheritance
class GoldenDoodle(Poodle, GoldenRetriever):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)


sammy = Samoyed('Sammy', 2, 10)

goldie = GoldenDoodle('Goldie', 1, 10)

generic_doggo = Dog('Gene', 10, 10)

print(goldie.bark())
print(sammy.bark())
print(generic_doggo.bark())