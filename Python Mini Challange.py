#Python Mini Challange

#1 Write a function that returns the maximum of two numbers.

def max(num1, num2):
	if num1 > num2:
		return num1
	else:
		return num2

#2 Write a function called fizz_buzz that takes a number.

    # If the number is divisible by 3, it should return “Fizz”.
    # If it is divisible by 5, it should return “Buzz”.
    # If it is divisible by both 3 and 5, it should return “FizzBuzz”.
    # Otherwise, it should return the same number.

def fizz_buzz(x):
	if int(x)%3 == 0 and int(x)%5 == 0:
		return "FizzBuzz"
	elif int(x)%3 == 0:
		return "Fizz"
	elif int(x)%5 == 0:
		return "Buzz"
	else:
		return x

#3 Write a function for checking the speed of drivers. This function should have one parameter: speed.

    #a. If speed is less than 70, it should print “Ok”.
    #b. Otherwise, for every 5km above the speed limit (70), it should give the 
    #	driver one demerit point and print the total number of demerit points. 
    #	For example, if the speed is 80, it should print: “Points: 2”.
    #c. If the driver gets more than 12 points, the function should print: “License suspended”

def speed_check(speed):
	spood = int(speed)

	if spood < 70:
		return("Ok")
	else:
		points = (spood - 70) // 5
		if points > 12:
			return("License suspended")
		else:
			return f"points: {points}"


#4 	Write a function called showNumbers that takes a parameter
 # 	called limit. It should print all the numbers between 0 and limit with a 
 #	label to identify the even and odd numbers. For example, if the limit is 3, it 
 #	should print:

  	#   0 EVEN
  	#   1 ODD
  	#   2 EVEN
  	#   3 ODD


def show_numbers(limit):
	for x in range(limit + 1)
		if x%2 == 1:
			return f"{x} ODD" 
		else:
			return f"{x} EVEN"

def show_numbers(limit):#never a good idea to put "print" on a function
	for x in range(limit + 1):
		if x%2 == 1:
			print(f"{x} ODD")
		else:
			print(f"{x} EVEN")

#5 	Write a function that returns the sum of multiples of 3 and 5 between 0 
# 	and limit (parameter). For example, if limit is 20, it should return the sum 
# 	of 3, 5, 6, 9, 10, 12, 15, 18, 20.

#6 Write a function called show_stars(rows). If rows is 5, it should print the following: 

    # *
    # **
    # ***
    # ****
    # *****

def show_stars(rows):
    for x in range(rows):
        print()
        for y in range(x):
            print("*", end ="")

#7 Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.

def primy(limit):
	if limit > 1:
		for x in range(2, limit + 1):
			for y in range(2, x):
				if (num%y) == 0:
					break
			else:
				print(limit)

