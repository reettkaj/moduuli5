kaupungit = []

for i in range(5):
    kaupunki = input(f"Anna {i+1}. kaupungin nimi: ")
    kaupungit.append(kaupunki)

print("\nSyöttämäsi kaupungit olivat:")
for kaupunki in kaupungit:
    print(kaupunki)