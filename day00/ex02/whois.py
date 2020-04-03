import sys

if len(sys.argv) > 1:
    if not sys.argv[1].isdigit():
        print("ERROR")
    elif int(sys.argv[1]) == 0:
        print("I'm Zero.")
    elif int(sys.argv[1]) % 2:
        print("I'm Odd.")
    else:
        print("I'm Even.")
