num = 0 
total = 0.0
while True :
    user_input = input("Enter a number: ")
    if user_input == ("done"):
        break
    try:
        float_value = float(user_input)
    except:
        print("Invalid Input")
        continue
    #print(user_input)
    num = num + 1
    total = total + float_value
#print("All Done")
print(total, num, total/num)