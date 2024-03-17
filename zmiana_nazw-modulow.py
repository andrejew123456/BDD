
import os

# Zakładając, że masz pliki od slajd1.py do slajd5.py
# i chcesz zmienić ich nazwy na slajd2.py do slajd6.py
for i in range(36, 25, -1):
    print(i)
    # print(os.getcwd())
    stara_nazwa = f'features\slajd_{i}.feature'
    nowa_nazwa = f'features\slajd_{i+1}.feature'
    print(stara_nazwa, nowa_nazwa)
    os.rename(stara_nazwa, nowa_nazwa)