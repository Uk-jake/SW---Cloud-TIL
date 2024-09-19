class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def setName(self, name):
        self.name = name
        
    def setAge(self, age):
        self.age = age
    

person1 = Person("John", 35)
person2 = Person("Alice", 25)

people = [person1, person2]

for person in people:
    print(f"Name: {person.getName()}, Age: {person.getAge()}")