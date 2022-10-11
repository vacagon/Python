def computepay(hour, rate):
    pay = 0
    if hour <= 40 :
        pay = hour*rate
    else :
        pay = 40*rate + (hour-40)*1.5*rate
    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate: ")
r = float(rate)
p = computepay(h, r)
print("Pay", p)
