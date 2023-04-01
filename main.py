import os
from kartoteka.impl.Kartoteka import Kartoteka
from kartoteka.Osoba import Osoba


kartoteka = Kartoteka()

while True:
    print()
    print()

    print("Jaka czynnosc chcesz wykonac?")
    print("1. Dodaj osobe.")
    print("2. Usun osobe.")
    print("3. Wyswietl ilosc osob.")
    print("4. Sprawdz czy osoba istnieje.")
    print("5. Wyswietl osobe.")
    print("6. Zakoncz prace.")

    wybor = int(input("Wprowadz odpowiedni numer: "))
    os.system('cls')

    match wybor:
        case 1:
            imie = input("Wprowadz imie osoby: ")
            nazwisko = input("Wprowadz nazwisko osoby: ")
            osoba = Osoba(imie, nazwisko)
            kartoteka.dodaj(osoba)
        case 2:
            imie = input("Wprowadz imie osoby: ")
            nazwisko = input("Wprowadz nazwisko osoby: ")
            osoba = Osoba(imie, nazwisko)
            kartoteka.usun(osoba)
        case 3:
            print(kartoteka.rozmiar())
        case 4:
            imie = input("Wprowadz imie osoby: ")
            nazwisko = input("Wprowadz nazwisko osoby: ")
            osoba = Osoba(imie, nazwisko)
            print(kartoteka.czyZawiera(osoba))
        case 5:
            index = int(input("Wprowadz indeks osoby: "))
            osoba = kartoteka.pobierz(index)
            print(osoba.getImie() + " " + osoba.getNaziwsko())
        case 6:
            exit(0)