import pickle
with open('odmeny.dat', 'rb') as f:
 nacitany_subor = pickle.load(f)
 print(nacitany_subor)
