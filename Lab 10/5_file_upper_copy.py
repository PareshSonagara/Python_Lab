
source_file = "source.txt"
target_file = "target.txt"

with open(source_file, 'r') as src, open(target_file, 'w') as tgt:
    for line in src:
        tgt.write(line.upper())
