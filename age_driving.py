country = input("where are you from? ")
age = int(input("How old are you?"))
if country == "Korea":
	if age >= 18:
		print(" You are allowed to take driver license test")
	else:
		print("You are too young to take! Young man!")
elif country == "U.S.A":
	if age >= 16:
		print("Wow! you can take the test NOW!")
	else:
		print("Man! you're close to taking the exam! Be patient!")
else:
  print("Sytem Fail to indentify, Soooooorry!")