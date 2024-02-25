import re
string = "almab Aazhymukab anzhab Arsen Beibaryb azim Aresiib Balzhan Akniet aashinb"
f = r"\b[Aa]\S*?[Bb]\b"
pattern = re.findall(f, string)
print(pattern)