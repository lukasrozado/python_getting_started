fname = input("Enter File: ")
if len(fname) < 1 : fname = "clown.txt"
hand = open(fname)

di = dict()
#FOR EVERY LINE IN THE FILE
for line in hand:
    line = line.rstrip() #STRIP EVERY LINE
    words = line.rsplit() #SEPARETE WORDS
    #COUNT AND UPDATE WORDS
    for word in words:
        di[word] = di.get(word,0) + 1
#print(di)

#CREATES A LIST AND STORE THE VALUES IN IT.
temp = list()
for key, value in di.items():
    new_tuples = (value , key)
    temp.append(new_tuples)

#SORT THE LIST
temp = sorted(temp, reverse = True)
#TOP FIVE SORTED
#print("Sorted", temp[:5])

#LOOP TO ORGANIZE THE LIST AND PRINT OUT
for value, key in temp[:5]:
    print(value, key)