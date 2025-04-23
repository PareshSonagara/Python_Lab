source_file = "source.txt"
target_file = "target.txt"

src = open(source_file, 'r')
tgt = open(target_file, 'w')

for line in src:
    tgt.write(line.upper())

src.close()
tgt.close()

print("All lines converted to uppercase and saved to target.txt")
