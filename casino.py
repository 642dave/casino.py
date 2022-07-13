"""
HRA CASINO, STASTNYCH PET
AUTHOR: DAVID RAKOVSKY
STUDENT ENGETO ACADEMY
KURZ PYTHON  3.5.2022 - 26.7.2022
DISCORD: #9097
EMAIL: david.rakovsky@centrum.cz

Moje hra KASINO, STASTNYCH PET, je hazardni hra,
kdy muzes vyhrat svoji sazku uhodnutim jednoho z peti cisel

"""




import random


hra_bezi = True
oddelovac = "=" * 80

print(oddelovac)
print("VITEJ VE HRE CASINO,".center(len(oddelovac)))
print("STATNYCH PET".center(len(oddelovac)))
print("--Hru muzes kdykoliv ukoncit napsanim slova konec--".center(len(oddelovac)))
print(oddelovac)
tvoje_tipovana_cisla = list()
vylosovana_cisla_kasina = list()
tvoje_vyherni_cisla = list()
vyherni_cisla_kasina = list()

def osetri_uzivatelsky_vstup(text):
    # osetri uzivatelsky vstup proti prekliku nebo zadani neplatnych udaju, dale umozni kdykoliv hru ukoncit
    if text.lower() == "konec":
        print("Diky za hru, ukoncuji...")
        quit()
    if not text.isnumeric():
        print("Zadal jsi neplatne udaje, ukoncuji!".upper().center(len(oddelovac)))
        quit()


while hra_bezi:
    vklad = input("Zadej vklad, se kterym jsi ochoten hrat, max. 20000 $: ".upper().center(len(oddelovac)))
    osetri_uzivatelsky_vstup(vklad)
    print()
    if int(vklad) > 20000:
        print("Vyse Tveho vkladu neni povolena!".upper().center(len(oddelovac)))
    if 0 < int(vklad) <= 20000:
        while hra_bezi:
            sazka = input(f"Zadej svoji sazku, max. {vklad} $: ".upper().center(len(oddelovac)))
            osetri_uzivatelsky_vstup(sazka)
            print()
            if int(sazka) > int(vklad):
                print("Zadal jsi sazku, ktera je vyssi nez Tvuj aktualni vklad!".upper().center(len(oddelovac)))
            if 0 < int(sazka) <= int(vklad):
                while hra_bezi:
                    volba_cisla = input("***  Z a d e j  c i s l o  o d  1  d o  5  ***: ".upper().center(len(oddelovac)))
                    osetri_uzivatelsky_vstup(volba_cisla)
                    tvoje_tipovana_cisla.append(volba_cisla)
                    print()
                    if int(volba_cisla) > 5:
                        print("Zvolene cislo neni povoleno!".upper().center(len(oddelovac)))
                        continue
                    if 0 < int(volba_cisla) <= 5:
                        print(f"Zadal jsi sazku {sazka} $".upper().center(len(oddelovac)))
                        vylosovane_cislo = random.randint(1, 5)
                        print(f"Kasino zadalo sazku {sazka} $".upper().center(len(oddelovac)))
                        print(f"Zvolil jsi cislo {volba_cisla}".upper().center(len(oddelovac)))
                        print(f"Kasino vylosovalo cislo {vylosovane_cislo}".upper().center(len(oddelovac)))
                        vylosovana_cisla_kasina.append(vylosovane_cislo)
                        print()
                    if vylosovane_cislo == int(volba_cisla):
                        tvoje_vyherni_cisla.append(volba_cisla)
                        print()
                        print("***Gratulujeme, uhodl jsi vylosovane cislo!***".upper().center(len(oddelovac)))
                        tvoje_vyherni_cisla.append(volba_cisla)
                        print()
                        vklad = int(vklad) + int(sazka)
                        print(f"Tvuj vklad se navysil o tvoji vyhru {sazka} $".center(len(oddelovac)))
                        print(f"TVOJE TIPOVANA CISLA: {tvoje_tipovana_cisla}".center(len(oddelovac)))
                        print(f"TVOJE VYHERNI CISLA: {tvoje_vyherni_cisla}".center(len(oddelovac)))
                        print(f"VYLOSOVANA CISLA KASINA: {vylosovana_cisla_kasina}".center(len(oddelovac)))
                        print(f"VYHERNI CISLA KASINA: {vyherni_cisla_kasina}".center(len(oddelovac)))
                        print(f"STAV TVEHO KONTA JE AKTUALNE {vklad} $".center(len(oddelovac)))
                        print(oddelovac)
                        break
                    if vylosovane_cislo != int(volba_cisla):
                        vyherni_cisla_kasina.append(vylosovane_cislo)
                        print()
                        print("---Litujeme, neuhodl jsi vylosovane cislo!---".upper().center(len(oddelovac)))
                        print()
                        vklad = int(vklad) - int(sazka)
                        print(f"Tvuj vklad se ponizil o tvoji sazku {sazka} $".upper().center(len(oddelovac)))
                        print(f"TVOJE TIPOVANA CISLA: {tvoje_tipovana_cisla}".center(len(oddelovac)))
                        print(f"TVOJE VYHERNI CISLA: {tvoje_vyherni_cisla}".center(len(oddelovac)))
                        print(f"VYLOSOVANA CISLA KASINA: {vylosovana_cisla_kasina}".center(len(oddelovac)))
                        print(f"VYHERNI CISLA KASINA: {vyherni_cisla_kasina}".center(len(oddelovac)))
                        print(f"Stav Tveho konta je aktualne {vklad} $".upper().center(len(oddelovac)))
                        print(oddelovac)
                        if int(vklad) == 0:
                            print("Litujeme, ale na Tvem konte nemas jiz dostatek prostredku".upper().center(
                                len(oddelovac)))
                            print("Nemuzes pokracovat. diky za hru!".upper().center(len(oddelovac)))
                            print(oddelovac)
                            quit()
                        break


















