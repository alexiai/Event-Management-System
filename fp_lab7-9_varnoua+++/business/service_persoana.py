from Domain.persoana import Persoana

class ServicePersoana:

    def __init__(self,validator_persoana,repo_persoana):
        self.__validator_persoana = validator_persoana
        self.__repo_persoana = repo_persoana

    def adauga_persoana(self,personID,nume,adresa):
        persoana = Persoana(personID,nume,adresa)
        self.__validator_persoana.valideaza(persoana)
        self.__repo_persoana.adauga_persoana(persoana)

    def cauta_persoana(self,personID):
        return self.__repo_persoana.cauta_persoana_dupa_id(personID)

    def modifica_persoana(self,personID,nume,adresa):
        persoana = Persoana(personID,nume,adresa)
        self.__validator_persoana.valideaza(persoana)
        self.__repo_persoana.modifica_persoana(persoana)

    def get_all_persoane(self):
        return self.__repo_persoana.get_all()