# The basic outline of this problem is to read the file, look for integers 
# using the re.findall(), looking for a regular expression of '[0-9]+' and then
#  converting the extracted strings to integers and summing up the 
# integers.

#OPEN THE FILE AND PROTECTION THE ENTERING
import re
handle = open("regex_sum_1606605.txt")
num = 0

#FOR EVERY LINE IN THE FILE REORGANIZE AND FIND WHAT IT'S NEED IT
for line in handle:
    text = line.rstrip()
    numbers_search = re.findall("[0-9]+" , text)
    if not numbers_search:
        continue
    #TRANSFORM THE NUMBERS IN INTEGERS AND SUM THE VALUES
    for numbers_result in numbers_search:
        num = num + int(numbers_result)
        #print(numbers_result)
print(num)