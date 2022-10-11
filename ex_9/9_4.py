name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
ddd = dict()
for lines in handle:
    if not lines.startswith("From: "): continue
    words = lines.split()
    ddd[words[1]] = ddd.get(words[1], 0) + 1
max_sender = None
max_num = None
for key,value in ddd.items():
    if max_num is None or value > max_num:
        max_num = value
        max_sender = key
print(max_sender,max_num)
