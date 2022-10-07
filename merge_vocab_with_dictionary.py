import csv
from dragonmapper import hanzi

# open the original vocab csv file
orig_contents = []
with open('vocab.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        orig_contents.append(row)

# open the dictionary csv file
dict_contents = []
with open('dict.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter='|')
    for row in csv_reader:
        dict_contents.append(row)

# match the only column of the vocab entries file with the first column of the dictionary file
matched = []

for i, orig_row in enumerate(orig_contents):
    print (f'{i/len(orig_contents):.2%}', end='\r')
    for dict_row in dict_contents:
        if orig_row[0] == dict_row[0]:
            matched.append([dict_row[0], hanzi.pinyin_to_zhuyin(dict_row[2]), dict_row[3]])

# write the matched entries to a new csv file
with open('merged.csv', 'w', encoding='utf-8') as f:
    csv_writer = csv.writer(f, delimiter='|')
    for row in matched:
        csv_writer.writerow(row)