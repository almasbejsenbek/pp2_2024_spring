
f = rimport re
capitals = "CanberraBrasiliaOttawaBeijingParisBerlinNewdelhiJakartaRomeTokyoMexicoCityAmsterdamMoscowRiyadhSeoulAnkaraKievAbujaLagosLondon"'[A-Z][a-z]*'
x = re.findall(f, capitals)
print(x)