import urllib


fname = raw_input('Enter file name: ')
if  len(fname) < 1  : fname = 'http://www.pythonlearn.com/code/mbox-short.txt'
print fname
fh = urllib.urlopen(fname)
data = fh.read()

for line in data:
	if not 'From: ' in line : continue
	pieces = line.split()
	email = pieces[1]
	print email
	#temp = email.split('@')
	#org = temp[1]
	#print org
