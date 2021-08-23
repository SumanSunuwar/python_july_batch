#encapsulation in python class:
# eg => capsule => layer (inside content- hide)
# eg => tv_remote => button are shown => inside things (hidden)

#concept in all programming
#class in itself is also encapsulation
#access modifier(public, protected, private)
# #puclically accesable
# class Student:

# 	scl_name = "abc"

# 	def __init__(self, name):
# 		self.name = name

# 	def study(self):
# 		print("is studying.")


# s1 = Student("ram")

# print(s1.name)






#private memebers




# class Student:

# 	def __init__(self,name,age,):
# 		self.__name = name #private instance attribute(_Student__name => name mangaling)
# 		self.age = age #public instance
# 		self._guardian = guardian #protected



# 	def student_detail(self):
# 		print(f"Student name: {self.name}")
# 		print(f"Student age: {self.age}")


# class Teacher:


# st1 = Student("David",25, "Chriss")

# #accessing data
# print(st1.__dict__)


#python private and protected (only followed by convention strictly)


#access modifier(public, protected, private members)
# accessor(getter) and mutator(setter)
#property , staticmethod, classmethod
# class Student:
# 	def __init__(self, name, password):

# 		self._username = name
# 		self.__password = password

# 	#getter function (accessor)
# 	def get_username(self):
# 		return self._username

# 	#setter function
# 	def set_password(self, newpassword):
# 		if len(newpassword) < 8:
# 			print("length of password should be greater than 8")
# 		else:
# 			self.__password = newpassword



# st1 = Student("Luke","luke123") #instantiate obj
# print(st1.__dict__)

# # print(st1.get_username())

# st1.set_password("duke1245")
# print(st1.__dict__)


# {'_username': 'Luke', '_Student__password': 'luke123'}
# {'_username': 'Luke', '_Student__password': 'duke1245'}


# {'_username': 'Luke', '_Student__password': 'luke123'}
# length of password should be greater than 8
# {'_username': 'Luke', '_Student__password': 'luke123'}


#property :

# class Product:
# 	def __init__(self, brand, price):
# 		self.brand = brand
# 		self.__price = price 

# 	@property
# 	def price(self):
# 		return self.__price

# 	@price.setter
# 	def price(self, newPrice):
# 		if newPrice <= 0:
# 			print("Cannot set price below zero!")
# 		else:
# 			self.__price = newPrice


# pd1 = Product("apple", 50000)
# print(pd1.__dict__)

# pd1.price = 100000

# print(pd1.__dict__)

#getter/setter

# @classmethod, @staticmethod 

#classemethod

# called using ClassName.MethodName()
# method in a class , first param = class itself
# classmethod can return an object of class
# classmethod can only access the class atttributes but not the instance attritute

# from datetime import date

# class Student:
# 	#initializer method
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age



# 	#classmethod
# 	@classmethod
# 	def birthyear(cls,name, yob):
# 		print(f"nameAttribute: {cls.name}")
# 		return cls(name, (date.today().month - yob))
# 	#	retrun Student(name, age) => new instance created


# st1 = Student("Ram", 20)
# print(st1.__dict__)

# st2 = Student.birthyear("shyam", 1995)
# print(st2.__dict__)

# {'name': 'Ram', 'age': 20}
# {'name': 'shyam', 'age': 26}


#staticmethod
#declared inside class
#cannot have cls or self parameter


# def is_even(num):
# 	return num % 2 == 0


# class Calculator:


# 	def __init__(self,num1, num2):
# 		self.num1 = num1
# 		self.num2 = num2

	# def add(self):
	# 	if Calculator.is_even(num1):
	# 		return self.num1 + self.num2

# 	def sub(self):
# 		return self.num1 - self.num2

# 	@staticmethod
# 	def is_even(num):
# 		return num % 2 == 0




# calc = Calculator(20, 15) 


# print(Calculator.is_even(20))











