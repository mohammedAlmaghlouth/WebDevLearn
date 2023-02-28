import sys
try:
    print(5/0)
except ZeroDivisionError:
    print("stupid")
    sys.exit
