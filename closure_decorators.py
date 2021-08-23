# #simple closure

# def multiplier(n):
# 	def times(a):
# 		return a * n
# 	return times

# times5 = multiplier(5)
# times4 = multiplier(4)
# print(times5(10)) 
# print(times4(100))

# # nonlocal variable / nested function

# decorators:

# def decorate_func(func):
# 	def wrapper():
# 		print("Printed before function calling")
# 		print(func)
# 		func()
# 		print("Printed after function calling")
# 	return wrapper

# @decorate_func
# def example():
# 	print("this is an example function")

# print(example)
# example()

# Printed before function calling
# this is an example function
# Printed after function calling

# <function decorate_func.<locals>.wrapper at 0x000001C57AC55040>
# Printed before function calling
# <function example at 0x000001C57AC4CF70>
# this is an example function
# Printed after function calling



#simple example

# def division(divident, divisor):
# 	return divident / divisor


# print(division(100, 5))
# print(division(100, 0))

# def smart_divsion(div): # decorator => parma=> function
# 	def wrapper(divident, divisor):
# 		if divisor == 0:
# 			return "Can not divide by zero!!"
# 		else:
# 			return div(divident, divisor)

# 	return wrapper



# @smart_divsion
# def division(divident, divisor): #> referencing wrapper
# 	return divident / divisor

# print(division(100, 5))
# print(division(100, 0))

# # 20.0
# Can not divide by zero!!

# def login_required(func):
# 	def wrapper(user):
# 		admin = "ram"
# 		if user == admin:
# 			return func(user)
# 		else:
# 			return f"sorry {user} is not authenicated for this view"


# def product_view(user):
# 	print(f"welcome {user}")
# 	print("list of products:")

# @login_required
# def sale_report_view(user):
# 	print(f"welcome {user}")
# 	print("showing sales report")

# @login_required
# def price_history(user):
# 	print(f"welcome {user}")
# 	print("showing price history")

# print(product_view("hari"))
# print(sale_report_view("ram"))
# print(price_history("ram"))

