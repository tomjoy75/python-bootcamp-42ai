import  sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    sys.exit()
if len(sys.argv) < 2:
    sys.exit()
try:
    arg = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
else:
    if arg == 0:
        print("I'm Zero.")
    elif arg % 2 != 0:
        print("I'm Odd.")
    else:
        print("I'm Even.")
