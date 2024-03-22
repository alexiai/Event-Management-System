from erori.validation_error import ValidError

class ValidatorEveniment:
    def __init__(self):
        pass

    def valideaza(self,eveniment):
        erori = ""
        if eveniment.get_id_eveniment() < 0:
            erori += "id invalid!\n"
        if eveniment.get_data() == "":
            erori += "data invalida!\n"
        if eveniment.get_timp() == "":
            erori += "timp invalid!\n"
        if eveniment.get_descriere() == "":
            erori += "descriere invalida!\n"
        if len(erori) > 0:
            raise ValidError(erori)