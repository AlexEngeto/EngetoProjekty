"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Alexander Hlaváček
email: Alex.Hlavacek@volny.cz
discord: Alexander Hlaváček
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

oddelovac = "=" * 63

uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

uzivatel = input("Zadejte svůj login:\n")
heslo = input("Zadejte své heslo:\n")

print(oddelovac)

if {key: value for key, value in uzivatele.items() if key == uzivatel and value == heslo}:
    print("Vítáme Tě uživateli", uzivatel.capitalize(), "v analyzátoru textů.",)
else:
    print("Uživatel", uzivatel, "není registrován. Program byl ukončen")    
    exit()

print("V nabidce jsou k výběru celkem", len(TEXTS), "texty." )

print(oddelovac)

volba = input("Vyberte si text podle čísla mezi 1 a konečnou hodnotou nabídky:\n")
if not volba:
    print("Nevyplnli jste číslo. Program byl ukončen")   
    exit()
 
elif volba.isnumeric():
    volba = int(volba)
    if volba < 1 or volba > len(TEXTS):
        print("Číslo:", volba, "není v nabídce. Program byl ukončen!")
        exit()   
    else:
        vybrany_text = TEXTS[volba - 1]
else:
    print("Zadali jste neplatný vstup:", volba, "Program byl ukončen!")
    exit()

print(oddelovac)

rozdeleny_text = vybrany_text.split()
slova_bez_interpunkce = [slovo.strip(',.') for slovo in rozdeleny_text]
delky_slov = [len(slovo) for slovo in slova_bez_interpunkce]

slova_velkym = [slovo for slovo in slova_bez_interpunkce if slovo.istitle() and slovo.isalpha()]
slova_velkymi = [slovo for slovo in slova_bez_interpunkce if slovo.isupper() and slovo.isalpha()]
slova_malymi = [slovo for slovo in slova_bez_interpunkce if slovo.islower() and slovo.isalpha()]
cisla = [slovo for slovo in slova_bez_interpunkce if slovo.isnumeric()]
soucet_cisel = [int(number) for number in cisla]

print("V textu je", len(rozdeleny_text), "slov.")
print("V textu je", len(slova_velkym), "slov s velkým počátečním písmenem.")
print("V textu je", len(slova_velkymi), "slov s velkými písmeny.")
print("V textu je", len(slova_malymi), "slov s malými písmeny.")
print("V textu je", len(cisla), "číselných stringů.")
print("Součet všech číselných stringů je:", sum(soucet_cisel), ".")

print(oddelovac)

print(f"LEN | OCCURENCES | NR.")
print(oddelovac)
hvezda = '*'
mezera = ' '
sada_delky_slov = set(delky_slov)

vyskyt_delky_slova = []
for cislo in sada_delky_slov:
    vyskyt_delky_slova.append(delky_slov.count(cislo))
max_pocet = max(vyskyt_delky_slova)
for num in sada_delky_slov:
    pocet_mezer = max_pocet - delky_slov.count(num)
    print(f"{num} | {hvezda * delky_slov.count(num)} {mezera * pocet_mezer} | {delky_slov.count(num)}")
      