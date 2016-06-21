import urllib


fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'http://www.pythonlearn.com/code/mbox.txt'
fh = urllib.urlopen(fname).read()
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    temp = email.split('@')
    org = temp[1]
print org
