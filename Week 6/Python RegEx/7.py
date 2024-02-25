import re
string = "Almab_aazhymukab_anzhab_arsen_aeibaryb_azim_aresiib_balzhan_akniet_aashinb"
x = re.sub(r'_\w', lambda match: match.group(0).replace('_', '').upper(), string)
print(x)
