class Participare:

    def __init__(self,id_participare,persoana,eveniment):
        self.__id_participare = id_participare
        self.__persoana = persoana
        self.__eveniment = eveniment
        #self.__participare = participare

    def get_id_participare(self):
        return self.__id_participare

    def get_persoana(self):
        return self.__persoana

    def get_eveniment(self):
        return self.__eveniment
    def set_persoana(self,persoana):
        self.__persoana = persoana

    def set_eveniment(self,eveniment):
        self.__eveniment = eveniment

    def __str__(self):
        return f"ID: {self.__id_participare}; Persoana: {self.__persoana}; Eveniment: {self.__eveniment}" #Participare: {self.__participare}"