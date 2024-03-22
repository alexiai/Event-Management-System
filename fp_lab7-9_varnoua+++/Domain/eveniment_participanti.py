class EvenimentParticipanti:

    def __init__(self,descriere_eveniment,nr_participari):
        self.__descriere_eveniment = descriere_eveniment
        self.__nr_participari = nr_participari

    def __str__(self):
        return f"evenimentul {self.__descriere_eveniment} are participari la id-urile: {self.__nr_participari}"

    def __lt__(self, other):
        return self.__nr_participari < other.__nr_participari