#3.1  Write a program to prompt the user for hours and rate per hour using 
# input to compute gross pay. Pay the hourly rate for the hours up to 40 
# and 1.5 times the hourly rate for all hours worked above 40 hours. Use 
# 45 hours and a rate of 10.50 per hour to test the program (the pay should 
# be 498.75). You should use input to read a string and float() to convert 
# the string to a number. Do not worry about error checking the user input - 
# assume the user types numbers properly.

def computepay(hour,rating):
	if hour > 40:
		regular = rating * hour
		overtime = (hour - 40.0) * (rating * 0.5)
		result_time = regular + overtime
	else:
		result_time = hours * rate
	return result_time

hours_ask = input("Enter hours: ")
rate_ask = input("Enter rate: ")
hours = float(hours_ask)
rate = float(rate_ask)
result_time = computepay(hours, rate)
print("Pay:", result_time)
