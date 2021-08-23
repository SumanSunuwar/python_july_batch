#function defined 
# def func():
# 	print("helloo python")

# #function executution
# func()

#lambda function:
#=> function without a name => anonymous
#=> called where defined => no need to define at one place and calling in another

#syntax;
# lambda param1, param2, param3,..... : return #code

# keyword : lambda
# varuables = params
# return is body
#eg

# adding = lambda x, y: x + y

# print(adding(5,2))


# print((lambda first_name, last_name : f"My name is {first_name} {last_name}")("john","doe"))

#higher order function

#interable obj => list = [1,2,3,4,5]

# map(function. iterable)  --> map object result return 

# numbers = [1,2,3,4,5] #iterable
# [3, 4, 5, 6, 7]

# def increment_by_two(val): #function
# 	return val + 2

# ans = list(map(increment_by_two, numbers))

# print(ans)
# iterable => function => map object
#finally type casting => list



# numbers = [1,2,3,4,5] #iterable


# # [3, 4, 5, 6, 7]


# inc_of_numbers = list(map(lambda val: val + 2, numbers ))


# namelist = ["ram","shyam","haru","sita","geeta"]

# res_namelist = ["RAM","SHYAM",..........]

# emails = ["abc@gmail.com","xyz@hotmail.com","test@outlook.com"]
#ans = ["gmail.com", "hotmail.com", "outlook.com"]


#filter function:
# map => iteration => map => return value => iteration set object
# filter => either true or false => value => iteration set object

#boolean return item => filter

# syntax:
# filter(function, iterable) => filter object


# def is_even(val):
# 	if val % 2 == 0:
# 		return True

# 	else:
# 		return False

#filter example

# numbers = [1,2,3,4,5]

# ans = list(filter(lambda x: x % 2 == 0, numbers))

# print(ans)

# emails = ["abc@gmail.com","xyz@hotmail.com","test@outlook.com","someone@gmail.com","me@yahoo.com","anyone@gmail.com"]
#ans = ["gmail.com"] => emails with only gmail.com

