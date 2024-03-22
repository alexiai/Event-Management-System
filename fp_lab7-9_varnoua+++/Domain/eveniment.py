class Eveniment:

    def __init__(self,id_eveniment,data,timp,descriere):
        self.__id_eveniment = id_eveniment
        self.__data = data
        self.__timp = timp
        self.__descriere = descriere

    def get_id_eveniment(self):
        return self.__id_eveniment

    def get_data(self):
        return self.__data

    def get_timp(self):
        return self.__timp

    def get_descriere(self):
        return self.__descriere

    def set_data(self,data):
        self.__data = data

    def set_timp(self,timp):
        self.__timp = timp

    def set_descriere(self,descriere):
        self.__descriere = descriere

    def __eq__(self, other):
        if isinstance(other, Eveniment):
            return self.__id_eveniment == other.__id_eveniment
        return False

    def __str__(self):
        return f"{self.__id_eveniment} {self.__data} {self.__timp} {self.__descriere}"
