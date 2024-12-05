import pickle
# serializácia
#evidencia odmien
kamil = ['Kamil', 'Snaživý', 250]
lenka = ['Lenka', 'Múdra', 200]
odmeny = [kamil, lenka]
with open('odmeny.dat', 'wb') as f:
 pickle.dump(odmeny, f)
