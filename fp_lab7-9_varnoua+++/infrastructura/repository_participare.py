from erori.repository_error import RepoError

class RepoParticipare:

    def __init__(self):
        self.__participari = {}

    def adauga_participare(self, participare):
        if participare.get_id_participare() in self.__participari:
            raise RepoError("Participare existentă!")
        self.__participari[participare.get_id_participare()] = participare
        print("Participare adăugată cu succes:", participare)

    def sterge_participare_dupa_id(self,id_participare):
        if id_participare not in self.__participari:
            raise RepoError("participare inexistenta!")
        del self.__participari[id_participare]

    def cauta_participare_dupa_id(self,id_participare):
        if id_participare not in self.__participari:
            raise RepoError("participare inexistenta!")
        return self.__participari[id_participare]

    def modifica_participare(self,participare):
        if participare.get_id_participare() not in self.__participari:
            raise RepoError("participare inexistenta!")
        self.__participari[participare.get_id_participare()] = participare

    def get_all(self):
        participari = []
        for participare_id in self.__participari:
            participari.append(self.__participari[participare_id])
        return participari

    def __len__(self):
        return len(self.__participari)