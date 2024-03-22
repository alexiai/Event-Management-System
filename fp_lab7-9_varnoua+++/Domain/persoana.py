class Persoana:
    def __init__(self,personID,nume,adresa):
        self.__personID = personID
        self.__nume = nume
        self.__adresa = adresa

    def get_personID(self):
        return self.__personID

    def get_nume(self):
        return self.__nume

    def get_adresa(self):
        return self.__adresa

    def set_nume(self,nume):
        self.__nume = nume

    def set_adresa(self,adresa):
        self.__adresa = adresa

    def __eq__(self, other):
        if isinstance(other, Persoana):
            return self.__personID == other.__personID
        return False

    def __str__(self):
        return f"{self.__personID} {self.__nume} {self.__adresa}"