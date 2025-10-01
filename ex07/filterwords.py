
#syntax list comprehension
#newlist = [expression for item in iterable if condition == True]

import  sys

if (len(sys.argv) != 3):
    print("ERROR")
    sys.exit()
msg = sys.argv[1]
try:
    nb = int(sys.argv[2])
except ValueError:
    print("ERROR")
    sys.exit()
#print(msg, nb)
#mylist = [w for w in msg if len(w) >= nb]
mylist = msg.split()
for i in range(len(mylist)):
    mylist[i] = mylist[i].strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~.')
newlist = [w for w in mylist if len(w) > nb]
#print(mylist)
print(newlist)
