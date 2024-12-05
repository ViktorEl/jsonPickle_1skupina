import json

kamil = ['Kamil', 'Snaživý', 250]
lenka = ['Lenka', 'Múdra', 200]
odmeny = [kamil, lenka]

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(odmeny, f)

with open('data.json', 'r', encoding='utf-8') as f:
    nacitany = json.load(f)
    print(nacitany)