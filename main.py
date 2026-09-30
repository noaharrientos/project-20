class vehicle:
    def __init__ ( self , Model , MaxPersonCapacity ) :
        self.Model=Model
        self.MaxPersonCapacity = MaxPersonCapacity
    def display ( self ) :
        print ( f" The model of the car is { self.Model } , and the max people that can fit inside of the car is { self.MaxPersonCapacity } " )
class car ( vehicle ) :
    def __init__ ( self, Model , MaxPersonCapacity , Brand , MaxSpeed , Interior ) :
        vehicle . __init__ ( self , Model , MaxPersonCapacity )
        self . Brand = Brand
        self . MaxSpeed = MaxSpeed
        self . Interior = Interior
    def displayvalues ( self ) :
        print ( f" The brand of the car is { self . Brand } , the max speed the car can go is { self . MaxSpeed } and the Interior is { self . Interior } " )
object1 = car ( 911 , 2 , "Porsche" , "297km/184mi" , "Leather" )
object1.display()
object1.displayvalues()