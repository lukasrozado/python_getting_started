#10.2 Write a program to read through the mbox-short.txt and figure out the 
# distribution by hour of the day for each of the messages. You can pull 
# the hour out from the 'From ' line by finding the time and then splitting 
# the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, 
# sorted by hour as shown below.

#OPEN THE FILE AND PROTECTION THE ENTERING
fname = input("Enter file:")
if len(fname) < 1:
    name = "mbox-short.txt"
handle = open(fname)


di = dict()
count = 0
#FOR EVERY LINE IN THE FILE REORGANIZE AND FIND WHAT IT'S NEED IT
for line in handle:
    text = line.rstrip()
    if not text.startswith("From"):
        continue
    text = line.split()
    text = text[5:6]
    #FOR EVERY WORDS SPLIT THEM AND STORE IN THE DICTIONARY AND COUNT
    for words in text:
        words = words[:2]
        di[words] = di.get(words,0)+1
        #print("First Version",words)
# SORT THE VALUE AND SHOW THE RESULT IN KEY AND VALUE
for key, value in sorted(di.items()):
    print (key, value)

