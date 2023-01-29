#___________________________________________________________________________

class DateTime:
    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        self.__year = year
        self.__month = month
        self.__day = day
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        
    def __repr__(self):
        return f"{self.__year}-{self.__month}-{self.__day} {self.__hour}:{self.__minute}:{self.__second}"

    @property
    def date(self):
        return f"{self.__year}-{self.__month}-{self.__day}"
    
    @date.setter
    def date(self, value):
        year, month, day = map(int, value.split("-"))
        self.__year = year
        self.__month = month
        self.__day = day

    @property
    def time(self):
        return f"{self.hour}:{self.minute}:{self.second}"
    
    @time.setter
    def time(self, value):
        hour, minute, second = map(int, value.split(":"))
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    @property
    def hour(self):
        return self.__hour
    
    @hour.setter
    def hour(self, hour):
        self.__hour = hour

    @property
    def minute(self):
        return self.__minute
    
    @minute.setter
    def minute(self, minute):
        self.__minute = minute

    @property
    def second(self):
        return self.__second
    
    @second.setter
    def second(self, second):
        self.__second = second
    
    @property
    def day(self):
        return self.__day
    
    @day.setter
    def day(self, day):
        self.__day = day
 
    def add_year(self,year):
        self.__year += year
        return self.__year
    
    def add_month(self, month):
        self.__month += month
        while self.__month > 12:
            self.__month -= 12
            self.__year += 1
    
    def add_day(self, day):
        while day > 0:
            if self.__month in [1, 3, 5, 7, 8, 10, 12]:
                if self.__day + day > 31:
                    day -= 31 - self.__day + 1
                    self.__day = 1
                    self.add_month(1)
                else:
                    self.__day += day
                    day = 0
            elif self.__month in [4, 6, 9, 11]:
                if self.__day + day > 30:
                    day -= 30 - self.__day + 1
                    self.__day = 1
                    self.add_month(1)
                else:
                    self.__day += day
                    day = 0
            else:
                if (self.__year % 4 == 0 and self.__year % 100 != 0) or self.__year % 400 == 0:
                    if self.__day + day > 29:
                        day -= 29 - self.__day + 1
                        self.__day = 1
                        self.add_month(1)
                    else:
                        self.__day += day
                    day = 0
                else:
                    if self.__day + day > 28:
                        day -= 28 - self.__day + 1
                        self.__day = 1
                        self.add_month(1)
                    else:
                        self.__day += day
                        day = 0
                        
    def add_hour(self, hour):
        while hour > 0:
            if self.__hour + hour >= 24:
                hour -= 24 - self.__hour
                self.__hour = 0
                self.add_day(1)
            else:
                self.__hour += hour
                hour = 0
    
    def add_minute(self, minute):
        while minute > 0:
            if self.__minute + minute >= 60:
                minute -= 60 - self.__minute
                self.__minute = 0
                self.add_hour(1)
            else:
                self.__minute += minute
                minute = 0
    
    def add_second(self, second):
        while second > 0:
            if self.__second + second >= 60:
                second -= 60 - self.__second
                self.__second = 0
                self.add_minute(1)
            else:
                self.__second += second
                second = 0

    def sub_year(self, year):
        self.__year -= year

    def sub_month(self, month):
        self.__month -= month
        while self.__month < 1:
            self.__month += 12
            self.__year -= 1

    def sub_day(self, day):
        while day > 0:
            if self.__day - day < 1:
                day -= self.__day
                self.sub_month(1)
                if self.__month in [1, 3, 5, 7, 8, 10, 12]:
                    self.__day = 31
                elif self.__month in [4, 6, 9, 11]:
                    self.__day = 30
                else:
                    if (self.__year % 4 == 0 and self.__year % 100 != 0) or self.__year % 400 == 0:
                        self.__day = 29
                    else:
                        self.__day = 28
            else:
                self.day -= day
                day = 0

    def sub_hour(self, hour):
        while hour > 0:
            if self.__hour - hour < 0:
                hour -= self.__hour
                self.__hour = 0
                self.sub_day(1)
                self.__hour = 23
            else:
                self.__hour -= hour
                hour = 0

    def sub_minute(self, minute):
        while minute > 0:
            if self.__minute - minute < 0:
                minute -= self.__minute
                self.__minute = 0
                self.sub_hour(1)
                self.__minute = 59
            else:
                self.__minute -= minute
                minute = 0


    def sub_second(self, second):
        while second > 0:
            if self.__second - second < 0:
                second -= self._second
                self.__second = 0
                self.sub_minute(1)
                self.__second = 59
            else:
                self.__second -= second
                second = 0



    def __add__(self, other):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.__year % 4 == 0:
            days_in_month[2] = 29

        self.__second += other


        while self.__second >= 60:
            self.__second -= 60
            self.__minute += 1


        while self.__minute >= 60:
            self.__minute -= 60
            self.__hour += 1


        while self.__hour >= 24:
            self.__hour -= 24
            self.__day += 1


        while self.__day > days_in_month[self.__month]:
            self.__day -= days_in_month[self.__month]
            self.__month += 1

        while self.__month > 12:
            self.__month -= 12
            self.__year += 1

        return self



    def __sub__(self, other):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.__year % 4 == 0:
            days_in_month[2] = 29

        self.__second -= other

        while self.__second < 0:
            self.__second += 60
            self.__minute -= 1

        while self.__minute < 0:
            self.__minute += 60
            self.__hour -= 1


        while self.__hour < 0:
            self.__hour += 24
            self.__day -= 1


        while self.__day < 1:
            self.__month -= 1
            self.__day += days_in_month[self.__month]


        while self.__month < 1:
            self.__year -= 1
            self.__month += 12

        return self

class DateTimeError(Exception):
    def __init__(self, error):
        self.error = error
    
    def __repr__(self):
        return self.error

dt = DateTime(2003, 5, 12, 0, 0, 0)
dt.sub_minute(3)
print(dt)
dt.sub_day(2)
print(dt)
dt.add_day(4)
print(dt)
print(dt + 1) 
print(dt + 60) 
print(dt + 3600)
print(dt - 1) 
print(dt - 60) 
print(dt - 3600) 




#_____________________________________________________________________
#_____________________________________________________________________
#_____________________________________________________________________

class Money:

    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency
    
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value


    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value




    def __repr__(self):
        return f"{self.__amount} {self.__currency}"




    def convert(self, new_currency):
        exchange_rates = {'AMD': 1, 'EUR': 430, 'RUB': 5.8, 'USD':400}
        if self.__currency == new_currency:
            return Money(self.__amount, new_currency)
        else:
            new_amount = self.__amount * exchange_rates[new_currency] / exchange_rates[self.__currency]
            return Money(new_amount, new_currency)



    def __add__(self, another):
        if isinstance(another, Money) and self.__currency == another.__currency:
            return Money(self.__amount + another.__amount, self.__currency)
        else:
            raise ValueError("Cannot add two Money objects with different currencies")




    def __sub__(self, another):
        if self.__amount < another.__amount:
            raise ValueError("The amount of money in the first instance is smaller than the second one")
        if self.__currency != another.__currency:
            raise ValueError("Cannot sub two Money objects with different currencies")
        return Money(self.__amount - another.__amount, self.__currency)
    



    def __truediv__(self, another):
        if type(another.__amount) == int or type(another.__amount)== float:
            return Money(self.__amount / another.__amount, self.__currency)
        elif another == 0:
            raise ZeroDivisionError("Cannot divide by 0")



    
    def __eq__(self,another):
        if isinstance(another, Money):
            return self.__amount == another.__amount and self.__currency == another.__currency




    def __ne__(self,another):
        if isinstance(another, Money):
            return self.__amount != another.__amount or self.__currency != another.__currency




    def __lt__(self,another):
        if self.__currency == another.__currency:
            return self.__amount < another.__amount
        else:
            raise ValueError("Different currencies")




    def __gt__(self,another):
        if self.__currency == another.__currency:
            return self.__amount > another.__amount
        else:
            raise ValueError("Different currencies")



    def __le__(self,another):
        if self.__currency == another.__currency:
            return self.__amount <= another.__amount
        else:
            raise ValueError("Different currencies")



    
    def __ge__(self,another):
        if self.__currency == another.__currency:
            return self.__amount >= another.__amount
        else:
            raise ValueError("Different currencies")

class MoneyError(Exception):
    def __init__(self, error):
        self.error = error
    
    def __repr__(self):
        return self.error

money = Money(1,'AMD')
print(money)
print(money.amount)
print(money.currency)
new_money = money.convert('USD')
print(new_money)
another = Money(100,'AMD')
add = money + another
#sub = money - another
truediv = money / another
print(add.amount)
print(add.currency)
#print(sub.amount)
#print(sub.currency)
print(truediv.amount)
print(money == another)
print(money != another)
print(money< another)
print(money>another)
print(money<= another)
print(money>=another)

#_____________________________________________________________________
#_____________________________________________________________________
#_____________________________________________________________________


class MyRange:

    def __init__(self, end,step):
        self.current = 0
        self.step = step
        self.end = end

    
    def __repr__(self):
        return f"MyRange ends at {self.end} with {self.step} step"


    
    def __iter__(self):
        return self
    


    def __next__(self):
        if self.current>= self.end:
            raise StopIteration
        else:
            current = self.current
            self.current += self.step
            return current



    def __len__(self):
        return(self.end -1) // self.step+1




    def __getitem__(self, index):
        if index >= 0 and index < len(self):
            return index * self.step
    
    

    def __reversed__(self):
        start = self.end - self.step
        if start < 0:
            start = 0
        return MyRange(start, -self.step)
    
class MyRangeError(Exception):
    def __init__(self, error):
        self.error = error
    
    def __repr__(self):
        return self.error

range = MyRange(10,2)
print(repr(range))
new_list = []
for num in range:
    new_list.append(num)
print(new_list)
reversed_numbers = list(reversed(new_list))
print(reversed_numbers)
print(len(range))
print(range[3])


#_____________________________________________________________________
#_____________________________________________________________________
#_____________________________________________________________________



class Date:

    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day

        
    def __repr__(self):
        return f"{self.day}.{self.month}.{self.year} "    


    
    def is_leap_year(self):
        if self.year % 4 ==0 or self.year %400 == 0:
            return True 
        else: 
            return False



    def add_day(self, day):
        while day > 0:
            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                if self.day + day > 31:
                    day -= 31 - self.day + 1
                    self.day = 1
                    self.add_month(1)
                else:
                    self.day += day
                    day = 0
            elif self.month in [4, 6, 9, 11]:
                if self.day + day > 30:
                    day -= 30 - self.day + 1
                    self.day = 1
                    self.add_month(1)
                else:
                    self.day += day
                    day = 0
            else:
                if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
                    if self.day + day > 29:
                        day -= 29 - self.day + 1
                        self.day = 1
                        self.add_month(1)
                    else:
                        self.day += day
                        day = 0
                else:
                    if self.day + day > 28:
                        day -= 28 - self.day + 1
                        self.day = 1
                        self.add_month(1)
                    else:
                        self.day += day
                        day = 0
            
        
    def add_month(self, month):   
        self.month =self.month + month
        
        while self.month > 12:
            self.year +=1
            self.month -= 12        
        
    def add_year(self, year):
        self.year = self.year + year

date = Date(31,1,2000)
print(date)
date.add_day(30)
print(date)
#I fixed the error with Fubruary 30





class Company:
    
    def __init__(self, company_name, founded_at, employees_count) :
        self.name = company_name
        self.founded = founded_at
        self.employees_count = employees_count



    
    def __repr__(self):
        return f'({self.name},{self.founded},{self.employees_count})'




company = Company('ACA', 1980, 45) 



class Person:
    def __init__(self,name,surname,gender, age, address,friends,job):
        self.name = name
        self.surname = surname
        for gender in ['Male', 'Female']:
            self.gender = gender 
        self.age = age
        self.address = address
        self.friends = []
        self.job = []




    def __repr__(self):
        return f'Person(" {self.name},{self.surname},{self.gender},{self.age},{self.address},{self.friends},{self.job}")'



    def add_friend(self, new_friend) :
        return self.friends.append(new_friend)



    
    def remove_friend(self, friend):
        return self.friends.pop(friend)



    
    def add_job(self, job):
        self.job.append(job.position)
        company.employees_count += 1 
        



    def remove_job(self, job):
        self.job.pop(job)
        company.employees_count-=1
        return self.job



    
    def display_job(self):
        return self.job

#START

class Doctor(Person):
    def __init__(self,department, profession, patronymic, salary,name,surname,gender, age, address,friends,job):
        super().__init__(name,surname,gender, age, address,friends,job)
        self.__department = department
        self.__profession = profession
        self.__patronymic = patronymic
        self.__salary = salary
    


    def __repr__(self):
        return f"Department -> {self.department}\nProfession -> {self.profession}\nPatronymic -> {self.patronymic}\nSalary -> {self.salary}"



    @property
    def department(self):
        return self.__department
    
    @department.setter
    def department(self,value):
        self.__department = value
    
    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, value):
        self.__profession = value

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        self.__patronymic = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value



if __name__ == "__main__":
    doctor = Doctor("Urologist", "Orthodont", "Doctor Smith", 100000, "Vardan", "Vardanyan", "Male", 30, "Yerevan", ["Poxos", "Petros"], "Doctor")
    print(doctor)

    doctor.salary = 1000000
    print(doctor.salary)

    doctor.department = "Surgeon"
    print(doctor.department)

    doctor.patronymic = 'Mayisovna'
    print(doctor.patronymic)


class Doctor(Exception):
    def __init__(self, error):
        self.error = error
    
    def __repr__(self):
        return self.error





#_____________________________________________________________________
#_____________________________________________________________________
#_____________________________________________________________________

class City:
    def __init__(self, name,population, language, mayor:Person ):
        self.__name = name
        self.__population = population
        self.__language = language
        self.__mayor = mayor
    
    def __repr__(self):
        return f"The {self.__name} city with approxiamtely {self.__population} people has {self.__language} speaking community. The mayor of the town is the {self.__mayor}"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        self.__population = value

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value
    
    @property
    def mayor(self):
        return self.__mayor

    @mayor.setter
    def mayor(self, value):
        self.__mayor = value



class CityError(Exception):
    def __init__(self, error):
        self.error = error
    
    def __repr__(self):
        return self.error



mayor = Person("Poghos", "Poghosyan", "Male",24, "Lernagorts", ['Arthur'], 'mayor' )
city = City("Kajaran", 10000, "Armenian", "Poghos")
print(city)
print(city.name)
print(city.language)
print(city.population)
print(mayor.age)

#_____________________________________________________________________
#_____________________________________________________________________
#_____________________________________________________________________

class University:
    def __init__(self, name: str, founded_at: Date, rector:Person, city:City):
        self.__name = name
        self.__founded_at = founded_at
        self.__rector = rector
        self.__city = city 
    
    def __repr__(self):
        return f"The University of {self.__name} was founded at {self.__founded_at} in {self.__city}. Now the head of it is {self.__rector} "
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def founded_at(self):
        return self.__founded_at
    
    @founded_at.setter
    def founded_at(self,value):
        self.__founded_at = value
    
    @property
    def rector(self):
        return self.__rector
    
    @rector.setter
    def rector(self,value):
        self.__rector = value
    
    @property
    def city(self):
       return self.__city
    
    @city.setter
    def city(self,value):
        self.__city = value



class UniversityError(Exception):
    def __init__(self, error):
        self.error = error
    
    def __repr__(self):
        return self.error

uni = University("AUA", 2000, "Markides", "Yerevan")
print(uni)

#_____________________________________________________________________
#_____________________________________________________________________
#_____________________________________________________________________

class Teacher(Person):
    def __init__(self,name,surname,gender, age, address,friends,job, university: University, faculty: str, experience: int, start_work_at: Date, subject: str, salary: int):
        super().__init__(name,surname,gender, age, address,friends,job)
        self.university = university
        self.__faculty = faculty
        self.__experince = experience
        self.__start_work_at = start_work_at
        self.__salary = salary
        self.__subject = subject
    
    def __repr__(self):
        return f"The person is a {self.__faculty} {self.__subject} teacher who works since {self.__start_work_at}. The teacher has {self.__experince}  years of experince and works for {self.__salary}$ "

    @property
    def experience(self):
        return self.__experience
    
    @experience.setter
    def experience(self,value):
        self.__experience = value

    @property
    def started_work_at(self):
        return self.__start_work_at

    @started_work_at.setter
    def faculty(self,value):
        self.__start_work_at = value
    
    @property
    def subject(self):
        return self.__subject
    
    @subject.setter
    def subject(self,value):
        self.__subject = value
    
    @property
    def faculty(self):
        return self.__faculty
    
    @faculty.setter
    def faculty(self,value):
        self.__faculty = value
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,value):
        self.__salary = value


class TeacherError(Exception):
    def __init__(self, error):
        self.error = error
    
    def __repr__(self):
        return self.error



#salary = Money(100000, "AMD")
uni = University("AUA", 2000, "Markides", "Yerevan")
date = Date(5, 12, 2003)
city = City("Yerevan", 100000, 'armenian', "Poghos")
teacher = Teacher("Jane", "Doe", "Female", 45, "Adress", ["Alen"], 'Doctor', uni, "CSE", 10, date, "DATA STRUCTURES", 5000)
print(teacher)   

#_____________________________________________________________________
#_____________________________________________________________________
#_____________________________________________________________________

class Student(Person):
    def __init__(self,name,surname,gender, age, address,friends,job, university: University, faculty: str, course: int, started_at: Date):
        super().__init__(name,surname,gender, age, address,friends,job)
        self.__university = university
        self.__faculty = faculty
        self.__course = course
        self.__started_at = started_at
        
    
    def __repr__(self):
        return f"The person is a {self.__university} {self.__faculty} {self.__course} student who started studying in {self.__started_at}."

    @property
    def university(self):
        return self.__university
    
    @university.setter
    def experience(self,value):
        self.__university= value

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self,value):
        self.__faculty = value
    
    @property
    def course(self):
        return self.__course
    
    @course.setter
    def subject(self,value):
        self.__course = value
    
    @property
    def started_at(self):
        return self.__started_at
    
    @started_at.setter
    def faculty(self,value):
        self.__started_at = value

class StudentError(Exception):
    def __init__(self, error):
        self.error = error
    
    def __repr__(self):
        return self.error

date = Date(25, 8, 20)
student = Student('Ina', 'Karapetyan', 'Female', 19, 'Kajaran', ['Name'], 'internship', 'AUA', 'CSE', 'Data Science', date )
print(student)



#_____________________________________________________________________
#_____________________________________________________________________
#_____________________________________________________________________
def called(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        return result
    wrapper.count = 0
    return wrapper

@called
def add(money, another):
    return money + another