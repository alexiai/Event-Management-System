from Domain.eveniment import Eveniment
from infrastructura.repository_eveniment import RepoEveniment


class RepositoryFileEveniment(RepoEveniment):
    def __init__(self, nume_fisier):
        RepoEveniment.__init__(self)
        self.nume_fisier = nume_fisier

    def load_from_file(self):
        with open(self.nume_fisier, "r") as f:
            lines = f.readlines()
            for line in lines:
                line.strip()
                if line != '\n':
                    params = line.split(',')
                    id = int(params[0])
                    data = params[1]
                    timp = int(params[2])
                    descriere = params[3]
                    eveniment = Eveniment(id, data,timp,descriere)
                    self._RepoEveniment__evenimente[id] = eveniment

    def write_to_file(self):
        with open(self.nume_fisier, "w") as f:
            evenimente = self.get_all()  # modificare aici
            for eveniment in evenimente:
                id = int(eveniment.get_id_eveniment())
                data = eveniment.get_data()
                timp = int(eveniment.get_timp())
                descriere = eveniment.get_descriere()
                f.write(str(id) + ',' + data + ',' + str(timp) + ',' + descriere + '\n')

    def adauga_eveniment(self,eveniment):
        self.load_from_file()
        RepoEveniment.adauga_eveniment(self,eveniment)
        self.write_to_file()
    def sterge_eveniment_dupa_id(self,id):
        self.load_from_file()
        RepoEveniment.sterge_eveniment_dupa_id(self,id)
        self.write_to_file()
    def modifica_eveniment(self,eveniment):
        self.load_from_file()
        RepoEveniment.modifica_eveniment(self,eveniment)
        self.write_to_file()
    def cauta_eveniment_dupa_id(self,id):
        self.load_from_file()
        return RepoEveniment.cauta_eveniment_dupa_id(self,id)
    def get_all(self):
        self.load_from_file()
        return RepoEveniment.get_all(self)