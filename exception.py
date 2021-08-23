# exception handling:
# exception: error optain => program / application => prevent breaking
#> abrupt termintion => prevent
# simple example of error

# num1 = int(input("Enter any number : "))
# num2 = int(input("Enter second number: "))

# print("The sum of numbers you entered is: ",num1 + num2)

# print("Your caculation!!!")


# python exception handling use case:
#syntax:

# try:
# 	#code or statements in try block
# except:
# 	#executed when error is caught in try block
# except:
# 	#executed when error is caught in try block
# else:
# 	#if error doesnt occur in try block or if try block error-free
# finally:
# 	#whether error or not => finally exceutes
# 	#try except => exceute


	
# try:
# 	num1 = int(input("Enter any number : ")) #error
# 	num2 = int(input("Enter second number: ")) #error
# except ValueError as msg: #error cathcing => error message showable
# 	print(msg)
# else:
# 	print("The division of numbers you entered is: ",num1 / num2)

# print("This is outside the try/except blocks !!!")



# try:
# 	print("this is try block")
# 	num1 = int(input("Enter a number : "))
# 	num2 = int(input("Enter another number : "))
# 	div = num1 / num2
# except ZeroDivisionError:
# 	print("Division by zero is not acceptable")
# else:
# 	print("Division: ",div)
# finally:
# 	num1 = 0
# 	num2 = 0
# print("this is outside of exception handling blocks")
# print(num1, num2)

#next
#file handling : (mode => w, r , a)


