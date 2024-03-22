from erori.validation_error import ValidError

class ValidatorParticipare:
    def __init__(self):
        pass

    def valideaza(self,participare):
        erori = ""
        if participare.get_id_participare() < 0:
            erori += "id invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)