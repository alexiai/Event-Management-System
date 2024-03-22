from infrastructura.repository_file_eveniment import RepositoryFileEveniment
from infrastructura.repository_file_participare import RepositoryFileParticipare
from infrastructura.repository_file_persoana import RepositoryFilePersoana
from validare.validator_persoana import ValidatorPersoana
from validare.validator_eveniment import ValidatorEveniment
from validare.validator_participare import ValidatorParticipare
from infrastructura.reposistory_persoana import RepoPersoana
from infrastructura.repository_eveniment import RepoEveniment
from infrastructura.repository_participare import RepoParticipare
from business.service_persoana import ServicePersoana
from business.service_eveniment import ServiceEveniment
from business.service_participare import ServiceParticipare
from prezentare.consola import UI
from testare.teste import Teste

if __name__ == '__main__':
    print("1.Ruleaza cu fisiere\n2.Ruleaza cu memorie")
    cmd=int(input(">>>"))
    if cmd==1:
        rP=RepositoryFilePersoana('persoane.txt')
        vP=ValidatorPersoana()
        sP=ServicePersoana(vP,rP)
        rE = RepositoryFileEveniment('evenimente.txt')
        vE = ValidatorEveniment()
        sE = ServiceEveniment(vE, rE)
        rPar = RepositoryFileParticipare('participari.txt')
        vPar = ValidatorParticipare()
        sPar = ServiceParticipare(vPar, rPar, rP, rE)
        consola=UI(sP,sE,sPar)
        teste = Teste()
        #teste.ruleaza_toate_testele()
        consola.run()

    else:
        if cmd==2:
            validator_persoana = ValidatorPersoana()
            validator_eveniment = ValidatorEveniment()
            validator_participare = ValidatorParticipare()
            repo_persoana = RepoPersoana()
            repo_eveniment = RepoEveniment()
            repo_participare = RepoParticipare()
            service_persoana = ServicePersoana(validator_persoana, repo_persoana)
            service_eveniment = ServiceEveniment(validator_eveniment, repo_eveniment)
            service_participare = ServiceParticipare(validator_participare, repo_participare, repo_persoana,
                                                     repo_eveniment)
            consola = UI(service_persoana, service_eveniment, service_participare)
            teste = Teste()
            teste.ruleaza_toate_testele()
            consola.run()
