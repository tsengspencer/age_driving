country = input("where are you from? ")
age = int(input("How old are you?"))
if country == "Korea":
	if age >= 18:
		print(" You are allowed to take driver license test")
	else:
		print("You are too young to take! Young man!")
