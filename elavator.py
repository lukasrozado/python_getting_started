#Convert elevator floors

try:
    inp = input("Europe floor? ")
except:
    inp = -1
us_floor = int(inp) + 1 #transform the string into a integer.
print("Us floor", us_floor)