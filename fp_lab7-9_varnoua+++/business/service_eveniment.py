from Domain.eveniment import Eveniment

class ServiceEveniment:

    def __init__(self,validator_eveniment,repo_eveniment):
        self.__validator_eveniment = validator_eveniment
        self.__repo_eveniment = repo_eveniment

    def adauga_eveniment(self,id_eveniment,data,timp,descriere):
        eveniment = Eveniment(id_eveniment,data,timp,descriere)
        self.__validator_eveniment.valideaza(eveniment)
        self.__repo_eveniment.adauga_eveniment(eveniment)

    def cauta_eveniment(self,id_eveniment):
        return self.__repo_eveniment.cauta_eveniment_dupa_id(id_eveniment)

    def modifica_eveniment(self,id_eveniment,data,timp,descriere):
        eveniment = Eveniment(id_eveniment,data,timp,descriere)
        self.__validator_eveniment.valideaza(eveniment)
        self.__repo_eveniment.modifica_eveniment(eveniment)

    def get_all_evenimente(self):
        return self.__repo_eveniment.get_all()