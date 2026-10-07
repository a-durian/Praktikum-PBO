from abc import ABC, abstractmethod

class Repository(ABC):
    
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def remove(self):
        pass
    
class UserRepository:
    def add(self):
        print("add user")

    def remove(self):
        print("remove user")
        
class ProductRepository:
    def add(self):
            print("add user")
    
    def remove(self):
        print("remove user")
        
        
products = [ProductRepository(), UserRepository()]

for repository in products:
    repository.add()
