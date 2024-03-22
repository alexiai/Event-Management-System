from Domain.persoana import Persoana
from infrastructura.reposistory_persoana import RepoPersoana


class RepositoryFilePersoana(RepoPersoana):
    def __init__(self, nume_fisier):
        RepoPersoana.__init__(self)
        self.nume_fisier = nume_fisier

    def load_from_file(self):
        with open(self.nume_fisier, "r") as f:
            lines = f.readlines()
            for line in lines:
                line.strip()
                if line != '\n':
                    params = line.split(',')
                    id = int(params[0])
                    nume = params[1]
                    adresa = params[2]
                    persoana = Persoana(id, nume, adresa)
                    self._RepoPersoana__persoane[id] = persoana

    def write_to_file(self):
        with open(self.nume_fisier, "w") as f:
            persoane = self.get_all()
            for persoana in persoane:
                id = int(persoana.get_personID())
                nume = persoana.get_nume()
                adresa = persoana.get_adresa()
                f.write(f"{id},{nume},{adresa}\n")

    def adauga_persoana(self,persoana):
        self.load_from_file()
        RepoPersoana.adauga_persoana(self,persoana)
        self.write_to_file()
    def sterge_persoana_dupa_id(self,id):
        self.load_from_file()
        RepoPersoana.sterge_persoana_dupa_id(self,id)
        self.write_to_file()
    def modifica_persoana(self,persoana):
        self.load_from_file()
        RepoPersoana.modifica_persoana(self,persoana)
        self.write_to_file()
    def cauta_persoana_dupa_id(self,id):
        self.load_from_file()
        return RepoPersoana.cauta_persoana_dupa_id(self,id)
    def get_all(self):
        self.load_from_file()
        return RepoPersoana.get_all(self)