import sys

def ispunctuation(char):
    if char.isprintable() and not char.isalnum() and not char.isspace():
        return True
    return False

def text_analyzer(msg = None):
    """ 
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if msg == None :
        print("What is the text to analyze?")
        msg = input(">> ")
    counts = {
            "printable": 0,
            "upper": 0,
            "lower": 0,
            "punctuation": 0,
            "space": 0
            }
#    li = [0,0,0,0,0]
    if not isinstance(msg, str):
        print("AssertionError: argument is not a string")
        sys.exit()
    for char in msg:
        if char.isprintable():
            counts["printable"] += 1
        if char.isupper():
            counts["upper"] += 1
        if char.islower():
            counts["lower"] += 1
        if ispunctuation(char):
            counts["punctuation"] += 1
        if char.isspace():
            counts["space"] += 1
    print(f"The text contains {counts['printable']} printable character(s):")
    print(f"- {counts['upper']} upper letter(s)")
    print(f"- {counts['lower']} lower letter(s)")
    print(f"- {counts['punctuation']} punctuation mark(s)")
    print(f"- {counts['space']} space(s)")

def main(argv):
    if len(argv) > 2:
        print("AssertionError: too many arguments")
        sys.exit()
    if len(argv) == 1:
        text_analyzer()
    else:
        text_analyzer(argv[1])

if __name__=='__main__':
    main(sys.argv)
