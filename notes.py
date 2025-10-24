# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    """"A simple Dog class to learn OOP

    Atrributes:
        fur_col - the color of the dogs fur
        name - the name of the dog
        age - the age of the dog
        favorite_food - the dog's favorite food
       
         __init__ intializes the class
    
    
    """ 
    def __init__(self, fur_color = "black", name="", age = 1, favorite_food = "kibble"):
        """Initialize a new Dog with fur_color, name, age, and favorite food"""
        self.fur_color = fur_color
        self.name = name
        self.age = age
        self.favorite_food = favorite_food
    def __str__(self):
        """return a string representation of a dog"""
        return f"{self.name} is a {self.age} year old {self.fur_color} dog who loves {self.favorite_food}"
    
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof, Woof!!"
    def birthday(self):
        """Celebrate the dog's birthday"""
        self.age += 1
        print(f"Celebrating{self.name} birthday.")
    def change_favorite_food(self, new_food):
        """Change the favorite food of the dog"""
        old_food = self.favorite_food
        self.favorite_food = new_food
        print(f"{self.name} use to love {old_food} and now oves {self.favorite_food}")




my_dog = Dog("black", "logan", 9, "salmon")
enggy_dog = Dog("black and white", "pelunchin", 13, "rice")
default_dog = Dog()
aaron_dog = Dog("peach and white", "dumbo", favorite_food="anything edible")

print(my_dog)
print(enggy_dog)
print(default_dog)
print(aaron_dog)



print()
print(enggy_dog.bark())

aaron_dog.birthday()
print(aaron_dog)




  