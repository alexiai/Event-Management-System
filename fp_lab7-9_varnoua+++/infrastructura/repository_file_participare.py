from Domain.eveniment import Eveniment
from Domain.participare import Participare
from Domain.persoana import Persoana
from infrastructura.repository_participare import RepoParticipare


class RepositoryFileParticipare(RepoParticipare):
    def __init__(self, nume_fisier):
        RepoParticipare.__init__(self)
        self.nume_fisier = nume_fisier

    def load_from_file(self):
        with open(self.nume_fisier, "r") as f:
            lines = f.readlines()
            for line in lines:
                line.strip()
                if line != '\n':
                    params = line.split(',')
                    id = int(params[0])
                    id_per = int(params[1])
                    id_ev = int(params[2])
                    participare = Participare(id, id_per,id_ev)
                    self._RepoParticipare__participari[id] = participare

    def write_to_file(self):
        with open(self.nume_fisier, "a") as f:  # Use "a" for append mode
            participari = self.get_all()
            for participare in participari:
                id = int(participare.get_id_participare())

                persoana = participare.get_persoana()
                if not isinstance(persoana, Persoana):
                    # Handle the case where get_persoana() returns an unexpected type
                    continue

                id_per = int(persoana.get_personID())

                eveniment = participare.get_eveniment()
                if not isinstance(eveniment, Eveniment):
                    # Handle the case where get_eveniment() returns an unexpected type
                    continue

                id_ev = int(eveniment.get_id_eveniment())

                f.write(str(id) + ',' + str(id_per) + ',' + str(id_ev) + '\n')

    def adauga_participare(self,participare):
        self.load_from_file()
        RepoParticipare.adauga_participare(self,participare)
        self.write_to_file()
        print("Participare adăugată în fișier:", participare)


    def sterge_participare_dupa_id(self,id):
        self.load_from_file()
        RepoParticipare.sterge_participare_dupa_id(self,id)
        self.write_to_file()
    def modifica_participare(self,participare):
        self.load_from_file()
        RepoParticipare.modifica_participare(self,participare)
        self.write_to_file()
    def cauta_participare_dupa_id(self,id):
        self.load_from_file()
        return RepoParticipare.cauta_participare_dupa_id(self,id)
    def get_all(self):
        self.load_from_file()
        return RepoParticipare.get_all(self)