import random
class Product:
    """ Class for creating the Product of Acme Corporation """

    def __init__(self,name,price=10,weight=20,flammability=0.5):
        """
        Initialising the Product class
        name : Name of the product
        price : Price of the product, default value is 10
        weight : Weight of the product, defualt value is 20
        flammability : Flammability of the product, default value is 0.5
        identifier : Integer to identify the prodcut generated randomly values between 1000000 to 9999999
        """
        self.identifier = random.randint(1000000 ,9999999)
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability


    def stealability(self):
        """ 
        Method to calculate stealibility of the prodcut
        It is calculated by using the price divided by the weight
        and then returns a message: if the ratio is less than 0.5 
        return "Not so stealable...", if it is greater or equal to
        0.5 but less than 1.0 return "Kinda stealable.", and
        otherwise return "Very stealable!"

        """
        self.steal_factor = self.price/self.weight

        if(self.steal_factor <0.5):
            return "Not so stealable..."
        elif((self.steal_factor <1) & (self.steal_factor >=0.5)):
            return "Kinda stealable."
        else:
            return "Very stealable!"


    def explode(self):
        """
        calculates the flammability of the prodcut.
        It is calculated by using flammability times the weight, and
        then returns a message: if the product is less 
        than 10 return "...fizzle.", if it is greater or
        equal to 10 but less than 50 return "...boom!",
        and otherwise return "...BABOOM!!"

        """
        self.exploding = self.flammability*self.weight
        if( self.exploding <10):
            return "...fizzle."
        elif((self.exploding <50) & (self.exploding >=10)):
            return "...boom!"
        else:
            return "...BABOOM!!"

class BoxingGlove(Product):
    """ Special kind of Product inhertied from Product class"""
    
    def __init__(self,name,price=10,weight=10,flammability=0.5):
        """ All the values of product remain the same, except for weight"""
        super().__init__(name=name,price=price,weight=weight,flammability=flammability)

    def explode(self):
        """ Overrides the explode of Product"""

        return "...it's a glove."
                
    def punch(self):
        """ Special method of Boxing glove """

        if( self.weight <5):
            return "That tickles."
        elif((self.weight <15) & (self.weight >=5)):
            return "Hey that hurt!"
        else:
            return "OUCH!"

            