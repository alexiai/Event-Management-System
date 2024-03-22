from Domain.eveniment import Eveniment
from Domain.eveniment_participanti import EvenimentParticipanti
from Domain.participare import Participare
from Domain.persoana import Persoana
from erori.repository_error import RepoError
from infrastructura.repository_file_eveniment import RepositoryFileEveniment
from infrastructura.repository_file_persoana import RepositoryFilePersoana
from validare.validator_persoana import *
from validare.validator_eveniment import *
from validare.validator_participare import *
from infrastructura.reposistory_persoana import RepoPersoana
from infrastructura.repository_eveniment import RepoEveniment
from infrastructura.repository_participare import RepoParticipare
from business.service_persoana import ServicePersoana
from business.service_eveniment import ServiceEveniment
from business.service_participare import ServiceParticipare

class Teste:

    def __goleste_fisier(self, nume_fisier):
        with open(nume_fisier, "w") as f:
            pass

    def tearDown(self):
        pass

    def __init__(self):
        pass

    def test_validatori(self):
        p1 = Persoana(1, 'Popescu Ion', 'str Lalelelor nr1')
        assert (p1.get_personID() == 1)
        assert (p1.get_nume() == 'Popescu Ion')
        assert (p1.get_adresa()== 'str Lalelelor nr1')

        e1 = Eveniment(1, '10-12-2023', 120, 'Sedita de grup')
        assert (e1.get_id_eveniment() == 1)
        assert (e1.get_data() == '10-12-2023')
        assert (e1.get_timp() == 120)
        assert (e1.get_descriere() == 'Sedita de grup')

        i1= Participare(1,1,1)
        assert (i1.get_id_participare() ==1)
        assert (i1.get_persoana() == 1)
        assert (i1.get_eveniment() == 1)

    def test_persoana(self):
        nume_fisierp = "testare/teste_persoane.txt"
        rP = RepositoryFilePersoana(nume_fisierp)
        self.__goleste_fisier(nume_fisierp)
        vP = ValidatorPersoana()
        sP = ServicePersoana(vP, rP)
         #adaugare
        sP.adauga_persoana(1, 'Popescu Ion', 'str Lalelelor nr1')
        assert int(len(sP.get_all_persoane())) == 1
         #stergere
        sP.adauga_persoana(2, 'Popescu Ana', 'str Principala nr 47')
        assert int(len(sP.get_all_persoane())) == 2
        rP.sterge_persoana_dupa_id(2)
        assert int(len(sP.get_all_persoane())) == 1
         #cautare
        assert int(rP.cauta_persoana_dupa_id(1).get_personID()) == 1
        assert rP.cauta_persoana_dupa_id(1).get_nume() == "Popescu Ion"
        assert sP.cauta_persoana(1).get_nume() == "Popescu Ion"
        assert rP.cauta_persoana_dupa_id(1).get_adresa().strip() == 'str Lalelelor nr1'
        assert sP.cauta_persoana(1).get_adresa().strip() == 'str Lalelelor nr1'
         #modifica
        sP.modifica_persoana(1,"Popescu Marian", "Cluj")
        assert int(len(sP.get_all_persoane())) == 1
        assert rP.cauta_persoana_dupa_id(1).get_nume() == "Popescu Marian"
        assert sP.cauta_persoana(1).get_nume() == "Popescu Marian"
        assert rP.cauta_persoana_dupa_id(1).get_adresa().strip() == "Cluj"
        assert sP.cauta_persoana(1).get_adresa().strip() == "Cluj"
    def test_eveniment(self):
        nume_fisiere = "testare/teste_evenimente.txt"
        rE = RepositoryFileEveniment(nume_fisiere)
        self.__goleste_fisier(nume_fisiere)
        vE = ValidatorEveniment()
        sE = ServiceEveniment(vE, rE)
         #adaugare
        sE.adauga_eveniment(1, "10-12-2023", 120, "Sedita de grup")
        assert int(len(sE.get_all_evenimente())) == 1
         #stergere
        sE.adauga_eveniment(2, "12-09-2023", 100, "Consultatie")
        assert int(len(sE.get_all_evenimente())) == 2
        rE.sterge_eveniment_dupa_id(2)
        assert int(len(sE.get_all_evenimente())) == 1
         #cautare
        assert int(rE.cauta_eveniment_dupa_id(1).get_id_eveniment()) == 1
        assert int(sE.cauta_eveniment(1).get_id_eveniment()) == 1
        assert rE.cauta_eveniment_dupa_id(1).get_data() == "10-12-2023"
        assert sE.cauta_eveniment(1).get_data() == "10-12-2023"
        assert int(rE.cauta_eveniment_dupa_id(1).get_timp()) == 120
        assert int(sE.cauta_eveniment(1).get_timp()) == 120
        assert rE.cauta_eveniment_dupa_id(1).get_descriere().strip() == "Sedita de grup"
        assert sE.cauta_eveniment(1).get_descriere().strip() == "Sedita de grup"
         #modifica
        sE.modifica_eveniment(1,"11-09-2023", 123, "Sedite de grup")
        assert rE.cauta_eveniment_dupa_id(1).get_data() == "11-09-2023"
        assert sE.cauta_eveniment(1).get_data() == "11-09-2023"
        assert int(rE.cauta_eveniment_dupa_id(1).get_timp()) == 123
        assert int(sE.cauta_eveniment(1).get_timp()) == 123
        assert rE.cauta_eveniment_dupa_id(1).get_descriere().strip() == "Sedite de grup"
        assert sE.cauta_eveniment(1).get_descriere().strip() == "Sedite de grup"

    def test_inscrieri(self):
        nume_fisierp = "testare/teste_persoane.txt"
        rP = RepositoryFilePersoana(nume_fisierp)
        self.__goleste_fisier(nume_fisierp)
        nume_fisiere = "testare/teste_evenimente.txt"
        rE = RepositoryFileEveniment(nume_fisiere)
        self.__goleste_fisier(nume_fisiere)
        nume_fisierpar = "testare/teste_participari.txt"
        rPart = RepoParticipare()
        self.__goleste_fisier(nume_fisierpar)
        vP = ValidatorPersoana()
        vE = ValidatorEveniment()
        vPart = ValidatorParticipare()
        sP = ServicePersoana(vP, rP)
        sE = ServiceEveniment(vE, rE)
        sPart = ServiceParticipare(vPart, rPart, rP, rE)
         #adaugare
        sP.adauga_persoana(1, 'Alexia', 'Cluj')
        sE.adauga_eveniment(1, '17-10-2023', '173', 'Gameing')
        sPart.inscriere(1, 1, 1)
        assert int(len(sPart.get_all_inscrieri())) == 1
         #cautari
        assert int(rPart.cauta_participare_dupa_id(1).get_id_participare()) == 1
        sP.adauga_persoana(2, 'Andreea', 'Sibiu')
        sE.adauga_eveniment(2, '17-06-2023', '163', 'IT')
        sPart.inscriere(2, 2, 2)
        assert int(len(rPart.get_all())) == 2
        try:
            sP.adauga_persoana(2, 'David', 'Mures')
            assert False
        except RepoError:
            pass
        try:
            sE.adauga_eveniment(2, '12-06-2024', '130', 'Sedinta')
            assert False
        except RepoError:
            pass
        sP.adauga_persoana(3, 'David', 'Mures')
        sE.adauga_eveniment(3, '12-06-2020', '130', 'Sedinta')
        try:
            sPart.inscriere(2, 3, 3)
            assert False
        except RepoError:
            pass
        assert int(len(rPart.get_all())) == 2

    def test_sortare_dupa_descriere(self):
        nume_fisierp = "testare/teste_persoane.txt"
        rP = RepositoryFilePersoana(nume_fisierp)
        self.__goleste_fisier(nume_fisierp)
        nume_fisiere = "testare/teste_evenimente.txt"
        rE = RepositoryFileEveniment(nume_fisiere)
        self.__goleste_fisier(nume_fisiere)
        nume_fisierpar = "testare/teste_participari.txt"
        rPart = RepoParticipare()
        self.__goleste_fisier(nume_fisierpar)
        vPart = ValidatorParticipare()
        vE = ValidatorEveniment()
        vP = ValidatorPersoana()

        sPart = ServiceParticipare(vPart, rPart, rP,rE)
        sE= ServiceEveniment(vE, rE)
        sP= ServicePersoana(vP, rP)

        sE.adauga_eveniment(1, "2023-01-01", 100, "Eveniment 1")
        sE.adauga_eveniment(2, "2023-02-01", 143, "Eveniment 2")
        sE.adauga_eveniment(3, "2023-03-15", 153, "Conferinta IT")
        sE.adauga_eveniment(4, "2023-04-20", 110, "Sesiune de training")
        sE.adauga_eveniment(5, "2023-05-10", 180, "Eveniment cultural")

        sP.adauga_persoana(1, "Ion Popescu", "Str. Primaverii, nr. 10")
        sP.adauga_persoana(2, "Ana Vasilescu", "Str. Libertatii, nr. 5")
        sP.adauga_persoana(3, "Mihai Popa", "Str. Tudor Vladimirescu, nr. 25")
        sP.adauga_persoana(4, "Ana Maria Radu", "Bd. Decebal, nr. 7")
        sP.adauga_persoana(5, "Adrian Stoica", "Str. Mihail Kogalniceanu, nr. 12")

        sPart.inscriere(1, 1,1)
        sPart.inscriere(2, 2,1)
        sPart.inscriere(3, 1,2)
        sPart.inscriere(4, 3,3)
          #inscrierile persoanei 1 ->s-a inscris la ev1 si la ev2
        inscrieri_filtrate = sPart.sortare_dupa_descriere(1)
        #assert len(inscrieri_filtrate) == 2
        #assert inscrieri_filtrate[0].get_descriere().strip() == "Eveniment 1"
        #assert inscrieri_filtrate[1].get_descriere().strip() == "Eveniment 2"

    def test_get_eveniment_participanti_max(self):
        nume_fisierp = "testare/teste_persoane.txt"
        rP = RepositoryFilePersoana(nume_fisierp)
        self.__goleste_fisier(nume_fisierp)
        nume_fisiere = "testare/teste_evenimente.txt"
        rE = RepositoryFileEveniment(nume_fisiere)
        self.__goleste_fisier(nume_fisiere)
        nume_fisierpar = "testare/teste_participari.txt"
        rPart = RepoParticipare()
        self.__goleste_fisier(nume_fisierpar)
        vPart = ValidatorParticipare()
        vE = ValidatorEveniment()
        vP = ValidatorPersoana()

        sPart = ServiceParticipare(vPart, rPart, rP, rE)
        sE = ServiceEveniment(vE, rE)
        sP = ServicePersoana(vP, rP)
        e1 = Eveniment(1, "2023-01-01", 100, "Eveniment 1")
        e2 = Eveniment(2, "2023-02-01", 143, "Eveniment 2")
        e4 = Eveniment(4, "2023-04-20", 110, "Sesiune de training")
        sE.adauga_eveniment(1, "2023-01-01", 100, "Eveniment 1")
        sE.adauga_eveniment(2, "2023-02-01", 143, "Eveniment 2")
        sE.adauga_eveniment(3, "2023-03-15", 153, "Conferinta IT")
        sE.adauga_eveniment(4, "2023-04-20", 110, "Sesiune de training")
        sE.adauga_eveniment(5, "2023-05-10", 180, "Eveniment cultural")

        sP.adauga_persoana(1, "Ion Popescu", "Str. Primaverii, nr. 10")
        sP.adauga_persoana(2, "Ana Vasilescu", "Str. Libertatii, nr. 5")
        sP.adauga_persoana(3, "Mihai Popa", "Str. Tudor Vladimirescu, nr. 25")
        sP.adauga_persoana(4, "Ana Maria Radu", "Bd. Decebal, nr. 7")
        sP.adauga_persoana(5, "Adrian Stoica", "Str. Mihail Kogalniceanu, nr. 12")

        sPart.inscriere(1, 1, 1)
        sPart.inscriere(2, 2, 1)
        sPart.inscriere(3, 3, 1)
        sPart.inscriere(4, 1, 2)
        sPart.inscriere(5, 2, 2)
        sPart.inscriere(6, 4, 2)
        sPart.inscriere(7, 1, 4)
        sPart.inscriere(8, 3, 4)
        sPart.inscriere(9, 1, 5)

        top_pers = sPart.get_persoane_cu_cele_mai_multe_participari()
        assert len(top_pers) == 1
        assert top_pers[0][0].get_nume() == "Ion Popescu"


    def test_top_20(self):
        nume_fisierp = "testare/teste_persoane.txt"
        rP = RepositoryFilePersoana(nume_fisierp)
        self.__goleste_fisier(nume_fisierp)
        nume_fisiere = "testare/teste_evenimente.txt"
        rE = RepositoryFileEveniment(nume_fisiere)
        self.__goleste_fisier(nume_fisiere)
        nume_fisierpar = "testare/teste_participari.txt"
        rPart = RepoParticipare()
        self.__goleste_fisier(nume_fisierpar)
        vPart = ValidatorParticipare()
        vE = ValidatorEveniment()
        vP = ValidatorPersoana()

        sPart = ServiceParticipare(vPart, rPart, rP, rE)
        sE = ServiceEveniment(vE, rE)
        sP = ServicePersoana(vP, rP)

        p1 = Persoana(1, "Ion Popescu", "Str. Primaverii, nr. 10")
        e1 = Eveniment(1, "2023-01-01", 1000, "Eveniment 1")
        e2 = Eveniment(2, "2023-02-01", 1430, "Eveniment 2")
        e3 = Eveniment(3, "2023-05-10", 1800, "Eveniment cultural")

        sP.adauga_persoana(1, "Ion Popescu", "Str. Primaverii, nr. 10")
        sE.adauga_eveniment(1, "2023-01-01", 1000, "Eveniment 1")
        sE.adauga_eveniment(2, "2023-02-01", 1430, "Eveniment 2")
        sE.adauga_eveniment(3, "2023-05-10", 1800, "Eveniment cultural")

        sPart.inscriere(1, 1, 1)  # Participare la Ev 1
        sPart.inscriere(2, 1, 1)  # Participare la Ev 1
        sPart.inscriere(3, 1, 2)  # Participare la Ev 2
        sPart.inscriere(4, 1, 3)  # Participare la Ev 3


        primele_20_la_suta = sPart.get_primele_20_la_suta()

        # Sunt 3 evenimente, al 3lea nu ar trebui sa intre in top
        assert len(primele_20_la_suta) > 0
        assert primele_20_la_suta[0].get_descriere().strip() == "Eveniment 1"
        assert primele_20_la_suta[1].get_descriere().strip() == "Eveniment 2"

    def test_evenimente_luna_ordonate(self):
        nume_fisierp = "testare/teste_persoane.txt"
        rP = RepositoryFilePersoana(nume_fisierp)
        self.__goleste_fisier(nume_fisierp)
        nume_fisiere = "testare/teste_evenimente.txt"
        rE = RepositoryFileEveniment(nume_fisiere)
        self.__goleste_fisier(nume_fisiere)
        nume_fisierpar = "testare/teste_participari.txt"
        rPart = RepoParticipare()
        self.__goleste_fisier(nume_fisierpar)
        vE = ValidatorEveniment()
        sE = ServiceEveniment(vE, rE)
        vPar = ValidatorParticipare()
        sPar = ServiceParticipare(vPar, rPart, rP, rE)

        # Adaugăm evenimente pentru luna curentă și o altă lună
        sE.adauga_eveniment(1, "15-01-2023", 120, "Eveniment 1")
        sE.adauga_eveniment(2, "01-01-2023", 100, "Eveniment 2")
        sE.adauga_eveniment(3, "02-05-2023", 150, "Eveniment 3")

        # Așteptăm evenimentele ordonate conform cerinței
        evenimente_ordonate = sPar.evenimente_in_luna("01")

        assert len(evenimente_ordonate) == 2
        assert evenimente_ordonate[0].get_descriere().strip() == "Eveniment 2"
        assert evenimente_ordonate[1].get_descriere().strip() == "Eveniment 1"

    def ruleaza_toate_testele(self):
        self.test_validatori()
        self.test_persoana()
        self.test_eveniment()
        self.test_inscrieri()
        self.test_sortare_dupa_descriere()
        self.test_get_eveniment_participanti_max()
        self.test_top_20()
        self.test_evenimente_luna_ordonate()