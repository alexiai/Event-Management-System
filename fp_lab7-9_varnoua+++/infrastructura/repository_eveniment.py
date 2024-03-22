from erori.repository_error import RepoError

class RepoEveniment:

    def __init__(self):
        self.__evenimente = {}

    def adauga_eveniment(self,eveniment):
        if eveniment.get_id_eveniment() in self.__evenimente:
            raise RepoError("eveniment existent!")
        self.__evenimente[eveniment.get_id_eveniment()] = eveniment

    def sterge_eveniment_dupa_id(self,id_eveniment):
        if id_eveniment not in self.__evenimente:
            raise RepoError("eveniment inexistent!")
        del self.__evenimente[id_eveniment]

    def cauta_eveniment_dupa_id(self,id_eveniment):
        if id_eveniment not in self.__evenimente:
            raise RepoError("eveniment inexistent!")
        return self.__evenimente[id_eveniment]

    def modifica_eveniment(self,eveniment):
        if eveniment.get_id_eveniment() not in self.__evenimente:
            raise RepoError("eveniment inexistent!")
        self.__evenimente[eveniment.get_id_eveniment()] = eveniment

    def get_all(self):
        evenimente = []
        for eveniment_id in self.__evenimente:
            evenimente.append(self.__evenimente[eveniment_id])
        return evenimente

    def __len__(self):
        return len(self.__evenimente)