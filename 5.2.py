luvut = []

while True:
    syote = input("Anna luku (tai paina Enter lopettaaksesi): ")

    if syote == "":
        break

    luvut.append(int(syote))

luvut.sort(reverse=True)

print("Viisi suurinta lukua ovat: ")
for luku in luvut[:5]:
    print(luku)