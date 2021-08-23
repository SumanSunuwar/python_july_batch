#inhjeritance => 
#characteristics or behaviour from parent class tranferring to child
#Father = properties seen in son/

# Father class => height, weight, work(), walk(), run()
# son class=> inherited from father + study()


# class Parent: #parent class 
# 	def __init__(self, name):
# 		self.name = name

# 	#behaviour
# 	def work(self):
# 		return f"{self.name} is working."


# class Child(Parent): #child class
# 	pass


# ch1 = Child("Nick") #instance of child

# print(ch1.work()) #method invoke


# Nick is working
#type :
# single inheritance
# multiple inheritance
# multi level inheritance
# hybrid inheritance

# polymorphism => many forms


#overloading/ overriding

# class Product:
# 	def __init__(self, brand, price):
# 		self.brand = brand
# 		self.price = price

# 	# == #operator overloading
# 	# def __eq__(self, obj):
# 	# 	return self.price == obj.price
# 	def __add__(self,obj):
# 		return self.price + obj.price


# p1 = Product("Nokia",5000)#intantiate object(insatance)
# print("Initial Price(nokia): ",p1.price)
# p2 = Product("Samsung",5000)
# print("Initial Price(samsung): ",p2.price)

# print(p1 + p2) 


# single inheritance:

#parent class for digital and physical classes
# class Product:
# 	def __init__(self, brand, price):
# 		self.brand = brand
# 		self.price = price

# 	def buy(self):
# 		return (f"{self.brand} is on sale")


# #subclass / child class for product class
# class Digital_product(Product):#single inheritance
# 	def __init__(self,brand,price,name):
# 		super().__init__(brand,price)
# 		self.name = name

# 	#overiding class method
# 	def buy(self): #re difine inherited method
# 		print(super().buy())
# 		return (f"{self.name} is also for free")


# class Physical_Product(Product):#sinlge inheritance
# 	pass


# d1 = Digital_product("Photosonic",5000,"Monalisa_canvas")
# p1 = Physical_Product("Apple",1000)

# print(d1.buy()) #> different behave
# print(p1.buy()) #> different behave


# Monalisa_canvas is for free
# Apple is on sale


#polymorphism 

# 5 + 5 > 10
# "five"+"five" > "fivefive" => object => special method
# [1,2,3,4] + [5,6,7] > [1,2,3,4,5,6,7]

#multi level inheritance/ multiple inheritance
#parent class for father/grand parent class for student
# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def walk(self):
# 		print(self.name, "is walking in person class")

# #parent class for student
# class Father(Person):
# 	def __init__(self,name,age):
# 		super().__init__(name,age)

# 	def work(self):
# 		print(self.name, "is working in father class")
# #grand child class for person,

# #multi level inheritance
# class Student(Father):
	
# 	def work(self):
# 		print(self.name, "is working is the Student class")


# st1 = Student("ram",20)
# print(st1.__dict__)
# st1.work()
# st1.walk()


#multiple inheritance:

# class Person:
# 	def __init__(self, name , age):
# 		self.name = name
# 		self.age = age

# 	def walk(self):
# 		return f"{self.name} is walking in the person class"

# class Father(Person):

# 	def work(self):
# 		return f"{self.name} is working in the father class"

# 	#override -> parent run and chile class
# 	def walk(self):
# 		return "Walking in the father class"

# class Mother(Person):

# 	def cook(self):
# 		return f"{self.name} is cooking in the mother class"


# 	def walk(self):
# 		return "Walking in the mother class"


# #multiple inheritance/multi level(hybrid inheritance)
# class Student(Mother, Father): #=> person as grand parent inherit
# 	pass
	






# st1 = Student("ram",20)

# print(st1.walk())
# print(st1.work())
# print(st1.cook())
# print(st1.mro())

# ram is walking in the person class
# this is father walking
# ram is working in the father class
# ram is cooking in the mother class


