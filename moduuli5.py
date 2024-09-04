import random
arpakuutiot = int(input("Anna arpakuutioiden määrä? "))

summa = 0

for _ in range(arpakuutiot):
    silmäluku = random.randint(1, 6)
    summa += silmäluku

print(f"Arpakuutioiden silmälukujen summa on: {summa}")