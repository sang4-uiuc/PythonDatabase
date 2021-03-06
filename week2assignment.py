import sqlite3
import urllib

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'http://www.pythonlearn.com/code/mbox.txt'
fh = urllib.urlopen(fname)
for line in fh:
	if not line.startswith('From: ') : continue
	pieces = line.split()
	email = pieces[1]
	temp = email.split('@')
	org = temp[1]
	cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
	row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts (org, count) 
		VALUES ( ?, 1 )''', ( org, ) )
	else : 
		cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))
#cur.execute('SELECT * FROM Counts ORDER BY count')
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
	print str(row[0]), row[1]

cur.close()

