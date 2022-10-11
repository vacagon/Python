name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
file = open(name)
ddd = dict()
for lines in file:
    if not lines.startswith("From "): continue
    words = lines.split()
    ddd[words[5][:2]] = ddd.get(words[5][:2],0) + 1
lst = list()
for (k,v) in ddd.items():
    newtup = (k,v)
    lst.append(newtup)
lst = sorted(lst, reverse = False)
for k,v in lst:
    print(k,v)
