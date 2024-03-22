from erori.repository_error import RepoError
from erori.validation_error import ValidError
import random
import string

class UI:
    def __init__(self,service_persoana,service_eveniment,service_participare):
        self.__service_persoana = service_persoana
        self.__service_eveniment = service_eveniment
        self.__service_participare = service_participare
        self.__comenzi = {
            "adauga_persoana": self.__ui_adauga_persoana,
            "print_persoane": self.__ui_print_persoane,
            "adauga_eveniment": self.__ui_adauga_eveniment,
            "print_evenimente": self.__ui_print_evenimente,
            "cauta_persoana": self.__ui_cauta_persoana,
            "cauta_eveniment": self.__ui_cauta_eveniment,
            "inscriere": self.__ui_inscriere,
            "print_inscrieri": self.__ui_print_inscrieri,
            "sterge_persoana": self.__ui_sterge_persoana_si_participarile_ei,
            "sterge_eveniment": self.__ui_sterge_eveniment_si_participarile_lui,
            "modifica_persoana": self.__ui_modifica_persoana_si_participarile_ei,
            "modifica_eveniment": self.__ui_modifica_eveniment_si_participarile_lui,
            "adauga_persoana_random": self.__ui_adauga_persoana_random,
            "adauga_eveniment_random": self.__ui_adauga_eveniment_random,
            "sortare_dupa_descriere": self.__ui_sortare_dupa_descriere,
            "persoane_celemaimulte_evenimente": self.__ui_persoane_evenimente_max,
            "primele_20_la_suta": self.__ui_primele_20_la_suta,
            "evenimente_luna": self.__ui_evenimente_luna_ordonate
        }

    def __ui_adauga_persoana(self):
        if len(self.__params) != 3:
            print("numar parametrii invaalid!")
            return
        personID = int(self.__params[0])
        nume = self.__params[1]
        adresa = self.__params[2]
        self.__service_persoana.adauga_persoana(personID,nume,adresa)
        print("persoana adaugata cu succes!")

    def __ui_print_persoane(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        persoane = self.__service_persoana.get_all_persoane()
        if len(persoane) == 0:
            print("nu exista persoane in aplicatie!")
            return
        for persoana in persoane:
            print(persoana)

    def __ui_adauga_eveniment(self):
        if len(self.__params) != 4:
            print("numar parametrii invalid!")
            return
        id_eveniment = int(self.__params[0])
        data = self.__params[1]
        timp = self.__params[2]
        descriere = self.__params[3]
        self.__service_eveniment.adauga_eveniment(id_eveniment,data,timp,descriere)
        print("eveniment adaugat cu succes!")

    def __ui_print_evenimente(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        evenimente = self.__service_eveniment.get_all_evenimente()
        if len(evenimente) == 0:
            print("nu exista evenimente in aplicatie!")
            return
        for eveniment in evenimente:
            print(eveniment)

    def __ui_cauta_persoana(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        personID = int(self.__params[0])
        persoana = self.__service_persoana.cauta_persoana(personID)
        print(persoana)

    def __ui_cauta_eveniment(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_eveniment = int(self.__params[0])
        eveniment = self.__service_eveniment.cauta_eveniment(id_eveniment)
        print(eveniment)

    def __ui_inscriere(self):
        if len(self.__params) != 3:
            print("numar parametrii invalid!")
            return
        id_participare = int(self.__params[0])
        personID = int(self.__params[1])
        id_eveniment = int(self.__params[2])
        self.__service_participare.inscriere(id_participare,personID,id_eveniment)
        print("persoana inscrisa cu succes!")

    def __ui_print_inscrieri(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return
        inscrieri = self.__service_participare.get_all_inscrieri()
        if len(inscrieri) == 0:
            print("nu exista inscrieri in aplicatie!")
            return
        for inscriere in inscrieri:
            print(inscriere)

    def __ui_sterge_persoana_si_participarile_ei(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        personID =int(self.__params[0])
        self.__service_participare.sterge_persoana_si_participarile_ei(personID)
        print(f"persoana cu id-ul {personID} si participarile ei sterse cu succes!")

    def __ui_sterge_eveniment_si_participarile_lui(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        id_eveniment = int(self.__params[0])
        self.__service_participare.sterge_eveniment_si_participarile_lui(id_eveniment)
        print(f"evenimentul cu id-ul {id_eveniment} si participarile lui sterse cu succes!")

    def __ui_modifica_persoana_si_participarile_ei(self):
        if len(self.__params) != 3:
            print("numar parametrii invalid!")
            return
        personID = int(self.__params[0])
        nume = self.__params[1]
        adresa = self.__params[2]
        self.__service_persoana.modifica_persoana(personID, nume, adresa)
        self.__service_participare.modifica_persoana_si_participarile_ei(personID)
        print("persoana modificata cu succes!")

    def __ui_modifica_eveniment_si_participarile_lui(self):
        if len(self.__params) != 4:
            print("numar parametrii invalid!")
            return
        id_eveniment = int(self.__params[0])
        data = self.__params[1]
        timp = self.__params[2]
        descriere = self.__params[3]
        self.__service_eveniment.modifica_eveniment(id_eveniment,data,timp,descriere)
        self.__service_participare.modifica_eveniment_si_participarile_lui(id_eveniment)
        print("eveniment modificat cu succes!")

    def __ui_adauga_persoana_random(self):
        if len(self.__params) != 3:
            print("numar parametrii invaalid!")
            return
        personID = int(self.__params[0])
        length_random1 = int(self.__params[1])
        length_random2 = int(self.__params[2])
        letters = string.ascii_lowercase
        result_str1 = ''.join(random.choice(letters) for i in range(length_random1))
        result_str2 = ''.join(random.choice(letters) for i in range(length_random2))
        nume = str(result_str1)
        adresa = str(result_str2)
        self.__service_persoana.adauga_persoana(personID,nume,adresa)
        print("persoana adaugata cu succes!")

    def __ui_adauga_eveniment_random(self):
        if len(self.__params) != 2:
            print("numar parametrii invalid!")
            return
        id_eveniment = int(self.__params[0])
        zi = random.randint(1, 31)
        luna = random.randint(1, 12)
        an = random.randint(2023, 2030)
        data = f"{zi:02d}-{luna:02d}-{an}"
        timp = int(random.randint(5,300))
        length_random = int(self.__params[1])
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length_random))
        descriere = str(result_str)
        self.__service_eveniment.adauga_eveniment(id_eveniment,data,timp,descriere)
        print("eveniment adaugat cu succes!")

    def __ui_sortare_dupa_descriere(self):
        if len(self.__params) != 1:
            print("numar parametrii invalid!")
            return
        personID = self.__params[0]
        sortare = self.__service_participare.sortare_dupa_descriere(personID)

        """for eveniment in sortare:
            print(eveniment)"""

    def __ui_persoane_evenimente_max(self):
        self.__params = []
        if len(self.__params) != 0:
            print("numar parametrii invalidi!")
            return
        persoane_cu_cele_mai_multe_participari = self.__service_participare.get_persoane_cu_cele_mai_multe_participari()
        for persoana, nr_participanti in persoane_cu_cele_mai_multe_participari:
            print(
                f"persoana cu cele mai multe participari: {persoana.get_nume()}, nr. participari: {nr_participanti}")


    def __ui_primele_20_la_suta(self):
        if len(self.__params) != 0:
            print("numar parametrii invalid!")
            return

        evenimente_top_20 = self.__service_participare.get_primele_20_la_suta()

        if len(evenimente_top_20) == 0:
            print("Nu exista!")
        else:
            for eveniment in evenimente_top_20:
                print(eveniment)

    def __ui_evenimente_luna_ordonate(self):
        if len(self.__params) != 1:
            print("Număr parametrii invalid!")
            return

        luna_selectata = self.__params[0]

        evenimente_luna_ordonate = self.__service_participare.evenimente_in_luna(luna_selectata)

        if len(evenimente_luna_ordonate) == 0:
            print(f"Nu există evenimente în luna {luna_selectata}!")
        else:
            for eveniment in evenimente_luna_ordonate:
                print(eveniment)

    def run(self):
        while True:
            print("""
        1.adauga_persoana(id/nume/adresa)
        2.print_persoane
        3.adauga_eveniment(id/data/timp/descriere)
        4.print_evenimente
        5.cauta_persoana(id)
        6.cauta_eveniment(id)
        7.inscriere(id,id_per,id_ev)
        8.print_inscrieri
        9.sterge_persoana(id)
        10.sterge_eveniment(id)
        11.modifica_persoana
        12.modifica_eveniment
        13.adauga_persoana_random(id, len, len)
        14.adauga_eveniment_random(id, len-desc)
        15.sortare_dupa_descriere(id_pers)
        16.persoane_celemaimulte_evenimente
        17.primele_20_la_suta
        18.evenimente_luna
        exit""")
            comanada = input(">>>")
            comanada = comanada.strip()
            if comanada == "":
                continue
            if comanada == "exit":
                return
            parti = comanada.split()
            nume_comanada = parti[0]
            self.__params = parti[1:]
            if nume_comanada in self.__comenzi:
                try:
                    self.__comenzi[nume_comanada]()
                except ValueError:
                    print("Eroare UI: tip numeric invalid")
                except ValidError as ve:
                    print(f"Validation Error: {ve}")
                except RepoError as re:
                    print(f"Repository Error: {re}")
            else:
                print("Comanda Invalida!")