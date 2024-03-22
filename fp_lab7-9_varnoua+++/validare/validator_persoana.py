from erori.validation_error import ValidError

class ValidatorPersoana:
    def __init__(self):
        pass

    def valideaza(self,persoana):
        erori = ""
        if persoana.get_personID() < 0:
            erori += "id invalid!\n"
        if persoana.get_nume() == "":
            erori += "nume invalid!\n"
        if persoana.get_adresa() == "":
            erori += "adresa invalida!\n"
        if len(erori) > 0:
            raise ValidError(erori)