score = input("Enter Score: ")

try:
    sc = float(score)
except:
    print("Not a number")

if (sc >= 0.0) & (sc <= 1.0) :
    if sc >= 0.9 :
        print("A")
    elif sc >= 0.8 :
        print("B")
    elif sc >= 0.7 :
        print("C")
    elif sc >= 0.6 :
        print("D")
    else :
        print("F")
else :
    print("Value out of range")
