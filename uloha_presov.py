import json

def nacitaj_subor(nazov_suboru):
    with open(nazov_suboru, 'r', encoding='utf-8') as f:
        nacitany_subor = json.load(f)
        return nacitany_subor
    

def dodavatelia(data):
    novy_slovnik = {}
    for slovnik in data:
        dodavatel = slovnik['Dodávateľ']
        suma = slovnik['Celková_cena']
        suma = suma.replace(',', '.')
        suma = suma.replace(' ', '')
        suma = float(suma)
        if dodavatel in novy_slovnik:
            novy_slovnik[dodavatel] += suma
        else:
            novy_slovnik[dodavatel] = suma
    return novy_slovnik
    

def najvacsi_dodavatel(dodavatelia):
    najvacsi = ''
    najvacsia_suma = 0
    for dodavatel, suma in dodavatelia.items():
        if suma > najvacsia_suma:
            najvacsia_suma = suma
            najvacsi = dodavatel
    return najvacsi, najvacsia_suma


data = nacitaj_subor('zoznam_faktury.json')
slovnik_dodavatelov = dodavatelia(data)
print(najvacsi_dodavatel(slovnik_dodavatelov))