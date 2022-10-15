import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = str(pieces[1])
    extension = re.findall('@(\w*.\w*.\w*)',email)
    extension = str(extension[0])
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (extension,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                        VALUES (?, 1)''', (extension,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (extension,))
conn.commit()
cur.execute('SELECT * FROM Counts ORDER BY count DESC')
table = cur.fetchall()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
conn.commit()

for r in table:
    cur.execute('INSERT INTO Counts(org, count) VALUES (?, ?)', (r[0], r[1]))
conn.commit()
# https://www.sqlite.org/lang_select.html
#sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
#for row in cur.execute(sqlstr):

#row = cur.fetchone()
#print(row)
#conn.commit()
cur.close()
