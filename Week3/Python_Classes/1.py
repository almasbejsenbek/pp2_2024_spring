def uncia_to_gramm(uncia):
    gramm = uncia * 28.3495231
    return gramm

uncia_in_magazine = float(input())
gramms = uncia_to_gramm(uncia_in_magazine)

print("Grammy:", gramms)