class Osoba:
    def __init__(self, imie, nazwisko):
        self.__imie = imie
        self.__nazwisko = nazwisko

    def __eq__(self, other):
        return self.__imie == other.__imie and self.__nazwisko == other.__nazwisko

    def getImie(self):
        return self.__imie

    def getNaziwsko(self):
        return self.__nazwisko
