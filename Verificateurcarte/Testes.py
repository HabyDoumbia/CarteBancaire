from Banque import Banque
from MasterCarteVerificateur import MasterCarteVerficateur

class Testes:
    def main(self):
        masterverif=MasterCarteVerficateur();
        verificateur = Banque()
        verificateur.verifierlacarte("5457325394612041")
