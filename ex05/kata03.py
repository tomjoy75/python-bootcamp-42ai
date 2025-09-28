import  sys

kata = "The right format"
if (len(kata) > 42):
    print("Wrong size")
    sys.exit()
print("-" * (42 - len(kata)) + kata, end='')

