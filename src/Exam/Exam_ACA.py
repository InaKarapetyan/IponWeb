import datetime
from datetime import timedelta

#TASK1
class Patient:
    def __init__(self,name,surname,age: int in range(18,101),gender):
        self.name = name
        self.surname = surname
        self.age = age
        for gender in ['M', 'F']:
            self.gender = gender
    
    def __repr__(self):
        return f"{self.name} {self.surname} - {self.gender}, {self.age} years old."
    
    def __ne__(self,another):
        if isinstance(another, Patient):
            return self.name != another.name or self.surname != another.surname

p = Patient("Ina", "Karapetyan", 15, "F")
#print(p)





class Doctor(Patient):
    def __init__(self,name: str,surname: str,scedule):
        self.name = name
        self.surname = surname
        self.scedule = {}
    
    def __repr__(self):
        return f"Doctor {self.name} {self.surname} has the following available scedule {self.scedule}"

    
    def register_patient(self, patient, datetime):
        duration = datetime.timedelta(minutes=30)
        if self.is_free(datetime) and self.is_free(datetime + duration):
            self.schedule[datetime] = patient
            return True
        return False


    def is_free(self, datetime):
        duration = datetime.timedelta(minutes=30)
        end_time = datetime + duration
        for schedule_time in self.schedule.items():
            if schedule_time <= datetime < schedule_time + duration or schedule_time < end_time <= schedule_time + duration:
                return False
        return True


    def is_registered(self, patient):
        for registration in self.schedule.values():
            return any(registration == patient)




scedule = datetime.datetime(2023, 2, 6, 10, 0, 0)
doctor = Doctor("Vardan", "Vardanyan", scedule)
print(doctor.is_free(scedule)) 

register = doctor.register_patient("Patient A", scedule)
print(register) 

print(doctor.is_free(scedule)) 
print(doctor.is_registered("Patient A")) 
#print(doctor)






#2

class Product:
    def __init__(self, price: int, id : int, quantity: int):
        self.price = price
        self.id = id
        self.quantity = quantity

    def __repr__(self):
        return f"We have {self.quantity} items of ID {self.id} with {self.price}$"
    
    def buy(self, count):
        if count<= self.quantity:
            self.quantity-=count
            return f"The {count} items of this product is confirmed to be bought"

        elif count > self.quantity:
            raise ValueError

    
        

product=Product(12,14,15)
#print(product)
#print(product.buy(14))



class Inventory(Product):

    def __init__(self, list : list, quantity, id, price):
        super().__init__(quantity,id,price)
        self.list = list

    def get_by_id(self,search_id):
        for object in list:
            if object.id == search_id:
                return f"The price is: {self.price}\nThe ID is: {self.id}\nThe quantity is: {self.quantity}"
            else:
                raise ValueError

    def __repr__(self):
            return f"This is an ID of the element you want: {self.id}" 


    def sum_of_products(self):
        sum = 0

        for product in list:
            sum+=product.quantity
        return sum
            
another = Product(16,10,18)
#print(another)
list = [product, another]
#print(Inventory.get_by_id(another, 10))
#print(Inventory.sum_of_products(list))










#3




class Hotel:

    def __init__(self, city, rooms: dict):
        self.city = city
        self.rooms = rooms
    
    def __repr__(self):
        return f"The hotel is located in {self.city} and has these rooms available{self.rooms}"
    
    def get_city(self):
        return f"The city the passenger wants to fly: {self.city}"
    
    def free_rooms_list(self,type):
        keys = self.rooms.keys()
        for key in keys:
            if key == type:
                return self.rooms[key]
    
    def reserve_rooms(self, type,count):
        keys = self.rooms.keys()
        for key in keys:
            if key == type:
                if self.rooms[key] == 0:
                    print("No avaialble rooms, sorry") 
                else:
                    self.rooms[key] = self.rooms[key] - count
                    print("Reserved! We are happy to welcome YOU")




k = {"penthouse": 2, "single" : 3, "double " : 4} 
hotel = Hotel("Stepanavan",k)






class Passenger(Hotel):
    def __init__(self, name :str,city: str,rooms: dict):
        self.__name = name
        self.city = city
        self.rooms = rooms
    
    def __repr__(self):
        return f"The passenger named {self.name} wants to fly to {self.city}"
    
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self,value):
        self.__name = value
    
    def get_city(self):
        return f"The city the passenger wants to fly: {self.city}"
    
    def get_room(self,type,count):
        return hotel.reserve_rooms(type, count)








def Book(hotel,passenger):
    print(passenger.get_room('single', 1))
    print(passenger)
    print(hotel)
    print(hotel.free_rooms_list("penthouse"))
    hotel.reserve_rooms("penthouse",1)
    print(hotel.free_rooms_list("penthouse"))

k = {"penthouse": 2, "single" : 3, "double " : 4} 
passenger = Passenger("Stepan", "Stepanavan", k)
Book(hotel,passenger)