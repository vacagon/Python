largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        x = int(num)
        if largest is None:
            largest = x
        if smallest is None:
            smallest = x
        if largest < x:
            largest = x
        if smallest > x:
            smallest = x
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
