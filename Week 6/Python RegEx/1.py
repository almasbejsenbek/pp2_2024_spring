import re
string = "semle a ab abbb aaabbb abababa"
x = re.findall("a{1}b*", string)
print(x)