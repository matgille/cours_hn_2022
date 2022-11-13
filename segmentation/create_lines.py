import sys
import random

text = sys.argv[1]

with open(text, "r") as input_text:
    text_as_list = input_text.read().split()

pas = 7
n = 0
while n < len(text_as_list):
    random_value = random.randint(-1, 3)
    if n + random_value < 10:
        pass
    else:
        text_as_list[n+random_value] += "\n"
        n += random_value
    n += pas

text_as_list = ' '.join(text_as_list).split("\n")
random.shuffle(text_as_list)


scaling = 0.8
limit = int(len(text_as_list) * scaling)
split = int((len(text_as_list)*scaling * 90) / 100)
print(len(text_as_list))
print(limit)
print(split)

with open("corpus/corpus_train.txt", "w") as output_file:
    output_string = '\n'.join(text_as_list[:split]).replace("\n ", "\n")
    output_file.write(output_string)

with open("corpus/corpus_test.txt", "w") as output_file:
    output_string = '\n'.join(text_as_list[split:limit]).replace("\n ", "\n")
    output_file.write(output_string)