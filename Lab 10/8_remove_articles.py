infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')

for line in infile:
    for word in [' a ', ' the ', ' an ']:
        line = line.replace(word, ' ')
    outfile.write(line)

infile.close()
outfile.close()
