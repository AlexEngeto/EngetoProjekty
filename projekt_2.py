"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Alexander Hlaváček
email: Alex.Hlavacek@volny.cz
discord: Alexander Hlaváček
"""
import random
import time
import datetime
import csv
import os

oddelovac = "=" * 50

def generator_tajneho_cisla(delka=4):
    """Generuje náhodné tajné číslo o zadané délce, které nezačíná nulou."""
    cislice = list(range(10))
    tajne_cislo = []

    while len(tajne_cislo) < delka:
        random.shuffle(cislice)
        cislo = cislice.pop(0)
        if cislo != 0 or len(tajne_cislo) > 0:
            tajne_cislo.append(cislo)
    return ''.join(map(str, tajne_cislo))

def overeni_cisla(cislo, delka):
    """Kontroluje, zda je zadané číslo platné."""
    try:
        int(cislo)
        return len(cislo) == delka and len(set(cislo)) == delka and cislo[0] != '0'
    except ValueError:
        return False

def hraj_hru(delka=4):
    """Hlavní funkce hry."""
    tajne_cislo = generator_tajneho_cisla(delka)
    pokusy_uzivatele = 10
    start_time = time.time()

    print(">" * 22, "START", "<" * 21)

    print("*******Vítáme Vás ve hře >>>Bulls & Cows<<<*******")

    print(oddelovac)

    print('''Vygeneroval jsem pro vás náhodné čtyřmístné číslo.
         Hra Bulls and Cows může začít.'''
    )

    print(oddelovac)

    while pokusy_uzivatele > 0:
        print(f"Máte {pokusy_uzivatele} pokusů.")

        print(oddelovac)

        aktualni_hadani = input('''
Zadejte čtyřmístné číslo,
které nesmí obsahovat písmena,
duplicity jednotlivých číslic,
nesmí začínat '0'
a musí to být celé číslo:\n'''
    )

        print(oddelovac)

        nyni = datetime.datetime.now()
        datum = nyni.strftime("%Y-%m-%d %H:%M:%S")
        print(datum)

        # print("Generované číslo počítačem:", tajne_cislo)

        while not overeni_cisla(aktualni_hadani, delka):
            print("Neplatný vstup. Zadejte prosím", delka, "-místné číslo bez duplicit, které nezačíná nulou.")
            aktualni_hadani = input("Zadejte svůj tip: ")

        bulls = 0
        cows = 0
        for i in range(delka):
            if aktualni_hadani[i] == tajne_cislo[i]:
                bulls += 1
            elif aktualni_hadani[i] in tajne_cislo:
                cows += 1

        print(oddelovac)

        print(f"Bulls: {bulls} Cows: {cows}")

        print(oddelovac)

        stop_time = time.time()
        uplynula_doba = stop_time - start_time

        if bulls == delka:
            print(f"Vyhrál jste za: {uplynula_doba:.2f} sekund. Zbylo vám: {pokusy_uzivatele} pokusů")
            break
        pokusy_uzivatele -= 1

    if pokusy_uzivatele == 0:
        print(f"Prohrál jste. Hádané číslo bylo: {tajne_cislo} Doba trvání: {uplynula_doba:.2f} sekund")

    print(oddelovac)

    nyni = datetime.datetime.now()
    datum = nyni.strftime("%Y-%m-%d %H:%M:%S")
    print(datum)

    datum = time.time()
    cas = time.time()
    pocet_pokusu = pokusy_uzivatele

    hlavicky = ['Datum', 'Počet pokusů', 'Čas (s)']

    with open('statistiky hry.csv', 'a', newline='') as soubor:

        if os.path.getsize('statistiky hry.csv') == 0:
            writer = csv.writer(soubor)
            writer.writerow(hlavicky)
            writer.writerow([datum, pocet_pokusu, f"{uplynula_doba:.2f}"])
        else:
            writer = csv.writer(soubor)
            writer.writerow([datum, pocet_pokusu, f"{uplynula_doba:.2f}"])

    print("=" * 20, "KONEC HRY", "=" * 20)

    konec = input("Pro ukončení stiskněte: 'ENTER'") # Pro běh v terminálu Windows, možno vymazat! Prodlužuje čas.

if __name__ == "__main__":
    hraj_hru()
