from erori.repository_error import RepoError

class RepoPersoana:

    def __init__(self):
        self.__persoane = {}

    def adauga_persoana(self,persoana):
        if persoana.get_personID() in self.__persoane:
            raise RepoError("persoana existenta!")
        self.__persoane[persoana.get_personID()] = persoana

    def sterge_persoana_dupa_id(self,personID):
        if personID not in self.__persoane:
            raise RepoError("persoana inexistenta!")
        del self.__persoane[personID]

    def cauta_persoana_dupa_id(self,personID):
        if personID not in self.__persoane:
            raise RepoError("persoana inexistenta!")
        return self.__persoane[personID]

    def modifica_persoana(self,persoana):
        if persoana.get_personID() not in self.__persoane:
            raise RepoError("persoana inexistenta!")
        self.__persoane[persoana.get_personID()] = persoana

    def get_all(self):
        persoane = []
        for persoana_id in self.__persoane:
            persoane.append(self.__persoane[persoana_id])
        return persoane

    def __len__(self):
        return len(self.__persoane)