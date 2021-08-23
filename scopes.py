#global variable / local variable
#=> variable is always available in that block only

# name ="ram" #global variable

# def greet():
# 	name = "shyam" #local variable
# 	print("welcome",name)
	

# greet()


#int => immutable
#list = > mutable
# num = 5
# numbers = [1,2,3,4,5] #global variable

# def some_func():
# 	num = 10 #immutable => change 
# 	numbers.append(10) #mutable => change

# 	print(num, numbers)

# print(num, numbers)
# some_func()



# gobal scope function, local function


#global var/ local  var
#scopes


# def outer_func(n):
# 	def first_func():
# 		print("this is first function")
# 		return "first"
# 	def second_func():
# 		print("this is second function")
# 		return "second"

# 	if n == 1:
# 		return first_func #reference
# 	if n == 2:
# 		return second_func #reference

# first = outer_func(1) 
# second = outer_func(2)

# first()
# second()


# this is first function
# this is second function
# None None




# def outer_func():

# 	def inner_func():
# 		print("this is inner function")
# 	return inner_func

# res = outer_func() 
# res()







# def home(name):
# 	print(f"Welcome {name}")

# def login(func, user): #funct = greet, user = kiran
# 	admin = "kiran"
# 	if user == admin:
# 		func(user) # home("hari")
# 	else:

# 		func(user)
# 		print("you are not admin authenticated!!")
# login(home, "kiran") #function reference

# application => main funct => login===main_funct

#decorators=>
#functions are injected into func to execute

# def decorate_func(func):
# 	def wrapper():
# 		print("Printed before function calling")
# 		func()
# 		print("Printed after function calling")
# 	return wrapper


# def example():
# 	print("this is an example function")

# a = decorate_func(example)
# a()


#decorators