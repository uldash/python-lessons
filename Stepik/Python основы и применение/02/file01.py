f = open('file01.txt', 'w')
f.write('Hello\n')
f.write('world')
f.close()

with open('file01.txt') as f, open('file01_copy.txt', 'w') as w:
    for line in f:
        w.write(line)
