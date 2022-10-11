hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Hourly rate:")
r = float(rate)
pay = 0.0
if h<=40 :
    pay = h*r
else:
    pay = 40*r + (h-40)*1.5*r

print(pay)
