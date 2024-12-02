#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name="Snoopy", breed= "Corgi"):
        self.breed = breed
        self.name = name
    def get_name(self):
        return self._name
        
    def set_name(self,name):
        if isinstance(name,str)  and (1<= len(name) <=25):
                self._name = name
        else:
          print("Name must be string between 1 and 25 characters.")
          self._name = "Invalid Name"
    name = property(get_name,set_name)
    def get_breed(self):
        return self._breed
    def set_breed(self,breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Invalid Breed"
    breed = property(get_breed,set_breed)
    
dog1 = Dog("Snoopy","Corgi")
print(dog1)
print(dog1.name)
dog2=Dog("ribashongilokasheshiakilhgfdekdkedkabcdefghijklmon","Corgifr3erf")
print(dog2.name)
print(dog2.breed)