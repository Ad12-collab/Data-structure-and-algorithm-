
   class person:
 age=7
 def __init__(self,name):
 self.name=name
 def display(self):
 print("this is a class with out __init__()")
 print("i am",self.name,"and i am ",person.age, "years")
y = person("hana")
print(y.age)
y.display()
y.name="dawit"
person.age=15
y.display()