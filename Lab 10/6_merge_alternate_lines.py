f1 = open('file1.txt')
f2 = open('file2.txt')
out = open('merged.txt', 'w')

lines1 = f1.readlines()
lines2 = f2.readlines()

for l1, l2 in zip(lines1, lines2):
    out.write(l1)
    out.write(l2)

if len(lines1) > len(lines2):
    for extra in lines1[len(lines2):]:
        out.write(extra)
else:
    for extra in lines2[len(lines1):]:
        out.write(extra)

f1.close()
f2.close()
out.close()
