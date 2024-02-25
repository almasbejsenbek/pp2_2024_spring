import re
capitals = "CanberraBrasiliaOttawaBeijingParisBerlinNewdelhiJakartaRomeTokyoMexicoCityAmsterdamMoscowRiyadhSeoulAnkaraKievAbujaLagosLondon"
f = r'[A-Z][a-z]*'
x = re.findall(f, capitals)
print(x)