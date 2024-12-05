import json

def nacitaj_subor(nazov_suboru):
    with open(nazov_suboru, 'r', encoding='utf-8') as f:
        nacitany_subor = json.load(f)
        return nacitany_subor
    





data = nacitaj_subor('zoznam_faktury.json')