from datetime import datetime

from Domain.eveniment import Eveniment
from Domain.participare import Participare
from Domain.eveniment_participanti import EvenimentParticipanti

class ServiceParticipare:

    def __init__(self,validator_participare,repo_participare,repo_persoane,repo_evenimente):
        self.__validator_participare = validator_participare
        self.__repo_participare = repo_participare
        self.__repo_persoane = repo_persoane
        self.__repo_evenimente = repo_evenimente

    def inscriere(self,id_participare,personID,id_eveniment):
        persoana = self.__repo_persoane.cauta_persoana_dupa_id(personID)
        eveniment = self.__repo_evenimente.cauta_eveniment_dupa_id(id_eveniment)
        participare = Participare(id_participare,persoana,eveniment)
        self.__validator_participare.valideaza(participare)
        self.__repo_participare.adauga_participare(participare)

    def sterge_persoana_si_participarile_ei(self,personID):
        persoana = self.__repo_persoane.cauta_persoana_dupa_id(personID)
        participari = self.__repo_participare.get_all()
        participari_persoana = [x for x in participari if x.get_persoana() == persoana]
        for participare_persoana in participari_persoana:
            self.__repo_participare.sterge_participare_dupa_id(participare_persoana.get_id_participare())
        self.__repo_persoane.sterge_persoana_dupa_id(personID)

    def sterge_eveniment_si_participarile_lui(self,id_eveniment):
        eveniment = self.__repo_evenimente.cauta_eveniment_dupa_id(id_eveniment)
        participari = self.__repo_participare.get_all()
        participari_persoana = [x for x in participari if x.get_eveniment() == eveniment]
        for participare_persoana in participari_persoana:
            self.__repo_participare.sterge_participare_dupa_id(participare_persoana.get_id_participare())
        self.__repo_evenimente.sterge_eveniment_dupa_id(id_eveniment)

    def modifica_persoana_si_participarile_ei(self,personID):
        persoana = self.__repo_persoane.cauta_persoana_dupa_id(personID)
        participari = self.__repo_participare.get_all()
        participari_persoana = [x for x in participari if x.get_persoana() == persoana]
        for participare_persoana in participari_persoana:
            participare_persoana.set_persoana(persoana)

    def modifica_eveniment_si_participarile_lui(self,id_eveniment):
        eveniment = self.__repo_evenimente.cauta_eveniment_dupa_id(id_eveniment)
        participari = self.__repo_participare.get_all()
        participari_persoana = [x for x in participari if x.get_eveniment() == eveniment]
        for participare_persoana in participari_persoana:
            participare_persoana.set_eveniment(eveniment)

    def sortare_dupa_descriere(self,personID):
        """
                Se afiseaza toate evenimentele la care a participat persoana cu id-ul id, evenimentele sunt ordonate alfabatic(pentru descriere) si dupa cronologic(dupa data)
                :param personID:
                :return:
                """
        inscrieri_lst = self.__repo_participare.get_all()
        evenimente_persoana = []

        for participare in inscrieri_lst:
            if participare.get_persoana() == int(personID):
                evenimente_persoana.append(participare.get_eveniment())

        ######
        persoane_dict = {persoana.get_personID(): persoana for persoana in self.__repo_persoane.get_all()}
        evenimente_dict = {eveniment.get_id_eveniment(): eveniment for eveniment in self.__repo_evenimente.get_all()}

        # Sort
        evenimente_persoana = sorted(
            evenimente_persoana,
            key=lambda ev_id: evenimente_dict[ev_id].get_descriere() if ev_id in evenimente_dict else "",
        )

        print("evenimente sortate:")
        for ev_id in evenimente_persoana:
            eveniment = evenimente_dict[ev_id]
            print(eveniment)

        #return evenimente_persoana

    def get_persoane_cu_cele_mai_multe_participari(self):
        """
        Returnează lista de persoane cu cele mai multe participări la evenimente
        """
        participari = self.__repo_participare.get_all()

        # Crează un dicționar pentru a număra participările fiecărei persoane
        participari_persoane = {}
        for participare in participari:
            persoana_id = participare.get_persoana()  # Obține ID-ul persoanei
            participari_persoane[persoana_id] = participari_persoane.get(persoana_id, 0) + 1

        # Găsește numărul maxim de participări
        max_participari = max(participari_persoane.values(), default=0)

        # Filtrăm persoanele cu cele mai multe participări
        persoane_cu_cele_mai_multe_participari = filter(
            lambda x: participari_persoane.get(x, 0) == max_participari,
            participari_persoane.keys()
        )

        # Obținem detalii despre persoanele cu cele mai multe participări
        detalii_persoane = []
        for persoana_id in persoane_cu_cele_mai_multe_participari:
            persoana = self.__repo_persoane.cauta_persoana_dupa_id(persoana_id)
            nr_participanti = participari_persoane.get(persoana_id, 0)
            detalii_persoane.append((persoana, nr_participanti))

        return detalii_persoane

    def get_primele_20_la_suta(self):
        participari = self.__repo_participare.get_all()

        # Crează un dicționar pentru a număra participările la fiecare eveniment
        participari_evenimente = {}
        for participare in participari:
            eveniment_id = participare.get_eveniment()  # Obține ID-ul evenimentului
            participari_evenimente[eveniment_id] = participari_evenimente.get(eveniment_id, 0) + 1

        # Nr de evenimente care reprezintă top 20%
        numar_evenimente_20_la_suta = int(len(participari_evenimente) * 0.2)

        # Selectează ID-urile evenimentelor cu cea mai mare participare
        top_events_ids = [
            eveniment_id for eveniment_id, participanti in participari_evenimente.items()
            if participanti >= numar_evenimente_20_la_suta
        ]

        # Obține obiectele Eveniment corespunzătoare ID-urilor evenimentelor
        top_events_objects = []
        for eveniment_id in top_events_ids:
            eveniment = self.__repo_evenimente.cauta_eveniment_dupa_id(eveniment_id)
            top_events_objects.append(eveniment)

        return top_events_objects

    def evenimente_in_luna(self, luna_str):
        """
        Afiseaza toate evenimentele dintr-o anumita luna, ordonate crescator dupa data si descrescator dupa timp.
        :param luna_str: sir de caractere reprezentand nr lunii (ex: "01" pentru ianuarie)
        :return: Lista evenimentelor din luna respectiva, ordonate dupa cerinta
        """
        evenimente = self.__repo_evenimente.get_all()
        evenimente_luna = [] #initializam o lista goala

        for eveniment in evenimente:
            data_eveniment = eveniment.get_data()
            luna_eveniment = data_eveniment.split('-')[1] #obtinem luna

            if luna_eveniment == luna_str:
                evenimente_luna.append(eveniment)

        evenimente_luna.sort(key=lambda ev: (ev.get_data(), -int(ev.get_timp())))

        return evenimente_luna
    def get_all_inscrieri(self):
        return self.__repo_participare.get_all()