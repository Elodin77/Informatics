a = open('addin.txt', 'r').readline()
b, c = a.split()
b = int(b)
c = int(c)
out = open('addout.txt', 'w').write(str(c + b))