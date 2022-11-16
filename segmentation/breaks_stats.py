import glob
import sys
import re

import stats

directory = sys.argv[1]
input_string = ""
input_orig_string = ""
for file in glob.glob(f"{directory}/*.normalized.tokenized.txt"):
    with open(file, "r") as input_file:
        input_string += input_file.read()
    with open(file.replace(".normalized.tokenized.txt", ".txt"), "r") as input_orig_file:
        input_orig_string += input_orig_file.read()
    print(file)
    input_orig_per_lines = input_orig_string.split('\n')
    print(f"Mean number of spaces: {stats.mean([line.count(' ') for line in input_orig_per_lines])}")

# On ne garde que les lignes entières car la justification fonctionne surtout sur celles-ci.
orig_reg_mapping = {orig: reg for orig, reg in zip(input_orig_string.split("\n"), input_string.split("\n")) if len(orig) > 40}

line_breaks = input_string.count("\n")
orig_hyphens = input_string.count("⸗")
hyphens = len(re.findall("[⸗-]\n", string=input_string))
correct_hyphens = len(re.findall("⸗-\n", string=input_string))
non_indicated_hyphens = len(re.findall(r'[^⸗]-\n', string=input_string))

mean_length = round(stats.mean([len(orig) for orig, reg in orig_reg_mapping.items()]), 2)

mean_length_with_hyphen = round(stats.mean([len(orig) - 1 for orig, reg in orig_reg_mapping.items() if "⸗" in orig]), 2)
median_length_with_hyphen = round(stats.median([len(orig) - 1 for orig, reg in orig_reg_mapping.items() if "⸗" in orig]), 2)


mean_length_with_reg_hyphen = round(stats.mean(
    [len(orig) for orig, reg in orig_reg_mapping.items() if len(re.findall(r'[^⸗]-', string=reg)) == 1]), 2)


median_length_with_reg_hyphen = round(stats.median(
    [len(orig) for orig, reg in orig_reg_mapping.items() if len(re.findall(r'[^⸗]-', string=reg)) == 1]), 2)


mean_length_with_no_hyphen = round(stats.mean(
    [len(orig) for orig, reg in orig_reg_mapping.items() if re.search(r'[⸗-]', string=reg) is None]), 2)

median_length_with_no_hyphen = round(stats.median(
    [len(orig) for orig, reg in orig_reg_mapping.items() if re.search(r'[⸗-]', string=reg) is None]), 2)


print(f"Nombre de lignes & {line_breaks}\\\\\hline")
print(f"Nombre de césures 'correctes' & {hyphens}\\\\\hline")
print(f"Nombre de césures marquées (⸗) & {orig_hyphens}\\\\\hline")
print(f"Nombre de césures 'correctes' marquées (⸗) & {correct_hyphens}\\\\\hline")
print(f"Nombre de césures non marquées & {non_indicated_hyphens}\\\\\hline")
print(f"Longueur moyenne de la ligne & {mean_length}\\\\\hline")
print(f"Longueur moyenne des lignes sans césure & {mean_length_with_no_hyphen}\\\\\hline")
print(f"Longueur moyenne des lignes avec césure marquée & {mean_length_with_hyphen}\\\\\hline")
print(f"Longueur moyenne des lignes avec césure non marquée & {mean_length_with_reg_hyphen}\\\\\hline")
print(f"Longueur médiane des lignes avec césure marquée & {median_length_with_hyphen}\\\\\hline")
print(f"Longueur médiane des lignes avec césure non marquée & {median_length_with_reg_hyphen}\\\\\hline")
