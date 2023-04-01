class Kartoteka:
    def __init__(self):
        self.__list = []

    def dodaj(self, osoba):
        self.__list.append(osoba)

    def usun(self, osoba):
        self.__list.pop(self.__list.index(osoba))

    def rozmiar(self):
        return len(self.__list)

    def czyZawiera(self, osoba):
        if osoba in self.__list:
            return True
        else:
            return False

    def pobierz(self, index=0):
        return self.__list[index]
