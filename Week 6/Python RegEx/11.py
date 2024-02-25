import re
import csv
f = open("row.txt", "r", encoding="utf8")
text = f.read()

pattern = r"\n(?P<Order>[0-9]+)\.\n(?P<Name>.+)\n(?P<Count>.+)x(?P<Price>.+)\n(?P<Cost>.+)\n"

results = re.finditer(pattern, text)

with open('data.csv', 'w', newline='', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Order', 'Name', 'Count', 'Price', 'Cost'])
    for x in results:
        writer.writerow(
        [x.group('Order'), 
        x.group('Name'), 
        x.group('Count'), 
        x.group('Price'), 
        x.group('Cost')]
        )