import sys
import unicodedata

with open("mapping.tsv", "r") as input_mapping:
    mapping = {line.replace("\n", "").split("\t")[0]: line.replace("\n", "").split("\t")[1] for line in
               input_mapping.readlines()}
    mapping = {unicodedata.normalize('NFC', key): unicodedata.normalize('NFC', value) for key, value in mapping.items()}

with open(sys.argv[1], "r") as input_file:
    file = input_file.read()
    file = unicodedata.normalize('NFC', file)

for orig, reg in mapping.items():
    file = file.replace(orig, reg)

with open(sys.argv[1].replace('.txt', '.normalized.txt'), "w") as output_file:
    output_file.write(file)
