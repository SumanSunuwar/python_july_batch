#mode in filehandling : "w", "r", "a"

# files => naming => ef txt=> hdd, ssd,

# write- read- funtions(file function)

# operations with a file in python
# 1. open a file
# 2. read or write (performance in or with a file)
# 3. close the opened file

# f = open("test.txt", "r")
# print(f.read())
# f.close()

# try:
# 	f = open("test.txt", "w") #opeing a file 
# except FileNotFoundError:
# 	print("File doesnt exist!")
# else:
# 	print(f.write("This is test file.")) #> len of string passed in write method
# finally:
# 	f.close()

# try:
# 	f = open("demo.txt", "r") #opeing a file 
# except FileNotFoundError:
# 	print("File doesnt exist!")
# else:
# 	print(f.read())
# finally:
# 	f.close()

# try:
# 	f = open("test.txt", "r") #opeing a file 
# except FileNotFoundError:
# 	print("File doesnt exist!")
# else:
# 	print(f.readlines()[1])
# finally:
# 	f.close() 

