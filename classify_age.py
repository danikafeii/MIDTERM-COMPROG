def classify_age():
	age = int(input("What is your age: "))

	if age < 0:
    		print("Invalid input, try again.")
	elif age < 12:
    		print("You're a child.")
	elif age < 19:
    		print("You're a teenager.")
	elif age < 64:
    		print("You're an adult.")
	else:
    		print("You're a senior.")
    
classify_age()