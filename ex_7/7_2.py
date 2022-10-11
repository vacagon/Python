def find_number(str):
    x = 0.0
    i = str.find('0')
    x = float(str[i:])
    return x

fname = input("Enter file name: ")
fh = open(fname)
avrg = 0.0
i = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    i = i+1
    avrg = avrg + find_number(line.strip())
print("Average spam confidence:", avrg/float(i))
