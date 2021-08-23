#login user=> existing user
#blog, buy product, upload post, image videos
#regiseter user=> new_user
#login=> multiple function

regisetered_users = [
	{"username":"suyog","password":"suyogsuyog"},
	{"username":"kiran","password":"kirankiran"},
	{"username":"jangbu","password":"jangbujangbu"}
]

print("------mindrisers admin-------")

while True:

	choice = int(input("""Enter your choice 
		1. For login
		2. For registration
		3. exit  """))
	if choice == 1:
		#login
		username = input("Enter username: ")
		pwd = input("Enter password: ")
		user = dict(username=username,password=pwd)
		if user in regisetered_users:
			print("Successfully logged in!")
		else:
			print("Sorry no such user!!")
	elif choice == 2:
		#register
		username = input("Set username: ")
		pwd = input("Set password: ")
		user = dict(username=username,password=pwd)
		if user in regisetered_users:
			print("sorry user already exists!!")
		else:
			regisetered_users.append(user)
			print("Successfully registered")
			print(f"users: {regisetered_users}")
	elif choice == 3:
		exit()

	else:
		print("Sorry invalid choice!!")
		

