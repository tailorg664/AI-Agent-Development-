class Dog:
      
      def __init__(self,name):
            self.name = name
            self.tricks = []
      def add_trick(self,trick):
            self.tricks.append(trick)
      

############################

german = Dog("German Shepherd")
german.add_trick("Sit")
labrador = Dog("Labrador")
labrador.add_trick("Fetch")
print(german.tricks)
print(labrador.tricks)